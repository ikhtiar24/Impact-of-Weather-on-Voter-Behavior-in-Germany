
import pandas as pd
import numpy as np 
import os
import sys
import pytest

# Add path to the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bin.calculate_correlation import relevant_columns



def test_unusable_TMK():
    df1 = pd.DataFrame({
        "TMK": [19, 20, 23, 22, np.nan],
        "target": [60, 63, 62, 70, 62]
    })
    with pytest.raises(ValueError, match="No weather factor had enough values to calculate correlation"):
        relevant_columns(df1, ["TMK"], "target")

def test_usable_RSK():
    df2 = pd.DataFrame({
        "RSK": [1, 2, 4, 3, 5],
        "target": [60, 63, 62, 70, 62]
    })
    usable, unusable = relevant_columns(df2, ["RSK"], "target")
    assert "RSK" in usable
    assert "RSK" not in unusable        

def test_empty_TMK():
    df3 = pd.DataFrame({
        "TMK": [np.nan, np.nan, np.nan, np.nan, np.nan],
        "target": [60, 63, 62, 70, 62]
    })
    with pytest.raises(ValueError, match="No weather factor had enough values to calculate correlation"):
        relevant_columns(df3, ["TMK"], "target")

def test_mixed_factor_categories():
    df4 = pd.DataFrame({
        "RSK": [1, np.nan, 4, np.nan, 5],
        "target": [60, 63, 62, 70, 62],
        "TMK": [19, 20, 23, 22, 24],
    })
    usable, unusable = relevant_columns(df4, ["TMK", "RSK"], "target")
    assert "RSK" in unusable
    assert "TMK" in usable

def test_missing_target():
    df5 = pd.DataFrame({
        "TMK": [19, 20, 23, 22, 25],
        "RSK": [1, 2, 3, 4, 5]
    })
    with pytest.raises(ValueError, match="Target column 'target' is missing"):
        relevant_columns(df5, ["TMK", "RSK"], "target")   

# pytest tests/test_unusable_weather_factors.py


