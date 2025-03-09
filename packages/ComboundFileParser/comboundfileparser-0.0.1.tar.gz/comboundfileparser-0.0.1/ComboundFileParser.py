#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###################
#    This module implements a Compound file parser (file format used by OLE
#    and base file format for macros, msi, msg, doc, xls...)
#    Copyright (C) 2025  ComboundFileParser

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
###################

"""
This module implements a Compound file parser (file format used by OLE
and base file format for macros, msi, msg, doc, xls...).

Basic example:
>>> c = CompoundFileFromName(filename)
>>> c.parse()
>>> for child in c.get_childs(0, set(), recursive=True):
...     print(child.id, child.parent_name + child.entry.DirectoryEntryName)
...     if child.entry.ObjectType == STREAM_OBJECT:
...         print(c.get_file_content(child))
>>> 

https://fr.wikipedia.org/wiki/Stockage_structur%C3%A9_COM
https://learn.microsoft.com/fr-fr/windows/win32/stg/compound-files
https://learn.microsoft.com/fr-fr/cpp/mfc/containers-compound-files?view=msvc-170

struct CompoundFileHeader {
    uint8_t headerSignature[8];
    uint8_t headerCLSID[16];
    uint16_t minorVersion;
    uint16_t majorVersion;
    uint16_t byteOrder;
    uint16_t sectorShift;
    uint16_t miniSectorShift;
    uint8_t reserved[6];
    uint32_t numDirectorySectors;
    uint32_t numFATSectors;
    uint32_t firstDirectorySectorLocation;
    uint32_t transactionSignatureNumber;
    uint32_t miniStreamCutoffSize;
    uint32_t firstMiniFATSectorLocation;
    uint32_t numMiniFATSectors;
    uint32_t firstDIFATSectorLocation;
    uint32_t numDIFATSectors;
    uint32_t DIFAT[109];
};
"""

__version__ = "0.0.1"
__author__ = "Maurice Lambert"
__author_email__ = "mauricelambert434@gmail.com"
__maintainer__ = "Maurice Lambert"
__maintainer_email__ = "mauricelambert434@gmail.com"
__description__ = """
This module implements a Compound file parser (file format used by OLE
and base file format for macros, msi, msg, doc, xls...)
"""
__url__ = "https://github.com/mauricelambert/ComboundFileParser"

# __all__ = []

__license__ = "GPL-3.0 License"
__copyright__ = """
ComboundFileParser  Copyright (C) 2025  Maurice Lambert
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.
"""
copyright = __copyright__
license = __license__

print(copyright)

from ctypes import (
    c_uint32,
    c_uint16,
    c_uint8,
    Structure,
    pointer,
    sizeof,
    memmove,
    c_wchar,
    c_ushort,
    c_ubyte,
    c_char,
    c_uint64,
)
from typing import TypeVar, List, Tuple, Iterable, Set
from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
from _io import _BufferedIOBase
from os.path import getsize
from io import BytesIO

FREESECT = 0xFFFFFFFF
ENDOFCHAIN = 0xFFFFFFFE
FATSECT = 0xFFFFFFFD
DIFSECT = 0xFFFFFFFC
NOT_APPLICABLE = 0xFFFFFFFC
MAXREGSECT = 0xFFFFFFFA
REGSECT_MIN = 0x00000000
REGSECT_MAX = 0xFFFFFFF9

ROOT_STORAGE_OBJECT = 0x5
STREAM_OBJECT = 0x2
STORAGE_OBJECT = 0x1
UNALLOCATED = 0x0

NOSTREAM = 0xFFFFFFFF

CompoundFileHeader = TypeVar("CompoundFileHeader")
ArrayUInt32 = TypeVar("ArrayUInt32")


def metaclass_factory(bases: Iterable[type]):
    """
    This function makes a new "master type" to resolve conflicts
    between two metaclasses.
    """

    metaclasses = [type(base) for base in bases if isinstance(base, type)]
    print(metaclasses)
    return type("MetaclassUnion", tuple(metaclasses), {})


