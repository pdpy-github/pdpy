# -*- coding: utf-8 -*-
# Copyright (C) Duncan Macleod (2018-2020)
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

"""This module provides plotting utilities for visualising GW data

The standard data types (`TimeSeries`, `Table`, `DataQualityFlag`, ...) can
all be easily visualised using the relevant plotting objects, with
many configurable parameters both interactive, and in saving to disk.
"""

import matplotlib

# utilities
from . import (
    rc,  # updated default parameters
    colors,  # extra colors
    gps,  # GPS timing scales and formats
    log,  # Logarithimic scaling mods
    units,  # unit support
)

# figure and axes extensions
from .plot import Plot
from .axes import Axes
from .bode import BodePlot
from .segments import SegmentAxes

from ..utils.env import bool_env

__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"

# load our rcParams as default (without latex unless requested)
if bool_env('PYDISCHARGE_RCPARAMS', True):
    matplotlib.rcParams.update(
        rc.rc_params(usetex=bool_env('PYDISCHARGE_USETEX', False)))
