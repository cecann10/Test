
**Applying Linear Regression to Investigate Relationship Between Cars' Features and Cars' Greenhouse Gases Emissions from their Tailpipe**</br>
This topic was chosen for Metis Data Science Bootcamp Summer 2020 Cohort's Project 2 on Linear Regression.

## GENERAL INFORMATION
Author & Investigator: **[Celina Plaza](https://github.com/cecann10)**

Institution: **Metis**

Email: celina.plaza@gmail.com

Date of data collection: 2020-07-06 through 2020-17-10

## PROJECT OVERVIEW
### Context
The United States Environmental Protection Agency reports that transportation is the largest contributor of the U.S.’s greenhouse gas emissions (gge) -- 28% of total gge.  The model developed for this project intends to help individuals better understand what features of their car can help inform them what may indicate more or less greenhouse gas emissions from the tailpipe of their car.

### Goal
Using a linear regression model, identify features in non-electric cars that have a relationship with the total greenhouse gas emissions from that car's tailpipe and also find to what degree each of those features affect the greenhouse gas emissions total.  

### Findings
XXXX


### Conclusion
XXXX



## METHODOLOGICAL INFORMATION

- **Methods used for collection/generation of data**:
All data was gathered through web-scraping [FuelEconomy.gov](https://www.fueleconomy.gov/) -- specifically the results from the website's ['Find and Compare Cars' - 'Browse by 'Model' tool](https://www.fueleconomy.gov/feg/findacar.shtml). Website is in html.

- **Methods for processing and cleaning the data**:
Functions for web-scraping were developed for relatively 'clean' gathering of data, so minimal effort was needed once data was scraped through the function and all cars' data was pulled together. For minor changes to naming, pandas was used.

- **Methods for analysis and modeling**:
To prepare data for analysis and modeling, dummies were created for categorical data where needed and some features were removed that were known to be irrelevant to finding predicted value of greenhouse gas emissions from tailpipe of car (the 'yp'). Correlations were then evaluated between all features via numerical, heatmap, and graphs.  Using `statsmodels` the parameters were developed in a linear regression model for features to find predicted value of greenhouse gas emissions from tailpipe of car.


## DATA & FILE OVERVIEW

- **File List**:
    * [Web Scraping Functions](data_and_analysis/data/master_functions.py) - functions used for web scraping to obtain information for each car's year-make-model.  ipynb version is [here](data_and_analysis/data/master_functions.ipynb)

    * [Individual Car Data Collection (Mitsubishi example)](data_and_analysis/data/mitsubishi_data.ipynb) - one example of format for how each car's year-make-model was collected through web-scraping.  All cars (25) were then pulled into a [master data file](data_and_analysis/data/all_cars_conjunction_junction_function.ipynb) (also linked below).  All other cars data sets follow format of `[makeofcar]_data.ipynb` for a file name and can be found in [full data and analysis folder](data_and_analysis)

    * [Master data file](data_and_analysis/data/all_cars_conjunction_junction_function.ipynb) - worksheet where all cars' data was pulled together to create master file.  csv of final data set is [here](data_and_analysis/csv/all_cars_df.csv)

    * [Exploratory Data Analysis & Model Development](data_and_analysis/all_cars_gge_model.ipynb) - worksheet where exploratory data analysis and linear regression model was developed, analyzed, and refined

    * [Images of Graphs](data_and_analysis/images) - folder to find all important graphs created during data analysis

- **Relationship between files**:
    * Files listed above are in order of collection and build from each other, but pickles have been made so that each file can be pulled independent of the other.  All pickles can be found in the [`data_and_analysis/pickles` folder](data_and_analysis/data/pickles)

- **Presentation Deck**:
    * [PDF version]()
    * [Google Slides version](https://docs.google.com/presentation/d/1iQDOqwAb18F0br533TtWnW1NMpT9LyKb7002M31rnDw/edit?usp=sharing)
    * [PPT version]()

## SHARING/ACCESS INFORMATION

 - Licenses/restrictions placed on the data: None, open for usage.  Obtained from public government source.

 - Links to other publicly accessible locations of the data: [FuelEconomy.gov](https://www.fueleconomy.gov/)

 - Was data derived from another source? Yes, [FuelEconomy.gov](https://www.fueleconomy.gov/)'s 'Find and Compare Cars tool'

 - Recommended citation for this dataset: [FuelEconomy.gov](https://www.fueleconomy.gov/)


## Technologies Used
  * Jupyter Notebook
  * Python
  * pandas
  * numpy
  * Pickle
  * BeautifulSoup
  * statsmodels
  * seaborn
  * sklearn
  * matplotlib


## Presentation Materials Used
  * Slidesgo - Template
  * freepik - Photos
  * Google Slides