class CombinedMeta(ABCMeta, type(Structure)):
    """
    This function makes a new "master type" to resolve conflicts
    between two metaclasses.
    """

    def __new__(cls, name, bases, attrs):
        attrs = type(Structure).__new__(cls, name, bases, attrs)
        return ABCMeta.__new__(cls, name, bases, attrs)


# class StructureBuilder(Structure, ABC, metaclass=metaclass_factory((Structure, ABC))):
class StructureBuilder(Structure):
    """
    This class implements a ctypes.Structure with `from_bytes` class
    method to create a new instance easily from bytes.
    """

    @abstractmethod
    def _transform_values(self) -> None:
        raise NotImplementedError("Abstract method definition")

    @abstractmethod
    def _check_values(self) -> None:
        raise NotImplementedError("Abstract method definition")

    @classmethod
    def from_bytes(cls: type, data: bytes) -> CompoundFileHeader:
        """
        This classmethod is a constructor from bytes.
        """

        if len(data) != sizeof(cls):
            raise ValueError("Invalid data length")

        instance = cls()
        memmove(pointer(instance), data, sizeof(cls))

        instance._transform_values()
        instance._check_values()

        return instance


class CompoundFileHeader(StructureBuilder):
    """
    This class implements a C Structure for the Combound File Headers.
    """

    _pack_ = 1
    _fields_ = [
        ("headerSignature", c_uint8 * 8),
        ("headerCLSID", c_uint8 * 16),
        ("minorVersion", c_uint16),
        ("majorVersion", c_uint16),
        ("byteOrder", c_uint16),
        ("sectorShift", c_uint16),
        ("miniSectorShift", c_uint16),
        ("reserved", c_uint8 * 6),
        ("numDirectorySectors", c_uint32),
        ("numFATSectors", c_uint32),
        ("firstDirectorySectorLocation", c_uint32),
        ("transactionSignatureNumber", c_uint32),
        ("miniStreamCutoffSize", c_uint32),
        ("firstMiniFATSectorLocation", c_uint32),
        ("numMiniFATSectors", c_uint32),
        ("firstDIFATSectorLocation", c_uint32),
        ("numDIFATSectors", c_uint32),
        ("DIFAT", c_uint32 * 109),
    ]

    def __init__(self):
        super().__init__()
        self.headerSignature = (c_uint8 * 8)(
            0xD0, 0xCF, 0x11, 0xE0, 0xA1, 0xB1, 0x1A, 0xE1
        )
        self.headerCLSID = (c_uint8 * 16)(*([0] * 16))
        self.minorVersion = 0x003E
        self.majorVersion = 0x0003  # or 0x0004
        self.byteOrder = 0xFFFE
        self.sectorShift = 0x0009  # or 0x000C depending on majorVersion
        self.miniSectorShift = 0x0006
        self.reserved = (c_uint8 * 6)(*([0] * 6))
        self.miniStreamCutoffSize = 0x00001000

    def _transform_values(self) -> None:
        """
        This method changes loaded values to useful values.

        This method do not returns any value, raise a ValueError if
        sector size is incorrect, set the sectors sizes values.
        """

        if self.sectorShift < 7 or self.sectorShift > 20:
            # self.sectorShift = 9
            raise ValueError(
                "Invalid sector shift (should be greater or equal to 7 and"
                f" smaller or equal to 20, but is: {self.sectorShift})"
            )

        self.sector_size = 1 << self.sectorShift

        if self.miniSectorShift < 3 or self.miniSectorShift > self.sectorShift:
            # self.miniSectorShift = 64
            raise ValueError(
                "Invalid mini sector shift (should be greater or equal to 3 "
                f"and smaller or equal to sectorShift ({self.sectorShift}), "
                f"but is: {self.miniSectorShift})"
            )

        self.mini_sector_size = 1 << self.miniSectorShift

        self.sector_structure = c_uint32 * self.sector_size
        self.mini_sector_structure = c_uint32 * self.mini_sector_size

    def _check_values(self) -> None:
        """
        This method checks headers values and raises ValueError when a value
        is incorrect.
        """

        if bytes(self.headerSignature) != b"\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1":
            raise ValueError("Invalid header signature")

        if any(self.headerCLSID):
            raise ValueError("Header CLSID must be all zeroes")

        if self.majorVersion not in (0x0003, 0x0004):
            raise ValueError("Invalid major version")

        if self.minorVersion != 0x003E:
            raise ValueError("Invalid minor version")

        if self.byteOrder != 0xFFFE:
            raise ValueError("Invalid byte order")

        if self.majorVersion == 0x0003 and self.sectorShift != 0x0009:
            raise ValueError("Invalid sector shift for version 3")
        elif self.majorVersion == 0x0004 and self.sectorShift != 0x000C:
            raise ValueError("Invalid sector shift for version 4")

        if self.miniSectorShift != 0x0006:
            raise ValueError("Invalid mini sector shift")

        if any(self.reserved):
            raise ValueError("Reserved bytes must be all zeroes")

        if self.majorVersion == 0x0003 and self.numDirectorySectors != 0:
            raise ValueError(
                "Number of directory sectors must be zero for version 3"
            )

        if self.miniStreamCutoffSize != 0x00001000:
            raise ValueError("Invalid mini stream cutoff size")

        if self.transactionSignatureNumber != 0:
            raise ValueError("Invalid transaction signature number")

        if (
            (
                self.numDIFATSectors == 0
                and self.firstDIFATSectorLocation == FREESECT
            )
            or (
                self.numDIFATSectors == 0
                and self.firstDIFATSectorLocation != ENDOFCHAIN
            )
            or (
                self.numDIFATSectors != 0
                and self.firstDIFATSectorLocation == ENDOFCHAIN
            )
        ):
            raise ValueError(
                "Incorrect number of sector or first sector value"
            )


