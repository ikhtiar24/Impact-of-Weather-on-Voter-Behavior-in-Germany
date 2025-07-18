import pandas as pd
import pytest
import os
import sys

# Add path to the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.visualize import visualize 

def test_plot(tmp_path):
    df = pd.DataFrame({
        "TMK": [20, 22, 25],
        "voter_turnout_pct": [60, 65, 70]
    })

    output_dir = tmp_path
    visualize(df, "TMK", "voter_turnout_pct", output_dir)

    file_path = output_dir / "TMK_and_voter_turnout_pct.png"
    assert os.path.exists(file_path)

def test_empty_data(tmp_path):
    df = pd.DataFrame({
        "TMK": [],
        "voter_turnout_pct": []
    })

    with pytest.raises(ValueError, match="No usable data available"):
        visualize(df, "TMK", "voter_turnout_pct", tmp_path)

