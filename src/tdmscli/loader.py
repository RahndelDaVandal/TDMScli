# tdmscli.loader.py
import pandas as pd
from pathlib import Path
from dataclasses import dataclass, field
from nptdms import TdmsFile

from tdmscli.display import display_files


@dataclass
class Loader:

    def get_channels(self, file_path: Path) -> list[str]:
        if not file_path.is_file():
            raise FileNotFoundError


tdms_dir = Path(__file__).parent.parent.parent / 'tdms-files'
file = tdms_dir / '2022-05-23T12-33-41_Phoenix_.tdms'
csv_path = tdms_dir / "FS2-5.23.22.csv"

with TdmsFile.open(file) as tdms_file:
    df = tdms_file['Formula Server 2'].as_dataframe()
    df.to_csv(csv_path)
    