class DirectoryEntry(StructureBuilder):
    """
    This class implements a C Structure for the Combound File Directory Entry.
    """

    _pack_ = 1
    _fields_ = [
        ("DirectoryEntryName", c_wchar * 32),
        ("DirectoryEntryNameLength", c_ushort),
        ("ObjectType", c_ubyte),
        ("ColorFlag", c_ubyte),
        ("LeftSiblingID", c_uint32),
        ("RightSiblingID", c_uint32),
        ("ChildID", c_uint32),
        ("CLSID", c_char * 16),
        ("StateBits", c_uint32),
        ("CreationTime", c_uint64),
        ("ModifiedTime", c_uint64),
        ("StartingSectorLocation", c_uint32),
        ("StreamSize", c_uint64),
    ]

    def _transform_values(self) -> None:
        """
        This method changes loaded values to useful values.
        """

        self.creation_time = (
            (self.CreationTime / 10000000 - 11644473600)
            if self.CreationTime
            else 0
        )
        self.modification_time = (
            (self.ModifiedTime / 10000000 - 11644473600)
            if self.ModifiedTime
            else 0
        )

    def _check_values(self) -> None:
        """
        This method checks directories entry values and raises ValueError
        when a value is incorrect.
        """

        if (
            ((len(self.DirectoryEntryName) + 1) * 2)
            if self.DirectoryEntryName
            else len(self.DirectoryEntryName)
        ) != self.DirectoryEntryNameLength:
            raise ValueError("Invalid directory entry name length")

        is_unallocated = self.ObjectType == UNALLOCATED
        is_root = self.ObjectType == ROOT_STORAGE_OBJECT
        is_stream = self.ObjectType == STREAM_OBJECT
        is_storage = self.ObjectType == STORAGE_OBJECT

        if is_unallocated:
            if self.DirectoryEntryNameLength != 0:
                raise ValueError("Unallocated directory entry with name")
            if self.StateBits != 0:
                raise ValueError(
                    "Unallocated directory entry with user-defined flags"
                )

        if (
            not is_unallocated
            and not is_root
            and not is_stream
            and not is_storage
        ):
            raise ValueError("Invalid directory entry type")

        if is_root or is_unallocated:
            if (
                self.LeftSiblingID != NOSTREAM
                or self.RightSiblingID != NOSTREAM
            ):
                raise ValueError(
                    "Root or Unallocated directory entry with right or left sibling"
                )

        if is_unallocated or is_stream:
            if self.ChildID != NOSTREAM:
                raise ValueError("Unallocated or Stream with child ID")
            if self.CLSID:
                raise ValueError("Unallocated or Stream with GUID")
            if self.CreationTime != 0 or self.ModifiedTime != 0:
                raise ValueError(
                    "Unallocated or Stream with creation or modified time"
                )

        if is_unallocated or is_storage:
            if self.StartingSectorLocation != 0:
                raise ValueError(
                    "Unallocated or Storage with start sector location"
                )
            if self.StreamSize != 0:
                raise ValueError("Unallocated or Storage with stream size")


