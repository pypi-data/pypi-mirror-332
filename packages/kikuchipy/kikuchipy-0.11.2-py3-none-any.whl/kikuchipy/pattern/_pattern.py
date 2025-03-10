# Copyright 2019-2024 The kikuchipy developers
#
# This file is part of kikuchipy.
#
# kikuchipy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kikuchipy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kikuchipy. If not, see <http://www.gnu.org/licenses/>.

from typing import Callable

from numba import njit
import numpy as np
from scipy.fft import fft2, fftshift, ifft2, ifftshift, irfft2, rfft2
from scipy.ndimage import gaussian_filter
from skimage.exposure import equalize_adapthist
from skimage.util.dtype import dtype_range

from kikuchipy.filters.fft_barnes import _fft_filter, _fft_filter_setup
from kikuchipy.filters.window import Window


def rescale_intensity(
    pattern: np.ndarray,
    in_range: tuple[int | float, ...] | None = None,
    out_range: tuple[int | float, ...] | None = None,
    dtype_out: str | np.dtype | type | None = None,
    percentiles: tuple[int, int] | tuple[float, float] | None = None,
) -> np.ndarray:
    """Rescale intensities in an EBSD pattern.

    Pattern max./min. intensity is determined from `out_range` or the
    data type range of :class:`numpy.dtype` passed to `dtype_out`.

    This method is based on :func:`skimage.exposure.rescale_intensity`.

    Parameters
    ----------
    pattern
        EBSD pattern.
    in_range
        Min./max. intensity values of the input pattern. If not given,
        it is set to the pattern's min./max intensity.
    out_range
        Min./max. intensity values of the rescaled pattern. If not
        given, it is set to ``dtype_out`` min./max according to
        ``skimage.util.dtype.dtype_range``.
    dtype_out
        Data type of the rescaled pattern. If not given, it is set to
        the same data type as the input pattern.
    percentiles
        Disregard intensities outside these percentiles. Calculated
        per pattern. Will overwrite ``in_range`` if given.

    Returns
    -------
    rescaled_pattern
        Rescaled pattern.
    """
    if dtype_out is None:
        dtype_out = pattern.dtype
    else:
        dtype_out = np.dtype(dtype_out)

    if percentiles is not None:
        in_range = np.nanpercentile(pattern, q=percentiles)

    if in_range is None:
        imin, imax = np.nanmin(pattern), np.nanmax(pattern)
    else:
        imin, imax = in_range
        pattern = np.clip(pattern, imin, imax)

    if out_range is None or out_range in dtype_range:
        try:
            omin, omax = dtype_range[dtype_out.type]
        except KeyError:
            raise KeyError(
                "Could not set output intensity range, since data type "
                f"'{dtype_out}' is not recognised. Use any of '{dtype_range}'."
            )
    else:
        omin, omax = out_range

    return _rescale_with_min_max(pattern, imin, imax, omin, omax).astype(dtype_out)


@njit(cache=True, nogil=True, fastmath=True)
def _rescale_with_min_max(
    pattern: np.ndarray,
    imin: int | float,
    imax: int | float,
    omin: int | float,
    omax: int | float,
) -> np.ndarray:
    """Rescale a pattern to a certain intensity range.

    The intensity range is typically given from a data type, e.g.
    [0, 255] for uint8 or [-1, 1] for float32. The data type and shape
    of ``pattern`` is arbitrary.
    """
    rescaled_pattern = (pattern - imin) / float(imax - imin)
    return rescaled_pattern * (omax - omin) + omin


@njit("float32[:, :](float32[:, :])", cache=True, nogil=True, fastmath=True)
def _rescale_without_min_max(pattern: np.ndarray) -> np.ndarray:
    """Rescale a pattern to the intensity range [-1, 1].

    ``pattern`` must be 2D array of data type float32.
    """
    return _rescale_with_min_max(
        pattern, imin=np.min(pattern), imax=np.max(pattern), omin=-1, omax=1
    )


@njit("float32[:](float32[:])", cache=True, nogil=True, fastmath=True)
def _rescale_without_min_max_1d_float32(pattern: np.ndarray) -> np.ndarray:
    """Rescale a pattern to the intensity range [-1, 1].

    ``pattern`` must be 1D array of data type float32.
    """
    return _rescale_with_min_max(
        pattern, imin=np.min(pattern), imax=np.max(pattern), omin=-1, omax=1
    )


