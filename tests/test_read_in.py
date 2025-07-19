import pandas as pd
import pytest
import os
import sys

# Add path to the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.read_in import read_in


def test_read_filled_csv(tmp_path):
    """Test reading a filled CSV file with expected columns."""
    file_path = tmp_path / "filled.csv"
    pd.DataFrame({
        "RSK": [1.2],
        "TMK": [20.5],
        "SDK": [5.0],
        "voter_turnout_pct": [60.0]
    }).to_csv(file_path, sep=";", index=False)

    df = read_in(str(file_path))
    assert not df.empty
    assert list(df.columns) == ["RSK", "TMK", "SDK", "voter_turnout_pct"]


def test_read_empty_csv(tmp_path):
    """Test reading a CSV file that is completely empty."""
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")  # create truly empty file

    with pytest.raises(ValueError, match="The file is empty or contains no readable columns."):
        read_in(str(file_path))


def test_read_nonexistent_file():
    """Test reading a file that does not exist."""
    with pytest.raises(FileNotFoundError):
        read_in("non_existent_file.csv")


def test_read_csv_with_comma_separator(tmp_path):
    """Test reading a CSV with comma as separator using the sep parameter."""
    file_path = tmp_path / "comma.csv"
    pd.DataFrame({
        "col1": [10],
        "col2": [20]
    }).to_csv(file_path, sep=",", index=False)

    df = read_in(str(file_path), sep=",")
    assert list(df.columns) == ["col1", "col2"]

