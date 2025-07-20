"""Clean missing weather values (-999) and export cleaned dataset."""

import argparse
import numpy as np
import os
import sys

# Add path to the project root
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..')))

from bin.read_in import read_in


def clean_missing(df, output_file):
    """
    Replace missing values with NaN and saves cleaned data to a CSV file.

    Parameters
    ----------
    df : DataFrame
        DataFrame containing merged weather and election data.
    output_file : str
        Path to the cleaned data CSV file.

    Notes
    -----
    NaN values will appear as empty cells ("") in the saved CSV file.
    """

    # copy merged data
    cleaned_df = df.copy()

    # replace missing values (-999) with NaN if column is present
    for column in ["RSK", "TMK", "SDK"]:
        if column in cleaned_df.columns:
            cleaned_df[column] = cleaned_df[column].replace(-999, np.nan)

    # export cleaned datas
    cleaned_df.to_csv(output_file, index=False)
    print(f"Replaced -999 with NaN. File saved as {output_file}")
    return cleaned_df


def main():
    """
    Command-line interface for cleaning missing values in weather columns.
    Parses --input and --output arguments, reads the input CSV, and writes
    the cleaned result.
    """
    parser = argparse.ArgumentParser(
        description="Clean missing values (-999 → NaN)")
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    args = parser.parse_args()

    df = read_in(args.input, sep=",")
    clean_missing(df, args.output)


if __name__ == "__main__":
    main()
