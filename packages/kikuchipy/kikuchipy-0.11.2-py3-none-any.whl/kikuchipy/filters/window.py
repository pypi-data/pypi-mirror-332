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

from __future__ import annotations

from copy import copy
from typing import Sequence

from dask.array import Array
import matplotlib.figure as mfigure
from matplotlib.pyplot import subplots
from numba import njit
import numpy as np
from scipy.signal.windows import get_window


class Window(np.ndarray):
    """A window/kernel/mask/filter of a given shape with some values.

    This class is a subclass of :class:`numpy.ndarray` with some
    additional convenience methods.

    It can be used to create a transfer function for filtering in the
    frequency domain, create an averaging window for averaging patterns
    with their nearest neighbours, and so on.

    Parameters
    ----------
    window
        Window type to create. Available types are listed in
        :func:`scipy.signal.windows.get_window` and includes
        "rectangular" and "gaussian", in addition to a "circular" window
        (default) filled with ones in which corner data are set to zero,
        a "modified_hann" window and "lowpass" and "highpass" FFT
        windows. A window element is considered to be in a corner if its
        radial distance to the origin (window center) is shorter or
        equal to the half width of the windows's longest axis. A 1D or
        2D :class:`numpy.ndarray` or :class:`dask.array.Array` can also
        be passed.
    shape
        Shape of the window. Not used if a custom window is passed to
        *window*. This can be either 1D or 2D, and can be asymmetrical.
        Default is (3, 3).
    **kwargs
        Required keyword arguments passed to the window type.

    See Also
    --------
    scipy.signal.windows.get_window

    Examples
    --------
    >>> import numpy as np
    >>> import kikuchipy as kp

    The following passed parameters are the default

    >>> w = kp.filters.Window(window="circular", shape=(3, 3))
    >>> w
    Window (3, 3) circular
    [[0. 1. 0.]
     [1. 1. 1.]
     [0. 1. 0.]]

    A window can be made circular

    >>> w = kp.filters.Window(window="rectangular")
    >>> w
    Window (3, 3) rectangular
    [[1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]]
    >>> w.make_circular()
    >>> w
    Window (3, 3) circular
    [[0. 1. 0.]
     [1. 1. 1.]
     [0. 1. 0.]]

    A custom window can be created

    >>> w = kp.filters.Window(np.arange(6).reshape(3, 2))
    >>> w
    Window (3, 2) custom
    [[0 1]
     [2 3]
     [4 5]]

    To create a Gaussian window with a standard deviation of 2, obtained
    from :func:`scipy.signal.windows.gaussian`

    >>> w = kp.filters.Window(window="gaussian", std=2)
    >>> w
    Window (3, 3) gaussian
    [[0.7788 0.8825 0.7788]
     [0.8825 1.     0.8825]
     [0.7788 0.8825 0.7788]]
    """

    _name: str | None = None
    _circular: bool = False

    def __new__(
        cls,
        window: str | np.ndarray | Array | None = None,
        shape: Sequence[int] | None = None,
        **kwargs,
    ) -> Window:
        if window is None:
            window = "circular"

        if shape is None and "Nx" not in kwargs.keys():
            shape = (3, 3)
        elif "Nx" in kwargs.keys():
            shape = (kwargs.pop("Nx"),)
        else:
            try:
                shape = tuple(shape)
                if any(np.array(shape) < 1):
                    raise ValueError(f"All window axes {shape} must be > 0.")
                if any(isinstance(i, float) for i in np.array(shape)):
                    raise TypeError
            except TypeError:
                raise TypeError(f"Window shape {shape} must be a sequence of ints.")

        exclude_window_corners = False
        if isinstance(window, np.ndarray) or isinstance(window, Array):
            name = "custom"
            data = window
        elif isinstance(window, str):
            window_kwargs = {}
            if window == "modified_hann":
                name = window
                window_func = modified_hann
                window_kwargs["Nx"] = shape[0]
            elif window in ["lowpass", "highpass"]:
                name = window
                if window == "lowpass":
                    window_func = lowpass_fft_filter
                else:
                    window_func = highpass_fft_filter

                window_kwargs = {
                    "shape": shape,
                    "cutoff": kwargs["cutoff"],
                    "cutoff_width": kwargs.pop("cutoff_width", None),
                }
            else:  # Get window from SciPy
                if window == "circular":
                    exclude_window_corners = True
                    window = "rectangular"
                name = window
                window_func = get_window
                window_kwargs["fftbins"] = kwargs.pop("fftbins", False)
                window_kwargs["Nx"] = kwargs.pop("Nx", shape[0])
                window_kwargs["window"] = (window,) + tuple(kwargs.values())
            data = window_func(**window_kwargs)
            if len(shape) == 2 and data.ndim == 1:
                window_kwargs["Nx"] = shape[1]
                data = np.outer(data, window_func(**window_kwargs))
        else:
            raise ValueError(
                f"Window {type(window)} must be of type numpy.ndarray, "
                "dask.array.Array, or a valid string"
            )

        obj = np.asarray(data).view(cls)
        obj._name = name

        if exclude_window_corners:
            obj.make_circular()

        return obj

    def __array_finalize__(self, obj) -> None:
        if obj is None:
            return
        self._name = getattr(obj, "_name", None)
        self._circular = getattr(obj, "_circular", False)

    def __array_wrap__(
        self, obj, context=None, return_scalar=False
    ) -> Window | np.ndarray:
        if obj.shape == ():
            return obj[()]
        else:
            return np.ndarray.__array_wrap__(self, obj, context, return_scalar)

    def __repr__(self) -> str:
        cls = self.__class__.__name__
        shape = str(self.shape)
        name = self.name
        data = np.array_str(self, precision=4, suppress_small=True)
        return f"{cls} {shape} {name}\n{data}"

    @property
    def circular(self) -> bool:
        """Return whether the window is circular."""
        return self._circular

    @property
    def distance_to_origin(self) -> np.ndarray:
        """Return the radial distance for each pixel to the window
        origin.
        """
        return distance_to_origin(self.shape, self.origin)

    @property
    def is_valid(self) -> bool:
        """Return whether the window is in a valid state."""
        return (
            isinstance(self.name, str)
            and (isinstance(self, np.ndarray) or isinstance(self, Array))
            and self.ndim < 3
            and isinstance(self.circular, bool)
        )

    @property
    def n_neighbours(self) -> tuple:
        """Return the maximum number of nearest neighbours in each
        navigation axis to the origin.
        """
        return tuple(np.subtract(self.shape, self.origin) - 1)

    @property
    def name(self) -> str:
        """Return the name of the window."""
        return self._name

    @property
    def origin(self) -> tuple[int, ...]:
        """Return the window origin."""
        return tuple(i // 2 for i in self.shape)

    def make_circular(self) -> None:
        """Make the window circular.

        The data of window elements who's radial distance to the
        window origin is shorter or equal to the half width of the
        window's longest axis are set to zero. This has no effect if the
        window has only one axis.
        """
        if self.ndim == 1:
            return

        # Get mask
        mask = self.distance_to_origin > max(self.origin)

        # Update data
        self[mask] = 0
        self._circular = True

        # Update name
        if self.name in ["rectangular", "boxcar"]:
            self._name = "circular"

    def shape_compatible(self, shape: tuple[int, ...]) -> bool:
        """Return whether the window shape is compatible with another
        shape.

        Parameters
        ----------
        shape
            Shape of data to apply window to.

        Returns
        -------
        is_compatible
            Whether the window shape is compatible with another shape.
        """
        if len(self.shape) > len(shape) or any(np.array(self.shape) > np.array(shape)):
            return False
        else:
            return True

    def plot(
        self,
        grid: bool = True,
        show_values: bool = True,
        textcolors: list[str] | None = None,
        cmap: str = "viridis",
        cmap_label: str = "Value",
        colorbar: bool = True,
        return_figure: bool = False,
    ) -> mfigure.Figure | None:
        """Plot window values with indices relative to the origin.

        Parameters
        ----------
        grid
            Whether to separate each value with a white spacing in a
            grid. Default is True.
        show_values
            Whether to show values as text in centre of element. Default
            is True.
        textcolors
            A list of two colors. The first is used for values below a
            threshold, the second for those above. If not given
            (default), this is set to ["white", "black"].
        cmap
            A colormap to color data with, available in
            :class:`matplotlib.colors.ListedColormap`. Default is
            "viridis".
        cmap_label
            Colormap label. Default is "Value".
        colorbar
            Whether to show the colorbar. Default is True.
        return_figure
            Whether to return the figure. Default is False.

        Returns
        -------
        fig
            Figure returned if *return_figure* is True.

        Examples
        --------
        A plot of window data with indices relative to the origin,
        showing element values and x/y ticks, can be produced and
        written to file

        >>> import kikuchipy as kp
        >>> w = kp.filters.Window()
        >>> fig = w.plot(return_figure=True)
        >>> fig.savefig('my_kernel.png')
        """
        if not self.is_valid:
            raise ValueError("Window is invalid")

        w = self.copy()

        if w.ndim == 1:
            w = np.expand_dims(w, axis=w.ndim)

        fig, ax = subplots()
        image = ax.imshow(w, cmap=cmap, interpolation=None)

        if colorbar:
            cbar = ax.figure.colorbar(image, ax=ax)
            cbar.ax.set_ylabel(cmap_label, rotation=-90, va="bottom")

        # Set plot ticks
        ky, kx = w.shape
        oy, ox = w.origin
        ax.set_xticks(np.arange(kx))
        ax.set_xticks(np.arange(kx + 1) - 0.5, minor=True)
        ax.set_xticklabels(np.arange(kx) - ox)
        ax.set_yticks(np.arange(ky))
        ax.set_yticklabels(np.arange(ky) - oy)
        ax.set_yticks(np.arange(ky + 1) - 0.5, minor=True)

        if grid:  # Create grid
            for spine in ax.spines.values():
                spine.set_visible(False)
            ax.grid(which="minor", color="w", linestyle="-", linewidth=3)
            ax.tick_params(which="minor", bottom=False, left=False)

        if show_values:
            # Enter values of window data as text
            kw = dict(horizontalalignment="center", verticalalignment="center")
            threshold = image.norm(np.amax(w)) / 2.0
            if textcolors is None:
                textcolors = ["white", "black"]
            for idx in np.ndindex(w.shape):
                val = w[idx]
                kw.update(color=textcolors[int(image.norm(val) > threshold)])
                coeff_str = str(round(val, 4) if val % 1 else int(val))
                image.axes.text(idx[1], idx[0], coeff_str, **kw)

        if return_figure:
            return fig


def distance_to_origin(
    shape: tuple[int] | tuple[int, int],
    origin: tuple[int] | tuple[int, int] | None = None,
) -> np.ndarray:
    """Return the distance to the window origin in pixels.

    Parameters
    ----------
    shape
        Window shape.
    origin
        Window origin. If not given, half the shape is used as origin
        for each axis.

    Returns
    -------
    distance
        Distance to the window origin in pixels.
    """
    if origin is None:
        origin = tuple(i // 2 for i in shape)
    coordinates = np.ogrid[tuple(slice(None, i) for i in shape)]
    if len(origin) == 2:
        squared = [(i - o) ** 2 for i, o in zip(coordinates, origin)]
        distance = np.sqrt(np.add.outer(*squared).squeeze())
    else:
        distance = abs(coordinates[0] - origin[0])
    return distance


@njit
def modified_hann(Nx: int) -> np.ndarray:
    r"""Return a 1D modified Hann window with the maximum value
    normalized to 1.

    Used in :cite:`wilkinson2006high`.

    Parameters
    ----------
    Nx
        Number of points in the window.

    Returns
    -------
    window
        1D Hann window.

    Notes
    -----
    The modified Hann window is defined as

    .. math:: w(x) = \cos\left(\frac{\pi x}{N_x}\right),

    with :math:`x` relative to the window centre.

    Examples
    --------
    >>> import numpy as np
    >>> import kikuchipy as kp
    >>> w1 = kp.filters.modified_hann(Nx=30)
    >>> w2 = kp.filters.Window("modified_hann", shape=(30,))
    >>> np.allclose(w1, w2)
    True
    """
    return np.cos(np.pi * (np.arange(Nx) - (Nx / 2) + 0.5) / Nx)


def lowpass_fft_filter(
    shape: tuple[int, int],
    cutoff: int | float,
    cutoff_width: int | float | None = None,
) -> np.ndarray:
    r"""Return a frequency domain low-pass filter transfer function in
    2D.

    Used in :cite:`wilkinson2006high`.

    Parameters
    ----------
    shape
        Shape of function.
    cutoff
        Cut-off frequency.
    cutoff_width
        Width of cut-off region. If None (default), it is set to half of
        the cutoff frequency.

    Returns
    -------
    window
        2D transfer function.

    Notes
    -----
    The low-pass filter transfer function is defined as

    .. math::

        w(r) = e^{-\left((r - c)/(\sqrt{2}w_c/2)\right)^2},
        w(r) =
        \begin{cases}
        0, & r > c + 2w_c \\
        1, & r < c,
        \end{cases}

    where :math:`r` is the radial distance to the window centre,
    :math:`c` is the cut-off frequency, and :math:`w_c` is the width of
    the cut-off region.

    Examples
    --------
    >>> import numpy as np
    >>> import kikuchipy as kp
    >>> w1 = kp.filters.Window(
    ...     "lowpass", cutoff=30, cutoff_width=15, shape=(96, 96)
    ... )
    >>> w2 = kp.filters.lowpass_fft_filter(
    ...     shape=(96, 96), cutoff=30, cutoff_width=15
    ... )
    >>> np.allclose(w1, w2)
    True
    """
    r = distance_to_origin(shape)

    if cutoff_width is None:
        cutoff_width = cutoff / 2

    window = np.exp(-(((r - cutoff) / (np.sqrt(2) * cutoff_width / 2)) ** 2))
    window[r > (cutoff + (2 * cutoff_width))] = 0
    window[r < cutoff] = 1

    return window


def highpass_fft_filter(
    shape: tuple[int, int],
    cutoff: int | float,
    cutoff_width: int | float | None = None,
) -> np.ndarray:
    r"""Return a frequency domain high-pass filter transfer function in
    2D.

    Used in :cite:`wilkinson2006high`.

    Parameters
    ----------
    shape
        Shape of function.
    cutoff
        Cut-off frequency.
    cutoff_width
        Width of cut-off region. If not given (default), it is set to
        half of the cutoff frequency.

    Returns
    -------
    window
        2D transfer function.

    Notes
    -----
    The high-pass filter transfer function is defined as

    .. math::

        w(r) = e^{-\left((c - r)/(\sqrt{2}w_c/2)\right)^2},
        w(r) =
        \begin{cases}
        0, & r < c - 2w_c\\
        1, & r > c,
        \end{cases}

    where :math:`r` is the radial distance to the window centre,
    :math:`c` is the cut-off frequency, and :math:`w_c` is the width of
    the cut-off region.

    Examples
    --------
    >>> import numpy as np
    >>> import kikuchipy as kp
    >>> w1 = kp.filters.Window(
    ...     "highpass", cutoff=1, cutoff_width=0.5, shape=(96, 96)
    ... )
    >>> w2 = kp.filters.highpass_fft_filter(
    ...     shape=(96, 96), cutoff=1, cutoff_width=0.5
    ... )
    >>> np.allclose(w1, w2)
    True
    """
    r = distance_to_origin(shape)
    if cutoff_width is None:
        cutoff_width = cutoff / 2
    window = np.exp(-(((cutoff - r) / (np.sqrt(2) * cutoff_width / 2)) ** 2))
    window[r < (cutoff - (2 * cutoff_width))] = 0
    window[r > cutoff] = 1
    return window