@dataclass
class Entry:
    id: int
    entry: DirectoryEntry
    parent_name: str


class CompoundFileHeaderVersion3(Structure):
    """
    This class implements the compound file headers in version 3
    (default for CompoundFileHeader).
    """


class CompoundFileHeaderVersion4(Structure):
    """
    This class implements the compound file headers in version 4.
    """

    def __init__(self):
        super().__init__()
        self.majorVersion = 0x0004
        self.sectorShift = 0x000C


class _CompoundFile(ABC):
    """
    This class implements methods for compound file parsing.
    """

    @abstractmethod
    def read(self, size: int) -> bytes:
        """
        This method should returns `size` next bytes of the file or bytes.
        """

    @abstractmethod
    def seek(self, position: int, mode: int) -> int:
        """
        This method moves to the position relative to `mode`.
        """


class CompoundFile(_CompoundFile):
    """
    This class implements methods for compound file parsing from a binary file.
    """

    def __init__(self, file: _BufferedIOBase):
        self.file = file
        self.size = getattr(self, "size", None)
        self.fat = []
        self.difat = []
        self.minifat = []
        self.fat_sectors = []
        self.difat_sectors = []
        self.minifat_sectors = []
        self.end_of_chain = False
        self.special_values_to_check = []

        if self.size is None:
            self.size = file.seek(0, 2)
            file.seek(0)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> False:
        self.close()
        return False

    def read(self, size: int) -> bytes:
        """
        This method returns `size` next bytes of the binary file.
        """

        return self.file.read(size)

    def seek(self, position: int, mode: int = 0) -> int:
        """
        This method moves to the position relative to `mode`.
        """

        return self.file.seek(position, mode)

    def close(self) -> None:
        """
        This method closes the file.
        """

        return self.file.close()

    def parse(self) -> None:
        """
        This method parses the compound file.
        """

        self.headers = headers = CompoundFileHeader.from_bytes(
            self.read(sizeof(CompoundFileHeader))
        )
        self.maximum_sectors_number = self.size / self.headers.sector_size
        self.sector_type = c_uint32 * (self.headers.sector_size // 4)
        self.follow_sectors(headers.DIFAT, None, True)

        for difat, sector in self.special_values_to_check:
            self.check_specials_values(sector, difat)

        if len(self.difat_sectors) != self.headers.numDIFATSectors:
            raise ValueError(
                "Difference between DIFAT sector number and parsed sectors length"
            )

        if len(self.fat_sectors) != self.headers.numFATSectors:
            raise ValueError(
                "Difference between FAT sector number and parsed sectors length"
            )

        self.process_mini_fat()
        if len(self.minifat_sectors) != self.headers.numMiniFATSectors:
            raise ValueError(
                "Difference between mini FAT sector number and parsed sectors length"
            )

        self.process_directories()
        # if len(self.directories_sectors) != self.headers.numDirectorySectors:
        #     raise ValueError("Difference between directories sector number and parsed sectors length")

    def check_specials_values(self, sector: int, difat: bool = False):
        """
        This methods checks for special values.
        """

        if difat:
            if self.fat[sector] != DIFSECT:
                raise ValueError("Sector should match a DIFAT sector")
        elif self.fat[sector] != FATSECT:
            raise ValueError("Sector should match a FAT sector")

    def follow_sectors(
        self, sectors: List[c_uint32], sector: c_uint32, difat: bool = False
    ) -> None:
        """
        This method loop over sector to find all sectors.
        """

        if sector is not None:
            self.fat_sectors.append(sector)
            self.fat.extend(sectors)
            if sector >= len(self.fat):
                self.special_values_to_check.append((difat, sector))
            else:
                self.check_specials_values(sector, difat)

        last = (len(sectors) - 1) if difat else 0xFFFFFFFF

        for index, fat_sector in enumerate(sectors):
            if fat_sector > REGSECT_MAX:
                if (
                    fat_sector != ENDOFCHAIN
                    and fat_sector != FREESECT
                    and index not in self.fat_sectors
                ):
                    raise ValueError("Invalid FAT sector")
                break
            self.process_sector(fat_sector, last == index)

    def process_sector(self, sector: c_uint32, difat: bool = False) -> None:
        """
        This method parses a FAT sector.
        """

        if sector > self.maximum_sectors_number:
            raise ValueError(
                "Sector size greater than the maximum possible sector"
            )

        if sector in self.fat or sector in self.difat:
            raise RuntimeError("Malicious file: recursive FAT sectors")

        if len(self.difat_sectors) * self.headers.sector_size > 0x6400000:
            raise ValueError("Malicious file: FAT too large")

        if difat:
            self.difat_sectors.append(difat)

        self.difat.append(sector)
        return self.follow_sectors(
            self.load_sector(sector),
            sector,
            difat,
        )

    def read_mini_sector(self, sector: int, size: int) -> bytes:
        """
        This methods reads a mini sector from root entry.
        """

        root_sectors, root = self.parse_get_blocks_list(
            self.directories[0].StartingSectorLocation
        )
        offset = self.headers.mini_sector_size * sector
        return b"".join(root)[offset : offset + size]

    def read_sector(self, sector: int, size: int) -> bytes:
        """
        This methods reads a sector from file.
        """

        self.seek((sector + 1) * self.headers.sector_size)
        return self.read(size)

    def load_sector(self, sector: int) -> ArrayUInt32:
        """
        This methods loads a sector from file.
        """

        return self.sector_type.from_buffer_copy(
            self.read_sector(sector, self.headers.sector_size)
        )

    def process_mini_fat(self) -> None:
        """
        This methods gets mini FAT sectors.
        """

        if (
            self.headers.numMiniFATSectors * self.headers.sector_size
            > 0x6400000
        ):
            raise ValueError("Mini FAT sector too large")

        self.check_block_list(
            "mini FAT",
            self.headers.firstMiniFATSectorLocation,
            self.headers.numMiniFATSectors,
        )
        self.minifat_sectors, minifat = self.parse_get_blocks_list(
            self.headers.firstMiniFATSectorLocation
        )

        for sector in minifat:
            self.minifat.extend(self.sector_type.from_buffer_copy(sector))

    def check_block_list(
        self, check_name: str, first_block: int, sectors_number: int
    ) -> None:
        """
        This methods performs checks on metadata before parsing blocks.
        """

        if sectors_number * self.headers.sector_size > 0x6400000:
            raise ValueError(
                f"{check_name} greater than maximum possible sector"
            )

        if first_block == FREESECT:
            raise ValueError(f"First {check_name} sector is free.")
        elif self.maximum_sectors_number < first_block:
            raise ValueError(f"First {check_name} sector is out of file")

    def parse_get_blocks_list(
        self,
        first_block: int,
        block_list: List[c_uint32] = None,
        size: int = None,
    ) -> Tuple[List[c_uint32], List[c_uint32]]:
        """
        This methods uses the FAT table to retrieve
        a list of sectors to identify data location.
        """

        if block_list is None:
            block_list = self.fat

        if size is None:
            size = self.headers.sector_size

        data = []
        sectors = []
        current_sector = first_block
        while current_sector != ENDOFCHAIN:
            if current_sector in sectors:
                raise RuntimeError("Cyclic mini FAT sector")

            sectors.append(current_sector)
            data.append(self.read_sector(current_sector, size))
            current_sector = block_list[current_sector]

        return sectors, data

    def process_directories(self) -> None:
        """
        This methods is a part of parsing compound file to gets directories.
        """

        self.check_block_list(
            "directory",
            self.headers.firstDirectorySectorLocation,
            self.headers.numDirectorySectors,
        )
        self.directories_sectors, directories = self.parse_get_blocks_list(
            self.headers.firstDirectorySectorLocation
        )
        self.directories = []

        directories = b"".join(directories)
        directory_size = sizeof(DirectoryEntry)
        self.directories = []

        while directories:
            directory = DirectoryEntry.from_bytes(directories[:directory_size])
            directories = directories[directory_size:]
            self.directories.append(directory)

        self.directories_length = len(self.directories)

    def get_file_content(self, entry: Entry):
        """
        This methods returns file content.
        """

        if entry.entry.StreamSize < self.headers.miniStreamCutoffSize:
            if entry.entry.StartingSectorLocation == FREESECT:
                raise ValueError("First file sector is free.")
            return self.read_mini_sector(
                entry.entry.StartingSectorLocation, entry.entry.StreamSize
            )
        else:
            self.check_block_list(
                "file", entry.entry.StartingSectorLocation, 0
            )
            file_sectors, file_content = self.parse_get_blocks_list(
                entry.entry.StartingSectorLocation
            )
            return b"".join(file_content)[: entry.entry.StreamSize]

    def get_door_entries(
        self, index: int, indexes: Set[int], parent_name: str, recursive: bool
    ) -> Iterable[Entry]:
        """
        This methods returns left an right sibling directory entry.
        """

        def get_next(id):
            if id == NOSTREAM:
                return
            if id >= self.directories_length:
                raise ValueError("Invalid sibling ID")
            if id in indexes:
                raise RuntimeError("Recursive directory entries")
            indexes.add(id)
            yield Entry(id, self.directories[id], parent_name)
            if recursive:
                child = self.directories[id]
                if (
                    child.ObjectType == STORAGE_OBJECT
                    or child.ObjectType == ROOT_STORAGE_OBJECT
                ):
                    yield from self.get_childs(id, indexes, parent_name, True)
            yield from self.get_door_entries(
                id, indexes, parent_name, recursive
            )

        next_ = self.directories[index]

        yield from get_next(next_.LeftSiblingID)
        yield from get_next(next_.RightSiblingID)

    def get_childs(
        self,
        index: int,
        indexes: Set[int] = set(),
        parent_name: str = "./",
        recursive: bool = False,
    ) -> Iterable[Entry]:
        """
        This methods yields DirectoryEntries for a directory.
        """

        if index >= self.directories_length:
            raise ValueError("Invalid ID")

        if not index:
            parent_name = "/"

        indexes.add(index)
        current_entry = self.directories[index]

        if (
            current_entry.ObjectType != STORAGE_OBJECT
            and current_entry.ObjectType != ROOT_STORAGE_OBJECT
        ):
            raise ValueError("Not a storage object")

        parent_name += current_entry.DirectoryEntryName + "/"
        child_id = current_entry.ChildID

        if child_id >= self.directories_length:
            raise ValueError("Invalid child ID")

        if child_id in indexes:
            raise RuntimeError("Recursive directory entries")

        child = self.directories[child_id]

        yield Entry(child_id, child, parent_name)
        yield from self.get_door_entries(
            child_id, indexes, parent_name, recursive
        )

        if recursive:
            if (
                child.ObjectType == STORAGE_OBJECT
                or child.ObjectType == ROOT_STORAGE_OBJECT
            ):
                yield from self.get_childs(
                    child_id, indexes, parent_name, True
                )


class CompoundFileFromName(CompoundFile):
    """
    This class implements methods for compound file parsing from a filename.
    """

    def __init__(self, filename: str):
        self.size = getsize(filename)
        file = open(filename, "rb")
        super().__init__(file)


class CompoundFileFromBytes(CompoundFile):
    """
    This class implements methods for compound file parsing from data bytes.
    """

    def __init__(self, data: bytes):
        file = BytesIO(data)
        self.size = len(data)
        super().__init__(file)
