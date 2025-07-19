import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt 
import os 
import sys

# Add project root path so imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.read_in import read_in
from bin.calculate_correlation import relevant_columns

# Pretty labels for axes
pretty_labels = {
    "TMK": "Temperature (°C)",
    "RSK": "Rainfall (mm)",
    "SDK": "Sunshine Duration (h)"
}

def visualize(df, weather, target, output_dir):
    """
    Generate a scatter plot with a regression line for a weather factor vs. voter turnout.

    Parameters
    ----------
    df : pandas.DataFrame
        Data containing the weather factor and turnout.
    weather : str
        Weather column to analyze.
    target : str
        Target column (e.g., voter turnout).
    output_dir : str
        Folder where plots are saved.
    """

    data = df[[weather, target]].dropna()
    if data.empty:
        raise ValueError(f"No usable data available for {weather} and {target}")

    fig, ax = plt.subplots()

    # Scatter plot
    ax.scatter(data[weather], data[target], label="data", alpha=0.6, color="steelblue", edgecolor='black')

    # Regression line
    try:
        coeffs = np.polyfit(data[weather], data[target], 1)
        line = np.poly1d(coeffs)
        x_vals = np.linspace(data[weather].min(), data[weather].max(), 100)
        ax.plot(x_vals, line(x_vals), label="Regression line", linestyle="-", color="darkblue")
    except Exception as e:
        print(f"ERROR: Couldn't generate regression line for {weather}: {e}")

    # Correlation coefficient (r)
    r = np.corrcoef(data[weather], data[target])[0, 1]
    title_weather = pretty_labels.get(weather, weather)
    ax.set_title(f"Correlation between {title_weather} and Turnout (r = {r:.2f})")

    ax.set_xlabel(title_weather)
    ax.set_ylabel("Voter Turnout (%)")
    ax.set_ylim(bottom=70)  # Start y-axis at 70%
    ax.grid(True)
    ax.legend()

    # Save plot with filename
    filename = f"{weather}_and_voter_turnout_pct.png"
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()
    print(f"Saved! You can find the plot here: {os.path.join(output_dir, filename)}")


def main():
    parser = argparse.ArgumentParser(
        description="Create scatter plots with regression lines to visualize the correlation between weather factors and voter turnout."
    )

    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input CSV file with merged weather and election data."
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Directory where the output plots (PNG files) will be saved."
    )

    args = parser.parse_args()

    df = read_in(args.input, sep=",")
    weather = ["TMK", "RSK", "SDK"]
    target = "voter_turnout_pct"

    usable, _ = relevant_columns(df, weather, target)
    for factor in usable:
        visualize(df, factor, target, args.output)


if __name__ == "__main__":
    main()