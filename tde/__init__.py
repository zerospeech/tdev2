# Copyright 2015-2019 Julien Karadayi
#
# This file is part of WDE: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Phonologizer is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with WDE. If not, see <http://www.gnu.org/licenses/>.
""" Term Discovery Evaluation tool"""
from importlib.metadata import version, PackageNotFoundError

# __version__ = "2.0.2"
try:
    __version__ = version("zerospeech-tde")
except PackageNotFoundError:
    # package is not installed
    __version__ = None
