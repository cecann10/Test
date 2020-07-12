
Title of Dataset:
**Applying Linear Regression to Investigate Relationship Between Cars' Features and Cars' Greenhouse Gases Emissions from their Tailpipe**
This topic was chosen for Metis Data Science Bootcamp Summer 2020 Cohort's Project 2 on Linear Regression.

## GENERAL INFORMATION
Author & Investigator: **Celina Plaza**
Institution: **Metis**
Email: celina.plaza@gmail.com

Date of data collection: 2020-07-06 - 2020-07-10



## SHARING/ACCESS INFORMATION

- Licenses/restrictions placed on the data: None, open for usage.  Obtained from public government source.

- Links to other publicly accessible locations of the data: [FuelEconomy.gov](https://www.fueleconomy.gov/)

- Was data derived from another source? Yes, [FuelEconomy.gov](https://www.fueleconomy.gov/)'s 'Find and Compare Cars tool'

- Recommended citation for this dataset: [FuelEconomy.gov](https://www.fueleconomy.gov/)


## METHODOLOGICAL INFORMATION

1. Description of methods used for collection/generation of data:
<Include links or references to publications or other documentation containing experimental design or protocols used in data collection>

2. Methods for processing the data:
<describe how the submitted data were generated from the raw or collected data>

3. Instrument- or software-specific information needed to interpret the data:
<include full name and version of software, and any necessary packages or libraries needed to run scripts>

4. Standards and calibration information, if appropriate:

5. Environmental/experimental conditions:

6. Describe any quality-assurance procedures performed on the data:

7. People involved with sample collection, processing, analysis and/or submission:


## DATA & FILE OVERVIEW

- File List:
  * [Web Scraping Function](data_and_analysis/master_functions.py) - functions used for web scraping to obtain information for each car's year-make-model

  * [Individual Car Data Collection (Mitsubishi example)](data_and_analysis/mitsubishi_data.ipynb) - one example of format for how each car's year-make-model was collected through web-scraping.  All cars (25) were evenutally pulled into the master data set.  All other cars data sets follow format of `[makeofcar]_data.ipynb` for a file name and can be found in [full data and analysis folder](data_and_analysis)

  * [Master data file](/data_and_analysis/all_cars_conjunction_junction_function.ipynb) - worksheet where all cars' data was pulled together to create master file

  * [Exploratory Data Analysis & ](/data_and_analysis/all_cars_gge_model.ipynb) - worksheet where all cars' data was pulled together to create master file

- Presentation Deck
    * [PDF version](presentation/group2_restaurants_presentation.pptx.zip)
    * [Google Slides version](presentation/d/1WM6FQhq_LA3J4gTEMYL6Mct-FhOKKyryhvghrXLp1vE/edit?usp=sharing)
    * [PPT version](presentation/group2_restaurants_presentation.pptx.zip)

 - Relationship between files, if important:

 - Additional related data collected that was not included in the current data package:

- Are there multiple versions of the dataset? yes/no
	A. If yes, name of file(s) that was updated:
		i. Why was the file updated?
		ii. When was the file updated?
