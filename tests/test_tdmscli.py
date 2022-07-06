import pytest
from tdmscli import __version__
from pathlib import Path
from tdmscli.loader import Loader


def test_version():
    assert __version__ == "0.1.0"


def test_loader_is_created():
    assert Loader() is not None
