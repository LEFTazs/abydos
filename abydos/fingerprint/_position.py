# Copyright 2018-2020 by Christopher C. Little.
# This file is part of Abydos.
#
# Abydos is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Abydos is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Abydos. If not, see <http://www.gnu.org/licenses/>.

"""abydos.fingerprint._position.

Cisłak & Grabowski's position fingerprint
"""

from ._fingerprint import MOST_COMMON_LETTERS_CG, _Fingerprint

__all__ = ['Position']


class Position(_Fingerprint):
    """Position Fingerprint.

    Based on the position fingerprint from :cite:`Cislak:2017`.

    .. versionadded:: 0.3.6
    """

    def __init__(
        self, n_bits=16, most_common=MOST_COMMON_LETTERS_CG, bits_per_letter=3
    ):
        """Initialize Count instance.

        Parameters
        ----------
        n_bits : int
            Number of bits in the fingerprint returned
        most_common : list
            The most common tokens in the target language, ordered by frequency


        .. versionadded:: 0.4.0

        """
        super(_Fingerprint, self).__init__()
        self._n_bits = n_bits
        self._most_common = most_common
        self._bits_per_letter = bits_per_letter

    def fingerprint(self, word):
        """Return the position fingerprint.

        Parameters
        ----------
        word : str
            The word to fingerprint

        Returns
        -------
        int
            The position fingerprint

        Examples
        --------
        >>> pf = Position()
        >>> bin(pf.fingerprint('hat'))
        '0b1110100011111111'
        >>> bin(pf.fingerprint('niall'))
        '0b1111110101110010'
        >>> bin(pf.fingerprint('colin'))
        '0b1111111110010111'
        >>> bin(pf.fingerprint('atcg'))
        '0b1110010001111111'
        >>> bin(pf.fingerprint('entreatment'))
        '0b101011111111'


        .. versionadded:: 0.3.0
        .. versionchanged:: 0.3.6
            Encapsulated in class

        """
        n_bits = self._n_bits
        position = {}
        for pos, letter in enumerate(word):
            if letter not in position and letter in self._most_common:
                position[letter] = min(pos, 2 ** self._bits_per_letter - 1)

        fingerprint = 0

        for letter in self._most_common:
            if n_bits:
                fingerprint <<= min(self._bits_per_letter, n_bits)
                if letter in position:
                    fingerprint += min(position[letter], 2 ** n_bits - 1)
                else:
                    fingerprint += min(
                        2 ** self._bits_per_letter - 1, 2 ** n_bits - 1
                    )
                n_bits -= min(self._bits_per_letter, n_bits)
            else:
                break

        for _ in range(n_bits):
            fingerprint <<= 1
            fingerprint += 1

        return fingerprint


if __name__ == '__main__':
    import doctest

    doctest.testmod()
