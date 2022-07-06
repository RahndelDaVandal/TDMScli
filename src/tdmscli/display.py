from pathlib import Path
from rich.console import Console
from rich import box
from rich.table import Table
from rich.traceback import install

install()


def strFileSize(B):
    """Return the given bytes as a human friendly KB, MB, GB, or TB string."""
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


def display_files(dir: Path) -> None:
    if not dir.is_dir():
        raise NotADirectoryError

    files = [file for file in dir.iterdir()]
    files.sort()

    table = Table(box=box.ROUNDED)

    table.add_column("NAME", style="blue")
    table.add_column("SIZE", style="green")

    for file in files:
        table.add_row(f"{file.name}", f"{strFileSize(file.stat().st_size)}")

    console = Console()

    console.print(table)
