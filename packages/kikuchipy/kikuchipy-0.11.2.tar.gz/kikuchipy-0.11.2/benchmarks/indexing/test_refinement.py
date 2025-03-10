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

import numpy as np
from orix.crystal_map import CrystalMap, PhaseList
from orix.quaternion import Rotation

import kikuchipy as kp


def ebsd_refinement_benchmark_setup():
    # Load patterns
    s = kp.data.nickel_ebsd_small()
    s.remove_static_background()
    s.remove_dynamic_background()

    # Load master pattern
    mp = kp.data.nickel_ebsd_master_pattern_small(projection="lambert")

    # Define crystal map
    rot1 = np.deg2rad([258, 58, 1])
    rot2 = np.deg2rad([292, 62, 182])
    rot = Rotation.from_euler([rot1, rot2, rot2, rot1, rot2, rot2, rot1, rot2, rot2])
    y, x = np.indices(s.axes_manager.navigation_shape[::-1])
    x = x.flatten() * 1.5
    y = y.flatten() * 1.5
    xmap = CrystalMap(rotations=rot, x=x, y=y, phase_list=PhaseList(mp.phase))

    # Define detector
    sig_shape = s.axes_manager.signal_shape[::-1]
    detector = kp.detectors.EBSDDetector(
        shape=sig_shape,
        pc=(0.42, 0.22, 0.50),
        sample_tilt=70,
    )

    # Signal mask
    signal_mask = ~kp.filters.Window("circular", sig_shape).astype(bool)

    return s, mp, rot, xmap, detector, signal_mask


def test_refine_orientation(benchmark):
    """Benchmark orientation refinement of nine (60, 60) EBSD patterns
    with Nelder-Mead.
    """
    s, mp, rot, xmap, detector, signal_mask = ebsd_refinement_benchmark_setup()

    # Prime the Numba cache by running once
    nav_mask1 = np.ones(xmap.shape, dtype=bool)
    nav_mask1[0, 0] = False
    _ = s.refine_orientation(
        xmap=xmap,
        detector=detector,
        master_pattern=mp,
        energy=20,
        navigation_mask=nav_mask1,
    )

    xmap_ref = benchmark(
        s.refine_orientation,
        xmap=xmap,
        detector=detector,
        master_pattern=mp,
        energy=20,
        signal_mask=signal_mask,
    )

    # Relaxed check of results, just to make sure results are not way
    # off
    assert np.all(xmap_ref.rotations.angle_with(rot, degrees=True) < 0.8)


def test_refine_pc(benchmark):
    """Benchmark projection center (PC) refinement of nine (60, 60) EBSD
    patterns with Nelder-Mead.
    """
    s, mp, rot, xmap, detector, signal_mask = ebsd_refinement_benchmark_setup()
    # Prime the Numba cache by running once
    nav_mask1 = np.ones(xmap.shape, dtype=bool)
    nav_mask1[0, 0] = False
    _ = s.refine_projection_center(
        xmap=xmap,
        detector=detector,
        master_pattern=mp,
        energy=20,
        navigation_mask=nav_mask1,
    )

    _, detector_ref, _ = benchmark(
        s.refine_projection_center,
        xmap=xmap,
        detector=detector,
        master_pattern=mp,
        energy=20,
        signal_mask=signal_mask,
    )

    # Relaxed check of results, just to make sure results are not way
    # off
    assert np.allclose(detector_ref.pc_average, [0.417, 0.219, 0.503], atol=1e-3)
