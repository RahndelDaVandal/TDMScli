# tdmscli.folder.py
from dataclasses import dataclass, field
from pathlib import Path

from rich.traceback import install

install()


@dataclass
class File:
    path: Path
    name: str = field(init=False)
    size: float = field(init=False)

    def __post_init__(self):
        self.name = self.path.name
        self.size = self.path.stat().st_size

    def __repr__(self) -> str:
        return(f"File(name='{self.name}', size='{self._size_str(self.size)}')")

    def __len__(self) -> int:
        return self.size

    def __eq__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        return self.name < other.name

    def __gt__(self, other) -> bool:
        return self.name > other.name

    def _size_str(self, B: int) -> str:
        B = float(B)
        KB = float(1024)
        MB = float(KB**2)  # 1,048,576
        GB = float(KB**3)  # 1,073,741,824
        TB = float(KB**4)  # 1,099,511,627,776

        if B < KB:
            return "{0} {1}".format(B, "Bytes" if 0 == B > 1 else "Byte")
        elif KB <= B < MB:
            return "{0:.2f} KB".format(B / KB)
        elif MB <= B < GB:
            return "{0:.2f} MB".format(B / MB)
        elif GB <= B < TB:
            return "{0:.2f} GB".format(B / GB)
        elif TB <= B:
            return "{0:.2f} TB".format(B / TB)


@dataclass
class Folder:
    path: Path
    files: list[File] = field(init=False)

    def __post_init__(self):
        self.files = self.get_files()

    def get_files(self) -> list[File]:
        return [File(file) for file in self.path.iterdir()]

    def __repr__(self) -> str:
        string = f"Folder(path=PosixPath('{self.path}'),\n"
        string += "\tfiles=[\n"
        for file in self.files:
            string += f"\t\t{file},\n"
        string += "\t\t]\n\t)"
        return string

    def __len__(self) -> int:
        return len(self.files)


fldr_path = Path(__file__).parent.parent.parent / "tdms-files"

fldr = Folder(fldr_path)
print(fldr)

not_dir = Folder(Path(__file__))
print(not_dir)