@njit("Tuple((float32[:], float32))(float32[:])", cache=True, nogil=True, fastmath=True)
def _zero_mean_sum_square_1d_float32(pattern: np.ndarray) -> tuple[np.ndarray, float]:
    pattern -= np.mean(pattern)
    return pattern, np.square(pattern).sum()


def _zero_mean(patterns: np.ndarray, axis: int | tuple[int, ...]) -> np.ndarray:
    patterns_mean = np.nanmean(patterns, axis=axis, keepdims=True)
    return patterns - patterns_mean


def _normalize(patterns: np.ndarray, axis: int | tuple[int, ...]) -> np.ndarray:
    patterns_squared = patterns**2
    patterns_norm = np.nansum(patterns_squared, axis=axis, keepdims=True)
    patterns_norm_squared = patterns_norm**0.5
    return patterns / patterns_norm_squared


def normalize_intensity(
    pattern: np.ndarray,
    num_std: int = 1,
    divide_by_square_root: bool = False,
    dtype_out: type | None = None,
) -> np.ndarray:
    """Normalize image intensities to a mean of zero and a given
    standard deviation.

    Data type is preserved.

    Parameters
    ----------
    pattern
        EBSD pattern.
    num_std
        Number of standard deviations of the output intensities (default
        is ``1``).
    divide_by_square_root
        Whether to divide output intensities by the square root of the
        image size (default is ``False``).
    dtype_out
        Data type of the normalized pattern. If not given, it is set to
        the same data type as the input pattern.

    Returns
    -------
    normalized_pattern
        Normalized pattern.

    Notes
    -----
    Data type should always be changed to floating point, e.g.
    ``float32`` with :meth:`numpy.ndarray.astype`, before normalizing
    the intensities.
    """
    normalized_pattern = _normalize_intensity(pattern, num_std, divide_by_square_root)

    if dtype_out is not None:
        normalized_pattern = normalized_pattern.astype(dtype_out)

    return normalized_pattern


@njit(cache=True, fastmath=True, nogil=True)
def _normalize_intensity(
    pattern: np.ndarray,
    num_std: int = 1,
    divide_by_square_root: bool = False,
) -> np.ndarray:
    pattern_mean = np.mean(pattern)
    pattern_std = np.std(pattern)
    pattern = pattern - pattern_mean
    if divide_by_square_root:
        return pattern / (num_std * pattern_std * np.sqrt(pattern.size))
    else:
        return pattern / (num_std * pattern_std)


def fft(
    pattern: np.ndarray,
    apodization_window: np.ndarray | Window | None = None,
    shift: bool = False,
    real_fft_only: bool = False,
    **kwargs,
) -> np.ndarray:
    """Compute the discrete Fast Fourier Transform (FFT) of an EBSD
    pattern.

    Very light wrapper around routines in :mod:`scipy.fft`. The routines
    are wrapped instead of used directly to accommodate easy setting of
    ``shift`` and ``real_fft_only``.

    Parameters
    ----------
    pattern
        EBSD pattern.
    apodization_window
        An apodization window to apply before the FFT in order to
        suppress streaks.
    shift
        Whether to shift the zero-frequency component to the centre of
        the spectrum (default is ``False``).
    real_fft_only
        If ``True``, the discrete FFT is computed for real input using
        :func:`scipy.fft.rfft2`. If ``False`` (default), it is computed
        using :func:`scipy.fft.fft2`.
    **kwargs
        Keyword arguments pass to :func:`scipy.fft.fft2` or
        :func:`scipy.fft.rfft2`.

    Returns
    -------
    out
        The result of the 2D FFT.
    """
    if apodization_window is not None:
        pattern = pattern.astype(np.float64)
        pattern *= apodization_window

    if real_fft_only:
        fft_use = rfft2
    else:
        fft_use = fft2

    if shift:
        out = fftshift(fft_use(pattern, **kwargs))
    else:
        out = fft_use(pattern, **kwargs)

    return out


