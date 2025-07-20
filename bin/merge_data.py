"""Merge weather data from multiple cities with voter turnout data."""

import pandas as pd
import argparse
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


def merging(weather_to_city):
    """
    Merges weather and voter turnout data for one election day of
    multiple cities.

    Parameters
    ----------
    weather_to_city: dict
        Dictionary mapping weather file paths to district names.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing voter turnout and weather data per district
        for given election day.
    """

    election_day = 20210926  # election_day (as integer)
    all_merged = []

    # structure data for each city
    for weather_file, district_name in weather_to_city.items():
        try:
            # reads weather file
            df = read_in(weather_file)

            # missing informations about the date in weather file
            if "MESS_DATUM" not in df.columns:
                print(f"WARNING: no date column in:\n{weather_file}")
                continue

            # only data from the election day
            df = df[df["MESS_DATUM"] == election_day]

            # missing measurement data on election day
            if df.empty:
                print(
                    f"WARNING: no data for election day {weather_file}")
                continue

            # rain, temperature, hours with sun-shine
            df = df[["RSK", "TMK", "SDK"]]
            # city in a column
            df["district_name"] = district_name
            # add to list
            all_merged.append(df)

        except Exception:
            print(f"Warning: Failed to process {weather_file}")

    # exit when data cannot be loaded
    if not all_merged:
        raise Exception("ERROR: weather data could not be loaded")

    # one table with all cities and their weather values on election day
    weather_df = pd.concat(all_merged, ignore_index=True)
    print("weather data loaded and combined")
    print(weather_df)
    # load and merge voter turnout
    election_df = read_in("data/dataset_election.csv", sep=",")

    # warning when district has no election data
    missing_districts = set(
        weather_df["district_name"]) - set(election_df["district_name"])
    if missing_districts:
        print(f"WARNING: missing districts in election data: {district_name}")

    merged = pd.merge(weather_df, election_df, on="district_name")
    return merged


def main():
    """
    Command-line interface for merging weather data with election turnout data.
    Reads weather data for multiple cities, filters for the election day,
    and joins it with voter turnout information. The merged dataset is saved
    as a CSV file to the specified output path.
    """
    parser = argparse.ArgumentParser(
        description="Merge weather data with elecion data.")
    parser.add_argument(
        "--output",
        required=True,
        help="Path to the output file")
    args = parser.parse_args()

    # Mapping: Wetterdatei → district_name
    weather_to_city = {
        "data/dataset_weather_berlin.csv": "Berlin, Stadt",
        "data/dataset_weather_hamburg.csv": "Hamburg, Freie und Hansestadt",
        "data/dataset_weather_köln.csv": "Köln, Stadt",
        "data/dataset_weather_stuttgart.csv": "Stuttgart, Stadtkreis",
        "data/dataset_weather_erfurt.csv": "Erfurt, Stadt",
        "data/dataset_weather_dresden.csv": "Dresden, Stadt",
        "data/dataset_weather_münchen.csv": "München, Landeshauptstadt"
    }
    merged = merging(weather_to_city)

    # create a csv file with prepared data
    merged.to_csv(args.output, index=False)
    print(f"Data successfully exported to file: '{args.output}'")


if __name__ == "__main__":
    main()
