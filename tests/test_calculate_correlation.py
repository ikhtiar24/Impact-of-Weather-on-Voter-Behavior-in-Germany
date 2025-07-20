import pandas as pd 
import numpy as np

def test_positive_corr():
    """Test positive correlation between weather factor and voter turnout."""
    df1 = pd.DataFrame({
        "TMK": [0,5,10,15,25], 
        "voter_turnout_pct": [70,75,80,85,90]
    })

    corr1 = df1.corr(numeric_only=True)["voter_turnout_pct"]["TMK"]
    assert corr1 > 0

def test_negative_corr():
    """Test negative correlation between weather factor and voter turnout."""
    df2 = pd.DataFrame({
        "TMK": [0,5,10,15,25], 
        "voter_turnout_pct": [90,86,80,75,70]
    })

    corr2 = df2.corr(numeric_only=True)["voter_turnout_pct"]["TMK"]
    assert corr2 < 0

def test_empty_values_corr():
    """Test correlation with empty values in the weather factor and election data."""
    df3 = pd.DataFrame({
        "TMK": [], 
        "voter_turnout_pct": []
    })

    corr_matrix = df3.corr(numeric_only=True)
    assert "TMK" not in corr_matrix.columns or pd.isna(corr_matrix.get("voter_turnout_pct", {}).get("TMK", np.nan))

def test_constant_values_corr():
    """Test correlation with constant values in the weather factor and election data."""
    df4 = pd.DataFrame({
        "TMK": [5, 5, 5, 5, 5],
        "voter_turnout_pct": [70, 70, 70, 70, 70]
    })
    corr4 = df4.corr(numeric_only=True)["voter_turnout_pct"]["TMK"]
    assert pd.isna(corr4) or corr4 == 0


