from pathlib import Path
from nptdms import TdmsFile
from tdmscli.display import display_files


path = Path(__file__).parent.parent.parent / "tdms-files"

display_files(path)
