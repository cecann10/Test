
# COVID-19's Effect On Car Accidents
A Student Project for Metis Data Science Bootcamp Summer 2020.

## GENERAL INFORMATION
Author & Investigator: **[Celina Plaza](https://github.com/cecann10)**

Institution: **Metis**

Email: celina.plaza@gmail.com

Date of data collection: 2020-08-26 through 2020-08-29

## PROJECT OVERVIEW
### Context
On average, the United States has ~36k fatalities per year from vehicle accidents.   There are behavioral actions that are associated with accidents -- e.g. not wearing a seatbelt, speeding, texting, etc -- but there are also external factors, such as weather, temperature, geography, whether at an intersection, that can play a part in propensity for an accident to occur.

With the spread of COVID and cities and states ‘locking down’ across the country, this brings in a new external factor to consider.  While COVID has had countless negative effects on the world, but during the height of stay-at-home orders by states there were reports of less cars on the road leading to cleaner air, clearer views, and more recreation; glimmers of unintended positive impacts.  Could COVID also be associated with fewer and/or less severe accidents?  This project explored that question.



### Goal

Using classification modeling techniques, identify what ‘evergreen’ external factors (geography, weather conditions, traffic signals in the area, etc.) have a relationship with the level of severity of an accident and also examine whether the ‘new’ external factor of the COVID-related lockdown rules slowed traffic in states has a relationship with the severity of an accident.

Additional analysis will be then be done to determine if COVID-related lockdown rules reduced frequency of accidents in general, looking state by state as their rules varied across the nation.

### Approach
To reach this project’s objectives, traffic data on car accidents from February 2016 to June 2020 across the US (~3.5M accidents) was collected and combined data on when states (if ever) implemented ‘stay-at-home’ orders for citizens and then also when they (if yet) reopened the state.

Classification modeling was used to determine if the ‘severity’ of an accident can be predicted with an understanding of the ‘evergreen’ external factors, and then also look at the period of COVID across states to see how it may have affected frequency and/or severity of accidents.


### Findings
Multiple featues were considered for the classifcation modeling:
- Temperature (F)
- Humidity(%)
- Visibility(mi)
- Wind Direction
- Wind Speed
- Weather Condition (e.g. Foggy, Snow, Cloudy)
- Presence of traffic signs/guides (e.g. Traffic Signal, Roundabout, No Exit)
- Time of Day (Day or Night)


Final features of the model were:
- XXX
- XXX
- XXX

A logistic Regression model leveraging oversampling for the 'positive' class (= high blood pressure) was found to be the best option between various classification models considered (Logistic Regression, Random Forest, and Decision Tree).  All models had similiar performance numbers, but the Linear Regression model selected could be a a higher threshold than the others while retaining high recall.  The model's resulting features were also easy to interpret and apply for individuals.

This model's main metric of performance was **Recall**, as it was determined that it was important to catch more people that could have high blood pressure (i.e. lower number False Negatives) vs. looking more to Precision where there would be risk of missing some people that did have high blood pressure (i.e. lower number False Positives).

With scaled data, formula for the model is:

Yp  =  -0.121 + 0.887(x1) + 0.340(x2) + 0.139(x3) + 0.152(x4) - 0.005(x5)

Threshold was set at 0.34, resulting in:

- **Accuarcy score: 0.XX**
- Precision: 0.XX
- Recall: 0.XX
- F1 Score: 0.XX
- ROC AUC Score: 0.XX


### Conclusion
The model demonstrates a relationship between an individual having high blood pressure to their age, weight, race, alcohol consumption, and smoking of cigarettes.

Age is the most significant of indicators of high blood pressure, followed by weight, then race, alcohol consumption, and cigarette smoking.


The model indicates that a person is more likely to have high blood pressure as their age, weight, and alcohol consumption increases.  And also if they currently smoke and idenify as of the race of Non-Hispanic Black.



## METHODOLOGICAL INFORMATION

#### Methods used for collection/generation of data:
- **Car Accident Data**: Car accident data was collected from [Kaggle.com]('https://www.kaggle.com/sobhanmoosavi/us-accidents') and downloaded in a csv format.
- **Stay-At-Home Data by State**: Data regarding when states were in a period of 'stay-at-home' orders was collected by mainly by referencing and cross-referencing [The National Academy for State Health Policy's website]('https://www.nashp.org/governors-prioritize-health-for-all/') and [Littler's website]('https://www.littler.com/publication-press/publication/stay-top-stay-home-list-statewide').  At times 3rd and 4th sources were used to verify a date listed or to find an updated date since stay-at-home orders were shifting often and after some of the main data sources had been published.  A master list of dates for each state was then created and combined with the car accident data based on what state the car accident was listed in.



#### Methods for processing and cleaning the data:
Original data was narrowed to only the variables that were needed for the modeling and/or analysis of COVID's effects.  Samples with null values were removed.

Weather Conditions were bucketed so that over 100 unique values were reduced to 8:
1. Rain/Thunderstorms
2. Snow/Hail
3. Cloudy
4. Foggy/Hazy
5. Dusty
6. Clear/Fair
7. Smoke
8. Wintry Mix


For the classificaion modeling, the target variable, Severity of Car Accident, originally had 4 values (1,2,3,4) that ranked sevrity of the accident.  The 1 and 4 ratings were too minor to use in modeling (1 was below 0.05% and 4 was below 0.3%), so only the 2 and 3 ratings were used in modeling -- therefore the model was a binary classificaion model (2 being majority class and 3 being minority class).


#### Methods for analysis and modeling:
For classification modeling, Logistic Regression, Decision Tree, and Random Forest models were all tested and compared.

'Dummies' were created for categorical data were needed and data was scaled for Logistic Regression modeling.  Common methods were used for address imbalance of the classes (undersampling, ADASYN), but utlimately did not improve the model and were therefore not used.

GridSearch was implmented to optimize parameters for Decision Tree & Random Forest models.  Thresholds were considered to best meet target metric of recall performance without too great of sacrifice to other metrics of precision, F1 score, and accuracy.


## DATA & FILE OVERVIEW
*Note all notebooks were originally run and developed from Google Cloud Platform)*

- **File List**:
    * [Data Collection & EDA](data_and_modeling/car_accidents_eda.ipynb) - worksheet for pulling in all car accident and stay-at-home by state data.  Then data was combined to master document, filtered to key features, and cleaned.

    * [Exploratory Data Analysis & Model Development](data_and_modeling/nhanes_bp_model.ipynb) - worksheet where exploratory data analysis and classification models were explored, developed, analyzed, and refined.

    * [CSVs](data_and_modeling/csv) - the originl csv used for collection of raw data on car accidents

    * [Images](data_and_modeling/images) - images of key graphs made in data collection and modeling process

- **Relationship between files**:
    * Files listed above are in order of collection and build from each other, but pickles have been made so that each file can be pulled independent of the other.  All pickles can be found in the [`data_and_modeling/pickles` folder](data_and_modeling/data/pickles)

- **Presentation Deck**:
    * [PDF version](Presentation/Presentation_PDF.zip)
    * [Google Slides version](XX)
    * [PPT version](Presentation/Presentation_PPT.zip)

## SHARING/ACCESS INFORMATION

 - Licenses/restrictions placed on the data: This car accident dataset has been distributed only for Research purposes, under Creative Commons Attribution-Noncommercial-ShareAlike license (CC BY-NC-SA 4.0). You are not allowed to directly download data from this file; go to [Kaggle.com]('https://www.kaggle.com/sobhanmoosavi/us-accidents') to collect data and follow their usage guidelines.

 - Recommended citation for this dataset:
- Car Accident data:
    - Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, and Rajiv Ramnath. “A Countrywide Traffic Accident Dataset.”, 2019.
    -   Moosavi, Sobhan, Mohammad Hossein Samavatian, Srinivasan Parthasarathy, Radu Teodorescu, and Rajiv Ramnath. "Accident Risk Prediction based on Heterogeneous Sparse Data: New Dataset and Insights." In proceedings of the 27th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems, ACM, 2019.

  - Stay-At-Home by State data:
    - [The National Academy for State Health Policy's "Chart: Each State’s COVID-19 Reopening and Reclosing Plans and Mask Requirements" August 20, 2020]('https://www.nashp.org/governors-prioritize-health-for-all/')
    - [Littler's "Stay on Top of 'Stay At Home' – A List of Statewide Orders" May 20, 2020]('https://www.littler.com/publication-press/publication/stay-top-stay-home-list-statewide')


## Technologies/Packages Used
  * Jupyter Notebook
  * Python
  * pandas
  * numpy
  * imblearn
  * pickle
  * statsmodels
  * seaborn
  * sklearn
  * matplotlib
  * yellowbrick
  * mlxtend


## Presentation Materials Used
  * Slidesgo - Template
  * freepik - Photos
  * Google Slides


*Centers for Disease Control and Prevention, National Center for Health Statistics. Underlying Cause of Death, 1999–2017. CDC WONDER Online Database. Atlanta, GA: Centers for Disease Control and Prevention; 2018. Accessed January 7, 2019.

** Kirkland EB, Heincelman M, Bishu KG, et. al. Trends in healthcare expenditures among US adults with hypertension: national estimates, 2003-2014. J Am Heart Assoc. 2018;7:e008731.
