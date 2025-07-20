import pandas as pd
import sys
import os

# Add path to the project root
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))

from bin.clean_missing import clean_missing


def test_replace_missing_values(tmp_path):
    """Test replacing missing values (-999) with NaN in weather data."""

    df1 = pd.DataFrame({
        "RSK": [-999, 1, -999, 2, 3, -999]
    })
    output_file1 = tmp_path / "missing_output1.csv"
    cleaned1 = clean_missing(df1, output_file1)
    assert cleaned1["RSK"].isna().sum() == 3
    assert (cleaned1["RSK"] == -99).sum() == 0


def test_only_missing_values(tmp_path):
    """Test the replacement if one weather data has only missing values."""
    df2 = pd.DataFrame({
        "RSK": [-999, -999, -999, -999]
    })
    output_file2 = tmp_path / "missing_output2.csv"
    cleaned2 = clean_missing(df2, output_file2)
    assert cleaned2["RSK"].isna().sum() == 4
    assert (cleaned2["RSK"] == -99).sum() == 0


def test_no_replace_needed(tmp_path):
    """Test that no replacement occurs if there are no missing values."""
    df3 = pd.DataFrame({
        "RSK": [1, 1, 4, 2, 3, 0]
    })
    output_file3 = tmp_path / "missing_output3.csv"
    cleaned3 = clean_missing(df3, output_file3)
    assert cleaned3["RSK"].isna().sum() == 0
    assert (cleaned3["RSK"] == -99).sum() == 0


def test_no_replace_needed_bc_no_weather_column(tmp_path):
    """Test that no replacement occurs if there is no weather column."""
    df4 = pd.DataFrame({
        "T": [1, 1, 4, 2, 3, 0, -999]
    })
    output_file4 = tmp_path / "missing_output4.csv"
    cleaned4 = clean_missing(df4, output_file4)
    assert cleaned4["T"].isna().sum() == 0
    assert (cleaned4["T"] == -99).sum() == 0


def test_empty(tmp_path):
    """Test that an empty DataFrame is handled correctly."""
    df5 = pd.DataFrame({
        "RSK": []
    })
    output_5 = tmp_path / "missing_output5.csv"
    cleaned5 = clean_missing(df5, output_5)
    assert cleaned5["RSK"].isna().sum() == 0
    assert (cleaned5["RSK"] == -99).sum() == 0
