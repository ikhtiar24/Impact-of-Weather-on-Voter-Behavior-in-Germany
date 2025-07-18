# Introduction

The project Impact of weather on voter behavior in Germany investigates whether and to what extent the weather has an influence on voting behavior in Germany. For this purpose, the Bundestag election on September 26, 2021 was analyzed using local weather data.

The results of the project are particularly relevant for future elections. They can help election organizers to develop suitable measures to increase voter turnout (stronger promotion of postal voting). 
A higher voter turnout generally leads to more representative election results and can therefore strengthen the population's trust and satisfaction with democratic processes in the long term.

The target group for this work includes election administrators, those responsible for election logistics and political scientists. 

# Dataset Overview

We concentrated on two datasets to perform the analysis, and they are as follows:

Election Dataset: The dataset of Bundestag elections based on September 2021, collected from the Germany Atlas. There are 400 rows and 11 columns that contain the territorial code and the name of the territorial unit, such as district name, district ID, voter turnout percentage, etc. Missing values are indicated as -9999.

Source of the data: {https://www.deutschlandatlas.bund.de/DE/Service/Downloads/downloads_node.html}

Local Weather Dataset: Secondly, we gathered the local weather data from the Deutscher Wetterdienst (DWD) website, which provides access to climate data. A variety of climate observation datasets are available on the website. The directory structure within /climate_environment/CDC usually includes subdirectories for several sorts of observations, such as hourly, daily, and monthly. We use daily data, including detailed weather observations obtained on election day (September 26, 2021) in numerous significant German cities. For the analysis, we take seven 7 cities such as Berlin, Dresden, Erfurt, Hamburg, Köln, München, and Stuttgart. 

Source of the data: {https://opendata.dwd.de/climate_environment/CDC/}

# Research Question

Does local weather influence voter turnout in Germany?



# Interpretation of Results

We carefully examined how three key factors might interact with voter turnout in several German districts:

Average Temperature(TMK): The plots demonstrate that the data points are grouped around a 75–80% voter turnout proportion. The regression line has little slope, while the average temperature on the X-axis shifts from 18.0 to 19.2. This implies that differences in average temperature within the range had a minimal linear effect on voter turnout, as the turnout percentage remained steady. 

Total Rainfall(RSK): The results are nearly identical to the average temperature; the data points for rainfall are spread out 75-80%. Despite rainfall levels ranging from near 0 to 17.5 units, the regression line remains fairly flat. This suggests that there is week relationship between election-day rainfall and voter turnout, despite variations in precipitation amounts. 

Sunshine Hours(SDK): The data point observations for sunshine hours likewise show a steady range of roughly 75–80%. Even though the shunshine hours vary from 2.5 to 9, the regression line shows a flat. This describes the weak linear relationship between the sunshine hours and the election day. 


According to the visualization, the important parameters for the German Bundestag Election 2021, such as average temperature, total rainfall, and sunshine hours, are not highly connected with voter turnout. The turnout percentage remained reasonably consistent despite the variations in weather conditions. 


[CONDUCT.md](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/CONDUCT.md?ref_type=heads)

[CONTRIBUTING.md](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/CONTRIBUTING.md?ref_type=heads)

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


