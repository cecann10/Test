# **Measuring Coronavirus Impact on New York City Restaurants with MTA Turnstile Data**

---
This is a topic chosen for Project 1 on Exploratory Data Analysis, for the Metis Data Science Bootcamp - Summer 2020 Cohort.

## Context
Restaurants in NYC have been negatively affected financially by the shelter-in-place mandated by the government since March 2020. The National Restaurant Association wants to prove how much NYC restaurants are struggling due to COVID regulations so that its members can gain more subsidies from the government to stay in business.  The Association has their restaurant’s revenue data but they also need data around foot-traffic so they can point to downward trends in traffic that are similar to downward trends in revenue to better prove their case to the government.

## Goal
Illustrate that NYC restaurants are struggling financially not because of poor business methods, but because the government mandated a quarantine, causing restaurants to lose foot-traffic from commuters, a vital component to NYC businesses.

## Findings
In analyzing total traffic around the top 10 busiest NYC subways stations for the months January through June in 2018, 2019, and 2020 , 2019 and 2018 showed very similar trends, supported with a p-value of 0.64.  Alternatively 2020 compared to 2019 had a p-value of 0.008, indicating there was a strong change in traffic trends in 2020.

When comparing 2020 traffic to prior years, January and February were similar to 2018 & 2019 (slightly higher), but in March 2020 -- during which Governor Cuomo declared a State of Emergency for New York and NYC’s shelter-in-place regulations began -- traffic dropped 55% compared to 2019.  Then **April - June 2020 traffic dropped 92% compared to 2019.** While traffic trends slightly increased April to June 2020, traffic was still 90% below 2019 in June.

The downward trends in traffic align with timing of COVID19 shelter-in-place regulations for NYC as well as reports of trends for revenue loss in the restaurant industry.  Next steps will be to work with the Restaurant Association to gather business revenue data and analyze how significant the correlation is between the foot traffic drops and revenue drops.


## Conclusion
The government quarantine directly causes NYC restaurants to operate at lower business capacity, but also indirectly causes them to lose a significant portion of their customers even if restaurants are open for takeout. In a location with steep costs of operation, where nearby foot-traffic from commuters is a vital component to business, New York City restaurants need greater subsidies to stay alive through the quarantine imposed on them by the government.


# Methodology

## Gathering data:
We focused our analysis on the [New York’s busiest subway stations in 2019](https://new.mta.info/agency/new-york-city-transit/subway-bus-ridership-2019), which the MTA provided in their 2019 ridership summary data

[Weekly turnstile data available from the MTA](http://web.mta.info/developers/turnstile.html) was used to provide subway ridership data from January-June in 2018, 2019, and 2020. Each year’s weekly data was concatenated into 6 month datasets.

## Cleaning data:
* Date and time data was converted to proper date-time format for processing.

* Hourly turnstile data from within each of the 10 stations was aggregated into rows of overall daily station data.

* Daily entries & exits were calculated by subtracting the beginning-of-day entry & exit number from each respective end-of-day number.

* Daily entries & exits exceeding 500,000 were considered unexplained outliers and replaced with mean of the traffic for that day of the week for the year

* Foot-traffic was calculated by summing entry and exit numbers for each station.

## Exploring and modeling data:
Daily station data was grouped by month for a more 1:1 comparison between the observed years.


# Deliverables
* [Full data and analysis](data_and_analysis)
  * [Python module](data_and_analysis/mta_data.py)
  * [Analysis notebook](data_and_analysis/mta_analysis.ipynb)
* Presentation Deck
  * [PDF version](presentation/group2_restaurants_presentation.pptx.zip)
  * [Google Slides version](presentation/d/1WM6FQhq_LA3J4gTEMYL6Mct-FhOKKyryhvghrXLp1vE/edit?usp=sharing)
  * [PPT version](presentation/group2_restaurants_presentation.pptx.zip)

## Team
[Celina Plaza](https://github.com/cecann10)

[Cynthia Wang](https://github.com/cynthiawang315)

[Joseph Grovers](https://github.com/josephgrovers)

## Technologies Used
* Jupyter Notebook
* Python
* Pandas
* Numpy
* Datetime
* Pickle
* Matplotlib
* Google Slides

## Additional Sources
[Restaurant Revenue Change via Wombply](https://www.womply.com/blog/data-dashboard-how-coronavirus-covid-19-is-impacting-local-business-revenue-across-the-u-s/)

## Presentation Materials Used
* Slidesgo - Template
* Flaticon - Icons
* Freepik - Infographics & images
