"""Identify and report weather factors excluded from correlation analysis."""

from bin.read_in import read_in
from bin.calculate_correlation import relevant_columns
import pandas as pd
import argparse
import sys
import os

# Add path to the project root
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))


def weather_factor_with_no_corr(factor, output_path):
    """
    Add excluded weather factors to a report file.

    Parameters
    ----------
    factor: str
        Name of weather factor that was excluded.
    output_path: str
        Path to file which reports excluded weather factors.
    """
    with open(output_path, "a") as f:
        f.write(f"The following weather variables {
                factor} were excluded from correlation analysis:\n")
    print(f"Report with excluded weather factors saved to {output_path}")


def main():
    """
    Command-line interface to identify and report unusable weather factors
    that lack sufficient data for correlation analysis.

    Reads a merged dataset, detects weather variables that cannot be used
    for correlation, logs them to a text report, and saves them in a CSV file.
    """
    parser = argparse.ArgumentParser(
        description="Report unusable weather factors.")
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input file (CSV)")
    parser.add_argument(
        "--output",
        required=True,
        help="Path to the output file")
    args = parser.parse_args()

    df = read_in(args.input, sep=",")
    weather = ["TMK", "RSK", "SDK"]
    target = "voter_turnout_pct"

    _, unusable = relevant_columns(df, weather, target)

    for factor in unusable:
        weather_factor_with_no_corr(factor, args.output)

    # Save results in CSV file
    result_df = pd.DataFrame(
        unusable, columns=["weather_factors_without_corr_value"])
    result_df.index.name = "weather_variable"
    result_df.to_csv(args.output)

    print(
        f"Weather variables for which no correlation could be calculated saved in {
            args.output}")


if __name__ == "__main__":

    main()
