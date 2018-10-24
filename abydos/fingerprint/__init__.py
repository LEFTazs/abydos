# -*- coding: utf-8 -*-

# Copyright 2014-2018 by Christopher C. Little.
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

"""abydos.fingerprint.

The fingerprint module implements string fingerprints such as:
    - string fingerprint
    - q-gram fingerprint
    - phonetic fingerprint
    - Pollock & Zomora's skeleton key
    - Pollock & Zomora's omission key
    - Cisłak & Grabowski's occurrence fingerprint
    - Cisłak & Grabowski's occurrence halved fingerprint
    - Cisłak & Grabowski's count fingerprint
    - Cisłak & Grabowski's position fingerprint
    - Synoname Toolcode
"""

from __future__ import unicode_literals

__all__ = ['basic', 'lightweight', 'speedcop', 'synoname']


if __name__ == '__main__':
    import doctest

    doctest.testmod()
