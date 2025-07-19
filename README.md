# Impact of Weather on Voter Bahavior in Germany 

## Overview

The project Impact of weather on voter behavior in Germany investigates whether and to what extent the weather has an influence on voting behavior in Germany. For this purpose, the Bundestag election on September 26, 2021 was analyzed using local weather data.

The results of the project are particularly relevant for future elections. They can help election organizers to develop suitable measures to increase voter turnout (stronger promotion of postal voting). 
A higher voter turnout generally leads to more representative election results and can therefore strengthen the population's trust and satisfaction with democratic processes in the long term.

The target group for this work includes election administrators, those responsible for election logistics and political scientists. 

## Table of Contents
- [Research Questions](#research-questions)
- [Hypotheses](#hypotheses)
- [Project Structure](#project-structure)
- [Dataset Overview](#dataset-overview)
- [Requirements](#requirements)
- [Installation](#️-installation)
- [Usage](#usage)
- [Run the Workflow](#run-the-workflow)
- [Interpretation of Results](#interpretation-of-results)
- [Note: DWD Weather Abbreviation](#note-dwd-weather-abbreviation)
- [Contributing](#contributing)
- [Conduct](#conduct)
- [License](#license)
- [Citation](#citation)
- [Contact](#contact-via-gitup)


## Research Questions

Does local weather influence voter turnout in Germany?<br>
Are certain weather variables (e.g. temperature, rain, sunshine) more strongly correlated with turnout?

## Hypotheses:
H1: There is a correlation between the weather and the voter turnout.<br>
H2: Higher rainfall on election day lower the voter turnout.<br>
H3: More sunshine hours has a positive effect on the voter turnout.<br>
H4: Even small lokal variations in temperature influence the voter turnout. 

## Project Structure 
The project is organized as follows:<br>
<pre> 
impact-of-weather-on-voter-turnout<br>
├── venv/                           # Local Python virtual environment<br>
├── bin/                            # Python files containing all code (processing, analysis)<br>
├── data/                           # Weather and election data as csv Files<br>
├── docs/                           # Planing, workflow, requirements.md (functional and non-functional)<br>
├── results/                        # Plots and csv file with correlation values<br>
├── tests/                          # Testing Python Code<br> 
├── workflow                        # Containing Snakefile<br>
├── CITATION.cff<br>
├── CONDUCT.md<br>
├── CONTRIBUTING.md<br>
├── LICENSE<br>
├── README.md                       # Project overview and usage instructions<br>
├── requirements.txt                # Required Python packages<br>
</pre>


## Dataset Overview

We concentrated on two datasets to perform the analysis, and they are as follows:

Election Dataset: The dataset of Bundestag elections based on September 2021, collected from the Germany Atlas. There are 400 rows and 11 columns that contain the territorial code and the name of the territorial unit, such as district name, district ID, voter turnout percentage, etc. Missing values are indicated as -9999.

Source of the data: {https://www.deutschlandatlas.bund.de/DE/Service/Downloads/downloads_node.html}

Local Weather Dataset: Secondly, we gathered the local weather data from the Deutscher Wetterdienst (DWD) website, which provides access to climate data. A variety of climate observation datasets are available on the website. The directory structure within /climate_environment/CDC usually includes subdirectories for several sorts of observations, such as hourly, daily, and monthly. We use daily data, including detailed weather observations obtained on election day (September 26, 2021) in numerous significant German cities. For the analysis, we take seven 7 cities such as Berlin, Dresden, Erfurt, Hamburg, Köln, München, and Stuttgart. 

Source of the data: {https://opendata.dwd.de/climate_environment/CDC/}




## Requirements:

To run this project, the following requirements must be met:

1. Software: 

Python: The programming language used for all analytic scripts (version 3.x recommended).
Snakemake: Workflow management system
Git: For version control and managing the project repository


2. Python Libraries:

numpy: For numeric operations
pandas: For analyzing and manipulating data
matplotlib: For visualizations.
scipy.stats: used for statistical functions
argparse: For handling command-line arguments
Pulp: An optimization library that Snakemake uses internally


3. Hardware:

A typical desktop or laptop computer with enough processing power and RAM to execute Python and Snakemake workflows.

More funcational and non-functional requirements: [requirements.md](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/docs/requirements.md?ref_type=heads)


## ⚙️ Installation:
To use our software, a few things need to be installed as mentioned above.<br>  
This section will guide you through the installation step by step.


## ⚙️ Install Python and Virtual Environment:
MacOS<br>
Linux<br>
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
 

## Usage
Below you will find instructions on how to use our tools, including simple descriptions and copy-paste examples you can run directly in your terminal.

### 1. Read in
Tool t0 read CSV Files and safe them as DataFrames. 

Example:
```bash
>>> python bin/read_in.py --input data/dataset_election.csv 
```

### 2. Merge Data

Tool to combine the voter turnout data with important weather factor data.  
Example:
```bash
>>> python bin/merge_data.py --output data/merged_all.csv
```

### 3. Clean Missing Values 

Tool to transform missing values (-999) to NaN.
Example:

```bash
>>> python bin/clean_missing.py --input data/merged_all.csv --output data/cleaned_data.csv
```

### 4. Calculate Correlation

Tool to calculate correlations between weather factors and voter turnout.
Example:
```bash 

>>> python bin/calculate_correlation.py --input data/cleaned_data.csv --output results/correlation.csv
``` 

### 5. Visualize Results 

Tool to visualize the correlation between weather factors and voter turnout.
Example:

```bash 
>>> python bin/visualize.py --input data/cleaned_data.csv --output results/plots/
``` 

### 6. Report all Weather Factors with no Correlation Value

Tool to get all weather factors reported for which there was no correlation calculation
Example:
```bash 
>>> python bin/unusable_weather_factors.py --input data/cleaned_data.csv --output results/unusable_weather_factors.csv
```

## Note: DWD weather abbreviation

RSK = Precipitation depth (1 = 1mm = 1l/square meter). <br>
TMK = Temperature in Celcius. <br>
SDK = Hours of Sunshine.


## Run the workflow:

The complete data analysis process was executed using the Snakemake file. Make sure you are in the root directory of the project, which includes bin/, data/, and workflow/.

1. Open the terminal or VS code integrated terminal
2. Activate the Python/Conda environment where Snakemake and all project dependencies are installed such as numpy, pandas, matplotlib, pulp etc.
3. Execute the full workflow use this command line: snakemake --snakefile workflow/Snakefile
4. Execute with multiple CPU cores (for faster processing), use this command line: snakemake --snakefile workflow/Snakefile --cores 4


After successful execution, find the results in the results/ and plots/directories within the project root. 


## Interpretation of Results

We carefully examined how three key factors might interact with voter turnout in several German districts:

Average Temperature(TMK): The plots demonstrate that the data points are grouped around a 75–80% voter turnout proportion. The regression line has little slope, while the average temperature on the X-axis shifts from 18.0 to 19.2. This implies that differences in average temperature within the range had a minimal linear effect on voter turnout, as the turnout percentage remained steady. 

Total Rainfall(RSK): The results are nearly identical to the average temperature; the data points for rainfall are spread out 75-80%. Despite rainfall levels ranging from near 0 to 17.5 units, the regression line remains fairly flat. This suggests that there is weak relationship between election-day rainfall and voter turnout, despite variations in precipitation amounts. 

Sunshine Hours(SDK): The data point observations for sunshine hours likewise show a steady range of roughly 75–80%. Even though the sunshine hours vary from 2.5 to 9, the regression line shows a flat. This describes the weak linear relationship between the sunshine hours and the election day. 


According to the visualization, the important parameters for the German Bundestag Election 2021, such as average temperature, total rainfall, and sunshine hours, are not highly connected with voter turnout. The turnout percentage remained reasonably consistent despite the variations in weather conditions. 



## Contributing
[CONTRIBUTING.md](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/CONTRIBUTING.md?ref_type=heads)

## Conduct
[CONDUCT.md](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/CONDUCT.md?ref_type=heads)


## License
[LICENSE](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/LICENSE?ref_type=heads)

## Citation 
[CITATION.cff](https://gitup.uni-potsdam.de/trendelenb/impact-of-weather-on-voter-behavior-in-germany/-/blob/main/CITATION.cff?ref_type=heads) 

## Contact via GitUP
Annegret Hartmann: @hartmann13 (https://gitup.uni-potsdam.de/hartmann13)<br>
Ikhtiar Ahmed: @ahmed16 (https://gitup.uni-potsdam.de/ahmed16)<br>
Caroline Trendelenburg: @trendelenb (https://gitup.uni-potsdam.de/trendelenb)





