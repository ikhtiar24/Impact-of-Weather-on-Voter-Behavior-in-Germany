# Introduction

The project Impact of weather on voter behavior in Germany investigates whether and to what extent the weather has an influence on voting behavior in Germany. For this purpose, the Bundestag election on September 26, 2021 was analyzed using local weather data.

The results of the project are particularly relevant for future elections. They can help election organizers to develop suitable measures to increase voter turnout (stronger promotion of postal voting). 
A higher voter turnout generally leads to more representative election results and can therefore strengthen the population's trust and satisfaction with democratic processes in the long term.

The target group for this work includes election administrators, those responsible for election logistics and political scientists. 



[CONDUCT.md](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/CONDUCT.md?ref_type=heads)

[CONTRIBUTING.md](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/CONTRIBUTING.md?ref_type=heads)
V
# ⚙️ Installation:
MacOS
Linux
Windows

precondition: Python version 3.10 or newer and pip should be available. 
🔍 proof:

```bash 
# Installation for MacOS/Linux
python3 --version 
pip --version 

# own virtual environment (optional): 
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

```bash 
# Installation for Windows
python --version 
pip --version 

# own virtual environment (optional): 
python -m venv venv
.\venv\Scripts\activate

pip install -r requirements.txt

```
 

# Tools

## 1. Read in
Tool th read in CSV Files and safe them as DataFrames. 

Example:
```bash
>>> python bin/read_in.py --input data/dataset_election.csv 
```

## 2. Merge Data

Tool to combine the voter turnout data with important weather factor data.  
Example:
```bash
>>> python bin/merge_data.py --output data/merged_all.csv
```

## 3. Clean Missing Values 

Tool to transform missing values (-999) to NaN.
Example:

```bash
>>> python bin/clean_missing.py --input data/merged_all.csv --output data/cleaned_data.csv
```

## 4. Calculate Correlation

Tool to calculate correlations between weather factors and voter turnout.
Example:
```bash 

>>> python bin/calculate_correlation.py --input data/cleaned_data.csv --output results/correlation.csv
``` 

## 5. Visualize Results 

Tool to visualize the correlation between weather factors and voter turnout.
Example:

```bash 
>>> python bin/visualize.py --input data/cleaned_data.csv --output results/plots/
``` 

## 6. Report all Weather Factors with no Correlation Value

Tool to get all weather factors reported for which there was no correlation calculation
Example:
```bash 
>>> python bin/unusable_weather_factors.py --input data/cleaned_data.csv --output results/unusable_weather_factors.csv
```

# Note: DWD weather abbreviation

RSK = Precipitation depth (1 = 1mm = 1l/square meter).  
TMK = Temperature in Celcius. 
SDK = Hours of Sunshine.


