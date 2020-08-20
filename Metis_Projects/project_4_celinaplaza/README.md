# An Analysis of United States Presidential Speeches Over the Ages
Using natural language processing to analyze sentiments, topics, and sophistication of US presidential speeches -- finding commonalities and shifts over time and across parties.

## GENERAL INFORMATION
Author & Investigator: **[Celina Plaza](https://github.com/cecann10)**

Institution: **Metis**

Email: celina.plaza@gmail.com

Date of data collection: 2020-08-08

## PROJECT OVERVIEW
### Context
Since the dawn of the United States democracy with George Washington, presidential speeches have served as both a reflection of the current state of the nation and a call for changes in a direction that the President believes the country should go.

Presidential speeches provide an insight of what the nation’s leaders are thinking and hoping for the nation’s direction in the moment of their speech, and could therefore also be assumed to be what their views are when making decisions, laws, and appointments for the country in that same time period.

US Presidents have great power over the country and this is their moment to tell the country what they intend to do with that power.  Their delivery of that information will affect the public's reception to the message.

From George Washington’s 1789 First Inaugural Address to Jimmy Carter’s 1977 Address to the Nation On Energy to Donald Trump’s 2019 State of the Union, every president to date (year 2020) has representation in the 991 speeches that were analyzed in this project.



### Goal
Through analysis of the presidential speeches using Natural Language Processing techniques and unsupervised learning models, identify themes of messages people hearing from Presidents and examine *how* they hearing that message (e.g. tone, sentiment, sophistication of words in speech)?  Then consider if any shifts observed are related to shifts in time, in parties, or greater global events occuring at time of speech (e.g. war, economic downturn).


### Findings
#### Sentiment:
- XXX

#### Topics:
- XXX

#### Sophistication of Words:
- XXX

### Conclusion
XXXX



## METHODOLOGICAL INFORMATION

#### Methods used for collection/generation of data:
All data was collected from [Kaggle.com](https://www.kaggle.com/littleotter/united-states-presidential-speeches) where Joseph Lilleberg provided the presidential speech transcritps through September 25, 2019.  Mr. Lilleberg obtained the data by webscrabing the The Miller Center at the University of Virginia's [website](https://millercenter.org/the-presidency/presidential-speeches) that offers the presidential speeches data publicly.

Very little basic cleaning was required of the text, and when cleaning, no data was changed -- only removed when needed.


#### Methods for analysis and modeling:
For exploratory data analysis (EDA) and text pre-processing,


## DATA & FILE OVERVIEW
**NOTE ALL JUPYTER NOTEBOOKS WERE CREATED & EXECUTED IN GOOGLE CLOUD**

- **File List**:
    * [EDA, Pre-processing, and Sentiment Analysis](<URL>) - worksheet for pulling in original dataset and then conducting exploratory data analysis, text-preprossing, and sentiment analysis of the speech transcripts.

    * [Topic Model Building & Selection](<URL>) - worksheet for testing topic-generating models for identifying topic categories for every presidential speech

    * [Topic Model Building & Selection](<URL>) - worksheet for testing topic-generating models for identifying topic categories for every presidential speech

    * [Final Master Data File](<URL>) - csv that includes all key data collected through work on this project:
      - Sentiment (Polarity and Subjectivity)
      - Speech Topic Category
      - Sophistication Level of Words

- **Relationship between files**:
    * Files listed above are in order of collection and build from each other, but csvs and pickles have been made so that each file can be pulled independent of the other.  All pickles can be found in the [`data_and_modeling/pickle` folder](data_and_modeling/pickle) folder and all csvs can be found in the [`data_and_modeling/csv` folder](data_and_modeling/csv) folder.

- **Presentation Deck**:
    * [PDF version](Presentation/Presentation_PDF.zip)
    * [Google Slides version](https://docs.google.com/presentation/d/13ajT7wo3lqLfZNRxJ899g3k6y6apVoLt1-c4uePJu3k/edit?usp=sharing)
    * [PPT version](Presentation/Presentation_PPT.zip)

## SHARING/ACCESS INFORMATION

 - Licenses/restrictions placed on the data: None, open for usage.

 - Links to other publicly accessible locations of the data: [CDC website](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx)

 - Was data derived from another source? Yes, [Kaggle.com](https://www.kaggle.com/littleotter/united-states-presidential-speeches)

 - Recommended citation for this dataset:
    - Data Source: [CDC's National Health and Nutrition Examination Survey](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx)
    - Data Collection: Joseph Lilleberg collected data and placed on Kaggle.com in csv for public use.


## Technologies/Packages Used
  * collections
  * gensim
  * Google Cloud Platform
  * matplotlib
  * nltk
  * Python
  * pandas
  * Pickle
  * re
  * scipy
  * seaborn
  * sklearn
  * string
  * textblob
  * textstat



## Presentation Materials Used
  * Slidesgo - Template
  * freepik - Photos
  * Google Slides