def ifft(
    fft_pattern: np.ndarray,
    shift: bool = False,
    real_fft_only: bool = False,
    **kwargs,
) -> np.ndarray:
    """Compute the inverse Fast Fourier Transform (IFFT) of an FFT of an
    EBSD pattern.

    Very light wrapper around routines in :mod:`scipy.fft`. The routines
    are wrapped instead of used directly to accommodate easy setting of
    ``shift`` and ``real_fft_only``.

    Parameters
    ----------
    fft_pattern
        FFT of EBSD pattern.
    shift
        Whether to shift the zero-frequency component back to the
        corners of the spectrum (default is ``False``).
    real_fft_only
        If ``True``, the discrete IFFT is computed for real input using
        :func:`scipy.fft.irfft2`. If ``False`` (default), it is computed
        using :func:`scipy.fft.ifft2`.
    **kwargs
        Keyword arguments pass to :func:`scipy.fft.ifft`.

    Returns
    -------
    pattern
        Real part of the IFFT of the EBSD pattern.
    """
    if real_fft_only:
        fft_use = irfft2
    else:
        fft_use = ifft2

    if shift:
        pattern = fft_use(ifftshift(fft_pattern, **kwargs))
    else:
        pattern = fft_use(fft_pattern, **kwargs)

    return np.real(pattern)


def fft_filter(
    pattern: np.ndarray,
    transfer_function: np.ndarray | Window,
    apodization_window: np.ndarray | Window | None = None,
    shift: bool = False,
) -> np.ndarray:
    """Filter an EBSD patterns in the frequency domain.

    Parameters
    ----------
    pattern
        EBSD pattern.
    transfer_function
        Filter transfer function in the frequency domain.
    apodization_window
        An apodization window to apply before the FFT in order to
        suppress streaks.
    shift
        Whether to shift the zero-frequency component to the centre of
        the spectrum. Default is ``False``.

    Returns
    -------
    filtered_pattern
        Filtered EBSD pattern.
    """
    # Get the FFT
    pattern_fft = fft(pattern, shift=shift, apodization_window=apodization_window)

    # Apply the transfer function to the FFT
    filtered_fft = pattern_fft * transfer_function

    # Get real part of IFFT of the filtered FFT
    return np.real(ifft(filtered_fft, shift=shift))


@njit(cache=True, fastmath=True, nogil=True)
def fft_spectrum(fft_pattern: np.ndarray) -> np.ndarray:
    """Compute the FFT spectrum of a Fourier transformed EBSD pattern.

    Parameters
    ----------
    fft_pattern
        Fourier transformed EBSD pattern.

    Returns
    -------
    spectrum
        2D FFT spectrum of the EBSD pattern.
    """
    return np.sqrt(fft_pattern.real**2 + fft_pattern.imag**2)


