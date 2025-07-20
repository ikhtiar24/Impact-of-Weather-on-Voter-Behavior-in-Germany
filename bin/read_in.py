"""Read CSV file into pandas DataFrame"""

import pandas as pd
import argparse


def read_in(input_file, sep=";"):
    """
    Reads a CSV file and transform it to a pandas DataFrame and treats empty
    strings as NaN.

    Parameters
    ----------
    input_file: str
        Path to CSV file.
    sep: str
        tool to seperate values in the CSV file.

    Returns:
    -------
    pandas.DataFrame
        DataFrame with values from the input_file and empty strings as NaN.

    """
    # read in CSV
    try:
        df = pd.read_csv(input_file, sep=sep, na_values=["", " "])
        df.columns = df.columns.str.strip()
    except pd.errors.EmptyDataError:
        raise ValueError("The file is empty or contains no readable columns.")

    # read_csv() works but the DataFrame is empty
    if df.empty:
        raise ValueError("Error: the data you gave as the input is empty.")

    return df


def main():
    """
    Command-line interface for reading a CSV file into a DataFrame.
    Parses --input argument, reads the CSV, and stores the DataFrame in 'df'.
    """
    parser = argparse.ArgumentParser(description="Read in a CSV file.")
    parser.add_argument(
        "--input",
        required=True,
        help="Path to the input file (CSV)")
    args = parser.parse_args()

    df = read_in(args.input, sep=",")
    return df


if __name__ == "__main__":
    main()
