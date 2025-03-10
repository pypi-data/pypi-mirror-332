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

import dask
import dask.array as da
import numpy as np

from kikuchipy.indexing.similarity_metrics._similarity_metric import SimilarityMetric


class NormalizedDotProductMetric(SimilarityMetric):
    r"""Similarity metric implementing the normalized dot product
    :cite:`chen2015dictionary`.

    The metric is defined as

    .. math::

        \rho = \frac
        {\langle \mathbf{X}, \mathbf{Y} \rangle}
        {||\mathbf{X}|| \cdot ||\mathbf{Y}||},

    where :math:`{\langle \mathbf{X}, \mathbf{Y} \rangle}` is the dot
    (inner) product of the pattern vectors :math:`\mathbf{X}` and
    :math:`\mathbf{Y}`.

    See :class:`~kikuchipy.indexing.SimilarityMetric` for the
    description of the initialization parameters and the list of
    attributes.
    """

    _allowed_dtypes: list[type] = [np.float32, np.float64]
    _sign: int = 1

    def __call__(
        self,
        experimental: da.Array | np.ndarray,
        dictionary: da.Array | np.ndarray,
    ) -> da.Array:
        """Compute the similarities between experimental patterns and
        simulated dictionary patterns.

        Before calling :meth:`match`, this method calls
        :meth:`prepare_experimental`, reshapes the dictionary patterns
        to 1 navigation dimension and 1 signal dimension, and calls
        :meth:`prepare_dictionary`.

        Parameters
        ----------
        experimental
            Experimental pattern array with as many patterns as
            :attr:`n_experimental_patterns`.
        dictionary
            Dictionary pattern array with as many patterns as
            :attr:`n_dictionary_patterns`.

        Returns
        -------
        similarities
        """
        experimental = self.prepare_experimental(experimental)
        dictionary = dictionary.reshape((self.n_dictionary_patterns, -1))
        dictionary = self.prepare_dictionary(dictionary)
        return self.match(experimental, dictionary)

    def prepare_experimental(
        self, patterns: np.ndarray | da.Array
    ) -> np.ndarray | da.Array:
        """Prepare experimental patterns before matching to dictionary
        patterns in :meth:`match`.

        Patterns are prepared by:
            1. Setting the data type to :attr:`dtype`.
            2. Excluding the experimental patterns where
               :attr:`navigation_mask` is ``False`` if the mask is set.
            3. Reshaping to shape ``(n_experimental_patterns, -1)``.
            4. Applying a signal mask if :attr:`signal_mask` is set.
            5. Rechunking if :attr:`rechunk` is ``True``.
            6. Normalizing to a mean of 0.

        Parameters
        ----------
        patterns
            Experimental patterns.

        Returns
        -------
        prepared_patterns
            Prepared experimental patterns.
        """
        patterns = da.asarray(patterns).astype(self.dtype)

        patterns = patterns.reshape((self.n_experimental_patterns, -1))

        if self.navigation_mask is not None:
            patterns = patterns[~self.navigation_mask.ravel()]

        if self.signal_mask is not None:
            patterns = self._mask_patterns(patterns)

        if self.rechunk:
            patterns = patterns.rechunk(("auto", -1))

        patterns = self._normalize_patterns(patterns)

        return patterns

    def prepare_dictionary(
        self, patterns: np.ndarray | da.Array
    ) -> np.ndarray | da.Array:
        """Prepare dictionary patterns before matching to experimental
        patterns in :meth:`match`.

        Patterns are prepared by:
            1. Setting the data type to :attr:`dtype`.
            2. Applying a signal mask if :attr:`signal_mask` is set.
            3. Normalizing to a mean of 0.

        Parameters
        ----------
        patterns
            Dictionary patterns.

        Returns
        -------
        prepared_patterns
            Prepared dictionary patterns.
        """
        patterns = patterns.astype(self.dtype)

        if self.signal_mask is not None:
            patterns = self._mask_patterns(patterns)

        patterns = self._normalize_patterns(patterns)

        return patterns

    def match(
        self,
        experimental: np.ndarray | da.Array,
        dictionary: np.ndarray | da.Array,
    ) -> da.Array:
        """Match all experimental patterns to all dictionary patterns
        and return their similarities.

        Parameters
        ----------
        experimental
            Experimental patterns.
        dictionary
            Dictionary patterns.

        Returns
        -------
        dot_products
            Normalized dot products.
        """
        return da.einsum(
            "ik,mk->im", experimental, dictionary, optimize=True, dtype=self.dtype
        )

    def _mask_patterns(self, patterns: da.Array | np.ndarray) -> da.Array | np.ndarray:
        with dask.config.set(**{"array.slicing.split_large_chunks": False}):
            patterns = patterns[:, ~self.signal_mask.ravel()]
        return patterns

    @staticmethod
    def _normalize_patterns(patterns: da.Array | np.ndarray) -> da.Array | np.ndarray:
        if isinstance(patterns, da.Array):
            dispatcher = da
        else:
            dispatcher = np

        # Normalize
        patterns_norm = dispatcher.sqrt(
            dispatcher.sum(dispatcher.square(patterns), axis=1)
        )[..., np.newaxis]
        patterns = patterns / patterns_norm

        return patterns
