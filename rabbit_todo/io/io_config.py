"""
I/O Configuration file.
"""
from __future__ import annotations

# --- Standard Library ---
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from enum import auto
from pathlib import Path


class FileType(Enum):
    JSON = auto()


class File:
    name: str
    type: FileType
    default_content: str = ""


@dataclass
class Directory:
    name: str
    path: Path
    children_dir: list[Directory] = field(default_factory=list)
    children_files: list[File] = field(default_factory=list)
