import pandas as pd
import sys
import os
import pytest

# Add path to the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.read_in import read_in


def test_read_filled_csv():
    file1 = "data/filled.csv"
    df1 = read_in(file1)
    assert not df1.empty
    assert list(df1.columns) == ["RSK", "TMK", "SDK", "voter_turnout_pct"]


def test_read_empty_csv():
    file2 = "data/empty.csv"
    with pytest.raises(ValueError, match="The file is empty or contains no readable columns."):
        read_in(file2)
       

# pytest tests/test_read_in.py