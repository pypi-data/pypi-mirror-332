#  Copyright (C) 2022 ASTRON (Netherlands Institute for Radio Astronomy)
#  SPDX-License-Identifier: Apache-2.0


"""
Contains classes to interact with (hdf5) files
"""

from ._attribute_def import attribute
from ._member_def import member
from ._readers import FileReader
from .hdf._hdf_readers import read_hdf5
from .hdf._hdf_writers import open_hdf5, create_hdf5
from ._writers import FileWriter

__all__ = [
    "FileReader",
    "FileWriter",
    "attribute",
    "member",
    "read_hdf5",
    "open_hdf5",
    "create_hdf5",
]
