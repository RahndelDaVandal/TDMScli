from pathlib import Path
from nptdms import TdmsFile
from rich.console import Console
from rich.table import Table
from rich import box
from rich.traceback import install

install()
console = Console()


def humanbytes(B):
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


# tests = [1, 1024, 500000, 1048576, 50000000, 1073741824, 5000000000, 1099511627776, 5000000000000]
# for t in tests: print("{0} == {1}".format(t,humanbytes(t)))


def display_files(dir: Path) -> None:
    if not dir.is_dir():
        raise NotADirectoryError

    files = [file for file in dir.iterdir()]

    table = Table(box=box.ROUNDED)

    table.add_column("NAME", style="bold blue")
    table.add_column("SIZE", style="bold green", justify="right")

    for file in files:
        table.add_row(f"{file.name}", f"{humanbytes(file.stat().st_size)}")

    console = Console()
    console.print(table)


print("\n\n")
for i in range(2):
    print("-" * 126)
print("\n\n")

files_dir = Path(__file__).parent.parent.parent / "tdms-files"
display_files(files_dir)
