import pandas as pd 
import pytest
import os
import sys

# Add path to the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.merge_data import merging 


def test_all_weather_data_empty(tmp_path):
    weather_file = tmp_path / "weather.csv"
    pd.DataFrame(columns=["RSK", "SDK", "TMK", "MESS_DATUM"]).to_csv(weather_file, index=False)

    election_file = tmp_path / "dataset_election.csv"
    pd.DataFrame({"district_name": ["Teststadt"], "turnout": [60.0]}).to_csv(election_file, index=False)

    data_dir = tmp_path / "data"
    data_dir.mkdir()
    election_file.rename(data_dir / "dataset_election.csv")

    with pytest.raises(Exception):
        merging({str(weather_file): "Teststadt"})


def test_missing_MESS_DATUM(tmp_path):
    weather_file = tmp_path / "weather.csv"
    pd.DataFrame({
        "RSK": [1],
        "SDK": [4],
        "TMK": [24]
    }).to_csv(weather_file, index=False)

    election_file = tmp_path / "dataset_election.csv"
    pd.DataFrame({"district_name": ["Teststadt"], "turnout": [60.0]}).to_csv(election_file, index=False)

    data_dir = tmp_path / "data"
    data_dir.mkdir()
    election_file.rename(data_dir / "dataset_election.csv")

    with pytest.raises(Exception, match="weather data could not be loaded"):
        merging({str(weather_file): "Teststadt"})

# pytest tests/test_merge_data.py
