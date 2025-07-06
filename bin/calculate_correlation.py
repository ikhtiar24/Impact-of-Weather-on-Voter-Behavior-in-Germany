import pandas as pd
import argparse
import sys
import os

# Add path to the project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bin.read_in import read_in



def relevant_columns(df, weather_factors, target):
    """
    Filter only useful columns in weather dataset
    
    Parameter
    ---------
    df: DataFrame
        Dataset contains weather and election data.

    weather_factors: list of str 
        List with all weather factor columns. 
    
    target: str
        Column of voter turnout in percent. 

    Returns
    -------
    list of str
        Weather factor column names that are available and usable in the given DataFrame.
    """
    # Warn if any columns are completely empty (only NaNs)
    empty_columns = df.columns[df.isna().all()].tolist()
    if empty_columns:
        print(f"WARNING: the column(s) {empty_columns} is/are empty and will not be calculatedbe ignored")
    

    if target not in df.columns:
        raise ValueError(f"Target column '{target}' is missing in the input file.")

    # only calculate correlation if there are at least 5 values in the weather varibale
    min_value = 5
    usable_weather_col = []
    unusable_weater_col = []
    for weather in weather_factors:
        valid_pair = df[[weather, target]].dropna()
        if len(valid_pair)  < min_value:
            print(f"WARNING: correlation between {weather} and voter turnout couldn't be calculate. To many missing values in {weather}")
            unusable_weater_col.append(weather)
        else:
            usable_weather_col.append(weather)
            print(f"correlation between {weather} and voter turnout could be calculated")    
    
    if len(usable_weather_col) == 0:
        raise ValueError("No weather factor had enough values to calculate correlation")

    return usable_weather_col, unusable_weater_col


def test_corr(df, target, usable):
    """
    Calculate correlations between weather factors and voter turnout.

    Parameters
    ----------
    df: DataFrame
        Data Frame with all important Informations about the weather and voter turnout.
    target: str
        Name of the column representing voter turnout in percent. 
    usable: list of str
        List of all weather factors columns names to calculate correlation with.
    
    Returns:
    -------
    pandas.Series
        Series containing correlations between voter turnout and usable weather factors.
    
    """

    # calculate correlation between voter turnout and each weather factor (only usable weather columns with more than 4 values)
    corr_df = df[[target] + usable].corr(numeric_only=True)
    correlation = corr_df[target].drop(labels=[target])
    return correlation


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    df = read_in(args.input, sep=",")
    weather_factors = ["TMK", "RSK", "SDK"]
    target = "voter_turnout_pct"

    usable, _ = relevant_columns(df, weather_factors, target)

    correlation = test_corr(df, target, usable)

    # export 
    result_df = correlation.to_frame(name="correlation_with_turnout")
    result_df.index.name = "weather_variable"
    result_df.to_csv(args.output)
    print(f"correlation saved in {args.output}")

if __name__ == "__main__":
    main()
    

# source .venv/bin/activate um pandas zu aktivieren