def fft_frequency_vectors(shape: tuple[int, int]) -> np.ndarray:
    """Get the frequency vectors in a Fourier Transform spectrum.

    Parameters
    ----------
    shape
        Fourier transform shape.

    Returns
    -------
    frequency_vectors
        Frequency vectors.
    """
    sy, sx = shape

    linex = np.arange(sx) + 1
    linex[sx // 2 :] -= sx + 1
    liney = np.arange(sy) + 1
    liney[sy // 2 :] -= sy + 1

    frequency_vectors = np.empty(shape=(sy, sx))
    for i in range(sy):
        frequency_vectors[i] = liney[i] ** 2 + linex**2 - 1

    return frequency_vectors


@njit(cache=True, fastmath=True, nogil=True)
def _remove_static_background_subtract(
    pattern: np.ndarray,
    static_bg: np.ndarray,
    dtype_out: np.dtype,
    omin: int | float,
    omax: int | float,
    scale_bg: bool,
) -> np.ndarray:
    """Remove static background from a pattern by subtraction."""
    pattern = pattern.astype(np.float32)
    if scale_bg:
        static_bg = _rescale_with_min_max(
            static_bg,
            imin=np.min(static_bg),
            imax=np.max(static_bg),
            omin=np.min(pattern),
            omax=np.max(pattern),
        )
    pattern = _remove_background_subtract(pattern, static_bg, omin, omax)
    return pattern.astype(dtype_out)


@njit(cache=True, fastmath=True, nogil=True)
def _remove_static_background_divide(
    pattern: np.ndarray,
    static_bg: np.ndarray,
    dtype_out: np.dtype,
    omin: int | float,
    omax: int | float,
    scale_bg: bool,
) -> np.ndarray:
    """Remove static background from a pattern by division."""
    pattern = pattern.astype(np.float32)
    if scale_bg:
        static_bg = _rescale_with_min_max(
            static_bg,
            imin=np.min(static_bg),
            imax=np.max(static_bg),
            omin=np.min(pattern),
            omax=np.max(pattern),
        )
    pattern = _remove_background_divide(pattern, static_bg, omin, omax)
    return pattern.astype(dtype_out)


def _remove_dynamic_background(
    pattern: np.ndarray,
    filter_func: Callable,
    operation: str,
    dtype_out: np.dtype,
    omin: int | float,
    omax: int | float,
    **kwargs,
) -> np.ndarray:
    """Remove dynamic background from a pattern.

    The dynamic background is generated by blurring the pattern in the
    frequency or the spatial domain. The background is removed by
    subtraction or division.

    Parameters
    ----------
    pattern
        Pattern to remove background from.
    filter_func
        Function to generate dynamic background with: either
        :func:`kikuchipy._pattern.fft_barnes._fft_filter` or
        :func:`scipy.ndimage.gaussian_filter`.
    operation
        Either ``"subtract"`` or ``"divide"``.
    dtype_out
        Data type to cast the output pattern to.
    omin, omax
        Output intensity range.
    **kwargs
        Keyword arguments passed to ``filter_func``.

    Returns
    -------
    pattern_out
        Pattern without dynamic background.
    """
    pattern = pattern.astype(np.float32)
    dynamic_bg = filter_func(pattern, **kwargs)
    if operation == "subtract":
        pattern = _remove_background_subtract(pattern, dynamic_bg, omin, omax)
    else:
        pattern = _remove_background_divide(pattern, dynamic_bg, omin, omax)
    return pattern.astype(dtype_out)


@njit(cache=True, fastmath=True, nogil=True)
def _remove_background_subtract(
    pattern: np.ndarray,
    background: np.ndarray,
    omin: int | float,
    omax: int | float,
) -> np.ndarray:
    """Remove background from pattern by subtraction and rescale."""
    pattern -= background
    imin = np.min(pattern)
    imax = np.max(pattern)
    return _rescale_with_min_max(pattern, imin, imax, omin, omax)


@njit(cache=True, fastmath=True, nogil=True)
def _remove_background_divide(
    pattern: np.ndarray,
    background: np.ndarray,
    omin: int | float,
    omax: int | float,
) -> np.ndarray:
    """Remove background from pattern by division and rescale."""
    pattern /= background
    imin = np.min(pattern)
    imax = np.max(pattern)
    return _rescale_with_min_max(pattern, imin, imax, omin, omax)


def remove_dynamic_background(
    pattern: np.ndarray,
    operation: str = "subtract",
    filter_domain: str = "frequency",
    std: int | float | None = None,
    truncate: int | float = 4.0,
    dtype_out: (
        str | np.dtype | type | tuple[int, int] | tuple[float, float] | None
    ) = None,
) -> np.ndarray:
    """Remove the dynamic background in an EBSD pattern.

    The removal is performed by subtracting or dividing by a Gaussian
    blurred version of the pattern. The blurred version is obtained
    either in the frequency domain, by a low pass Fast Fourier Transform
    (FFT) Gaussian filter, or in the spatial domain by a Gaussian
    filter. Returned pattern intensities are rescaled to fill the input
    data type range.

    Parameters
    ----------
    pattern
        EBSD pattern.
    operation
        Whether to ``"subtract"`` (default) or ``"divide"`` by the
        dynamic background pattern.
    filter_domain
        Whether to obtain the dynamic background by applying a Gaussian
        convolution filter in the ``"frequency"`` (default) or
        ``"spatial"`` domain.
    std
        Standard deviation of the Gaussian window. If not given, it is
        set to width/8.
    truncate
        Truncate the Gaussian window at this many standard deviations.
        Default is ``4.0``.
    dtype_out
        Data type of corrected pattern. If not given, it is set to
        input patterns' data type.

    Returns
    -------
    corrected_pattern
        Pattern with the dynamic background removed.

    See Also
    --------
    kikuchipy.signals.EBSD.remove_dynamic_background,
    kikuchipy.pattern.remove_dynamic_background
    """
    if std is None:
        std = pattern.shape[1] / 8

    if dtype_out is None:
        dtype_out = pattern.dtype
    else:
        dtype_out = np.dtype(dtype_out)

    if filter_domain == "frequency":
        (
            fft_shape,
            kernel_shape,
            kernel_fft,
            offset_before_fft,
            offset_after_ifft,
        ) = _dynamic_background_frequency_space_setup(
            pattern_shape=pattern.shape, std=std, truncate=truncate
        )
        dynamic_bg = _fft_filter(
            image=pattern,
            fft_shape=fft_shape,
            window_shape=kernel_shape,
            transfer_function=kernel_fft,
            offset_before_fft=offset_before_fft,
            offset_after_ifft=offset_after_ifft,
        )
    elif filter_domain == "spatial":
        dynamic_bg = gaussian_filter(input=pattern, sigma=std, truncate=truncate)
    else:
        filter_domains = ["frequency", "spatial"]
        raise ValueError(f"{filter_domain} must be either of {filter_domains}.")

    # Remove dynamic background
    omin, omax = dtype_range[dtype_out.type]
    if operation == "subtract":
        corrected = _remove_background_subtract(pattern, dynamic_bg, omin, omax)
    else:
        corrected = _remove_background_divide(pattern, dynamic_bg, omin, omax)

    return corrected.astype(dtype_out)


def _dynamic_background_frequency_space_setup(
    pattern_shape: list[int] | tuple[int, int],
    std: int | float,
    truncate: int | float,
) -> tuple[
    tuple[int, int], tuple[int, int], np.ndarray, tuple[int, int], tuple[int, int]
]:
    # Get Gaussian filtering window
    shape = (int(truncate * std),) * 2
    window = Window("gaussian", std=std, shape=shape)
    window = window / (2 * np.pi * std**2)
    window /= np.sum(window)

    # FFT filter setup
    (
        fft_shape,
        transfer_function,
        offset_before_fft,
        offset_after_ifft,
    ) = _fft_filter_setup(pattern_shape, window)

    return (
        fft_shape,
        window.shape,
        transfer_function,
        offset_before_fft,
        offset_after_ifft,
    )


def get_dynamic_background(
    pattern: np.ndarray,
    filter_domain: str = "frequency",
    std: int | float | None = None,
    truncate: int | float = 4.0,
) -> np.ndarray:
    """Get the dynamic background in an EBSD pattern.

    The background is obtained either in the frequency domain, by a low
    pass Fast Fourier Transform (FFT) Gaussian filter, or in the spatial
    domain by a Gaussian filter.

    Data type is preserved.

    Parameters
    ----------
    pattern
        EBSD pattern.
    filter_domain
        Whether to obtain the dynamic background by applying a Gaussian
        convolution filter in the ``"frequency"`` (default) or
        ``"spatial"`` domain.
    std
        Standard deviation of the Gaussian window. If not given, a
        deviation of pattern width/8 is chosen.
    truncate
        Truncate the Gaussian window at this many standard deviations.
        Default is ``4.0``.

    Returns
    -------
    dynamic_bg
        The dynamic background.
    """
    if std is None:
        std = pattern.shape[1] / 8

    if filter_domain == "frequency":
        (
            fft_shape,
            kernel_shape,
            kernel_fft,
            offset_before_fft,
            offset_after_ifft,
        ) = _dynamic_background_frequency_space_setup(
            pattern_shape=pattern.shape, std=std, truncate=truncate
        )
        dynamic_bg = _fft_filter(
            image=pattern,
            fft_shape=fft_shape,
            window_shape=kernel_shape,
            transfer_function=kernel_fft,
            offset_before_fft=offset_before_fft,
            offset_after_ifft=offset_after_ifft,
        )
    elif filter_domain == "spatial":
        dynamic_bg = gaussian_filter(input=pattern, sigma=std, truncate=truncate)
    else:
        filter_domains = ["frequency", "spatial"]
        raise ValueError(f"{filter_domain} must be either of {filter_domains}.")

    return dynamic_bg.astype(pattern.dtype)


def get_image_quality(
    pattern: np.ndarray,
    normalize: bool = True,
    frequency_vectors: np.ndarray | None = None,
    inertia_max: int | float | None = None,
) -> float:
    """Return the image quality of an EBSD pattern.

    The image quality is calculated based on the procedure defined by
    Krieger Lassen :cite:`lassen1994automated`.

    Parameters
    ----------
    pattern
        EBSD pattern.
    normalize
        Whether to normalize the pattern to a mean of zero and standard
        deviation of 1 before calculating the image quality (default is
        ``True``).
    frequency_vectors
        Integer 2D array assigning each FFT spectrum frequency component
        a weight. If not given, these are calculated from
        :func:`~kikuchipy.pattern.fft_frequency_vectors`. This only
        depends on the pattern shape.
    inertia_max
        Maximum possible inertia of the FFT power spectrum of the image.
        If not given, this is calculated from the
        ``frequency_vectors``, which in this case *must* be passed. This
        only depends on the pattern shape.

    Returns
    -------
    image_quality
        Image quality of the pattern.
    """
    if frequency_vectors is None:
        sy, sx = pattern.shape
        frequency_vectors = fft_frequency_vectors((sy, sx))

    if inertia_max is None:
        sy, sx = pattern.shape
        inertia_max = np.sum(frequency_vectors) / (sy * sx)

    return _get_image_quality(pattern, normalize, frequency_vectors, inertia_max)


def _get_image_quality(
    pattern: np.ndarray,
    normalize: bool,
    frequency_vectors: np.ndarray,
    inertia_max: float,
) -> float:
    """See docstring of :func:`get_image_quality`."""
    pattern = pattern.astype(np.float32)

    if normalize:
        pattern = normalize_intensity(pattern)

    # Compute FFT
    # TODO: Reduce frequency vectors to real part only to enable real part FFT
    fft_pattern = fft2(pattern)

    return _get_image_quality_numba(fft_pattern, frequency_vectors, inertia_max)


@njit(cache=True, fastmath=True, nogil=True)
def _get_image_quality_numba(
    fft_pattern: np.ndarray, frequency_vectors: np.ndarray, inertia_max: float
) -> float:
    # Obtain (un-shifted) FFT spectrum
    spectrum = fft_spectrum(fft_pattern)

    # Calculate inertia (see Lassen1994)
    inertia = np.sum(spectrum * frequency_vectors) / np.sum(spectrum)

    return 1 - (inertia / inertia_max)


@njit("float32[:, :](float32[:, :], int64)", cache=True, fastmath=True, nogil=True)
def _bin2d(pattern: np.ndarray, factor: int) -> np.ndarray:
    n_rows_new = pattern.shape[0] // factor
    n_cols_new = pattern.shape[1] // factor

    new_pattern = np.zeros((n_rows_new, n_cols_new), dtype=pattern.dtype)

    for r in range(n_rows_new):
        for rr in range(r * factor, (r + 1) * factor):
            for c in range(n_cols_new):
                value = new_pattern[r, c]
                for cc in range(c * factor, (c + 1) * factor):
                    value += pattern[rr, cc]
                new_pattern[r, c] = value

    return new_pattern


@njit(cache=True, fastmath=True, nogil=True)
def _downsample2d(
    pattern: np.ndarray,
    factor: int,
    omin: int | float,
    omax: int | float,
    dtype_out: np.dtype,
) -> np.ndarray:
    pattern = pattern.astype(np.float32)
    binned_pattern = _bin2d(pattern, factor)
    imin = np.min(binned_pattern)
    imax = np.max(binned_pattern)
    rescaled_pattern = _rescale_with_min_max(binned_pattern, imin, imax, omin, omax)
    return rescaled_pattern.astype(dtype_out)


def _adaptive_histogram_equalization(
    image: np.ndarray,
    kernel_size: tuple[int, int] | list[int],
    clip_limit: int | float = 0,
    nbins: int = 128,
) -> np.ndarray:
    """Local contrast enhancement with adaptive histogram equalization.

    This method makes use of
    :func:`skimage.exposure.equalize_adapthist`.

    Parameters
    ----------
    image
        Image (e.g. EBSD pattern).
    kernel_size
        Shape of contextual regions for adaptive histogram equalization.
    clip_limit
        Clipping limit, normalized between 0 and 1 (higher values give
        more contrast). Default is 0.
    nbins
        Number of gray bins for histogram. Default is 128.

    Returns
    -------
    image_eq
        Image with enhanced contrast.
    """
    image_eq = equalize_adapthist(image, kernel_size, clip_limit, nbins)
    image_eq = rescale_intensity(image_eq, dtype_out=image.dtype.type)
    return image_eq
