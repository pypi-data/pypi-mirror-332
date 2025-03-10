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

"""Convenience functions for creating HyperSpy signals to use as
navigators with :meth:`~hyperspy.signals.Signal2D.plot`.
"""

import hyperspy.api as hs
import numpy as np
from skimage.exposure import rescale_intensity


def get_rgb_navigator(
    image: np.ndarray, dtype: str | np.dtype | type = "uint16"
) -> hs.signals.Signal2D:
    """Create an RGB navigator signal which is suitable to pass to
    :meth:`~hyperspy._signals.signal2d.Signal2D.plot` as the
    ``navigator`` parameter.

    Parameters
    ----------
    image
        RGB color image of shape ``(n rows, n columns, 3)``.
    dtype
        Which data type to cast the signal data to, either ``"uint16"``
        (default) or ``"uint8"``. Must be a valid :class:`numpy.dtype`
        identifier.

    Returns
    -------
    s
        Signal with an (n columns, n rows) signal shape and no
        navigation shape, of data type either ``rgb8`` or ``rgb16``.
    """
    dtype = np.dtype(dtype)
    image_rescaled = rescale_intensity(image, out_range=dtype.type).astype(dtype)
    s = hs.signals.Signal2D(image_rescaled)
    s = s.transpose(signal_axes=1)
    s.change_dtype({"uint8": "rgb8", "uint16": "rgb16"}[dtype.name])
    return s
