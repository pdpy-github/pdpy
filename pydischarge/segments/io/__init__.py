# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2014-2020)
#
# This file is part of pyDischarge.
#
# pyDischarge is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyDischarge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyDischarge.  If not, see <http://www.gnu.org/licenses/>.

"""Input/output routines for the `pydischarge.segments` classes
"""

from . import (  # pylint: disable=unused-import
    ligolw,  # LIGO_LW XML
    segwizard,  # LIGO SegWizard ASCII
    hdf5,  # HDF5
    json,  # segments-web.ligo.org JSON
)

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
