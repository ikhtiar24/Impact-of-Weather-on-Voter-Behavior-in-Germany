import pandas as pd
import argparse
import numpy as np
import matplotlib.pyplot as plt 
import os 
import sys

# Add path to the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.read_in import read_in
from bin.calculate_correlation import relevant_columns


def theoretic_line(ax, x_min, x_max):
    """
    Create a theoretical regression line. 
    
    Parameters
    ----------
    ax: matplotlib.axes.Axes
        Axes object to plot on.

    x_min: float
        the minimum value of current weather factor

    x_max: float 
        the maximum value of current weather factor

    Returns
    -------
    None
        It adds a line to the plot. 

    """


    xpoints = np.array([x_min, x_max])  # range from min to max value of weather factor
    ypoints = np.array([0,100]) # voter turnout from 0-100%
    
    ax.plot(xpoints, ypoints, color = "gray", linestyle = ":", label = "theoretical regression line")


def visualize(df, weather, target, output_dir):
    """
    Plot the correlation between weather factor and voter turnout with a regression line.

    Parameters
    ----------
    df: pandas.DataFrame
        Data Frame containing data about the weather and voter turnout,
    weather: str
        Name of weather factor.
    target: str
        Name of the target column (voter_turnout_pct)
    output_dir: str 
        Path to the direction where the plots are stored.

    Returns
    -------
    None
        PNG files with plotted correlations and regression line are saved. 
    """

    data = df[[weather, target]].dropna()

    fig, ax = plt.subplots()

    # Scattering: for each value one point in the plot
    if data.empty:
        raise ValueError(f"No usable data available for {weather} and {target}")
    ax.scatter(data[weather], data[target], label="data", alpha=0.6)


    # real regression line
    coefficient = np.polyfit(data[weather], data[target], 1)
    line = np.poly1d(coefficient)
    x_vals = np.linspace(data[weather].min(), data[weather].max(), 100)

    # Error Handling for real regression line
    try:
        ax.plot(x_vals, line(x_vals), label="real regession line", linestyle="-")
    except:
        print(f"ERROR: The real regression line couldn't be created for {weather}")

    # Error Handling for theoretical regression line
    try: theoretic_line(ax, data[weather].min(), data[weather].max())
    except:
        print(f"ERROR: The theortical regression line couldn't be created for {weather}")
    
    # labels for the plot
    ax.set_xlabel(weather)
    ax.set_ylabel("Voters Turnout in Percent")
    ax.set_title(f"Correlation: Voters Turnout in Percent and {weather}")
    ax.legend()
    ax.grid(True)

    # safe the PNGs
    filename = f"{weather}_and_{target}.png"
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()
    print(f"Saved! You can find the plot here: {os.path.join(output_dir, filename)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    df = read_in(args.input, sep=",")
    weather = ["TMK", "RSK", "SDK"]
    target = "voter_turnout_pct"

    # for each usable weather one visualization
    usable, _ = relevant_columns(df, weather, target)
    for factor in usable:
        visualize(df, factor, target, args.output)


if __name__ == "__main__":
    main()