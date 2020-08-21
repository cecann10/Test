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
Sentiment of individual speeches is very situational-dependent. e.g. the tone of an Inaguaral Address vs. a speech regarding a treaty with Native Americans both given by the same President can be executed with different tones (sad/negative to happy/positive) and subjectivity (opinons vs. facts).

That being said, *average* sentiment of Presidents does show variation by person, while not significantly by political party.

#### Topics:

Using and LDA model, topic categories were created for the speeches. The topic category titles and words with their weights that make up that topic are:
- **Law, constitution, and rights**: 0.018*"law" + 0.015*"constitution" + 0.015*"right" + 0.013*"question" + 0.010*"congress" + 0.009*"house" + 0.008*"election" + 0.008*"slavery" + 0.008*"act" + 0.007*"union"

- **World peace with war & force**: 0.014*"world" + 0.013*"peace" + 0.009*"vietnam" + 0.009*"american" + 0.009*"soviet" + 0.009*"war" + 0.007*"force" + 0.007*"new" + 0.006*"military" + 0.006*"security"

- **War with American freedom**: 0.019*"world" + 0.016*"war" + 0.013*"american" + 0.012*"peace" + 0.012*"men" + 0.010*"life" + 0.009*"america" + 0.009*"freedom" + 0.007*"right" + 0.007*"free"

- **Work & business**: 0.009*"law" + 0.008*"congress" + 0.008*"work" + 0.007*"business" + 0.006*"service" + 0.006*"public" + 0.006*"national" + 0.006*"american" + 0.005*"commission" + 0.005*"legislation"

- **American jobs and family help & needs**: 0.017*"american" + 0.013*"america" + 0.010*"new" + 0.009*"job" + 0.009*"work" + 0.007*"tax" + 0.007*"child" + 0.007*"world" + 0.006*"help" + 0.006*"need"


- **Public power & duty**: 0.016*"public" + 0.016*"power" + 0.009*"duty" + 0.009*"bank" + 0.008*"constitution" + 0.007*"congress" + 0.007*"law" + 0.007*"citizen" + 0.006*"union" + 0.006*"present"


- **Laws, treaties, and action**: 0.012*"congress" + 0.008*"law" + 0.008*"treaty" + 0.007*"act" + 0.007*"war" + 0.006*"duty" + 0.006*"citizen" + 0.006*"power" + 0.005*"territory" + 0.005*"public"


Overall, topics of speeches seem to vary more over the years vs by political party.

Topics of speeches seem to carry relationship with state-of-nation
and historical periods may also be the catalyst for a shift in tone for generations. e.g. The era of the New Deal saw the beginning of 'American jobs and family help & needs' speeches and that tone has continued since that period.



#### Sophistication of Words:
Sophistication of words in speeches has trended down over years and really saw a shift in lowering of 'grade level' required to understand words starting around the 1920s.

The 'lowering' around the 1920s could potentially to be more relatable as more people heard the speeches given that the 1920s would have seen the advent of raidos being common in people's homes, but the findings of this project cannot confirm this theory -- it's a consideration for ongoing study.


#### Conclusion:
Shifts in language and topics of speeches seem to vary more by date than by political party.

The lack of distinct difference between political parties of could be due in part to shifts that have occured in political parties over the years that have caused 'flips' on some issues for what party stood for what value, but even in recent years there is no strong line of difference between Republicans and Democrats.

Historical periods -- the state of the nation -- and aging of the nation showing more difference between speeches indicates that the Presidents more or less follow a tone that they feel is needed for that moment in time, and may model after prior Presidents if seen as being effective with the country.



## METHODOLOGICAL INFORMATION

#### Methods used for collection/generation of data:
All data was collected from [Kaggle.com](https://www.kaggle.com/littleotter/united-states-presidential-speeches) where Joseph Lilleberg provided the presidential speech transcritps through September 25, 2019.  Mr. Lilleberg obtained the data by webscrabing the The Miller Center at the University of Virginia's [website](https://millercenter.org/the-presidency/presidential-speeches) that offers the presidential speeches data publicly.

Minimal basic cleaning was required of the text, and when cleaning, no data was changed -- only removed when needed.


#### Methods for modeling:
For topic modeling, an LDA model with genism was utitlized.  Text pre-processing for the model included lemmatization, custom stopwords, and use of CountVectorizer to vectorize words for modeling and other analysis.


## DATA & FILE OVERVIEW
**NOTE ALL JUPYTER NOTEBOOKS WERE CREATED & EXECUTED IN GOOGLE CLOUD**

- **File List**:
    - [EDA, Pre-processing, and Sentiment Analysis](data_and_analysis/potus_speech_eda_sentiment.ipynb) - notebook for pulling in original dataset and then conducting exploratory data analysis, text-preprossing, and sentiment analysis of the speech transcripts.

    - [Topic Model Building & Selection](data_and_analysis/potus_speech_topics.ipynb) - notebook for testing topic-generating models for identifying topic categories for every presidential speech.  Also assigning historical periods to each speech.

    - [Sophistication of Speech](data_and_analysis/potus_speech_grade_level.ipynb) - notebook for analyzing the text's 'sophistication of speech' (grade level required to understand words in text/speech).  Also where key findings from all notebooks on the speeches is pulled together in a master dataframe to explort for visualization

    - **Final Master Data File** - **Note that this file is not linked because it was removed to meet size requirements for project submission.  If you run the notebooks, this csv file will be created and can be found in the 'csv' folder.** The file is a csv that includes all key data collected through work on this project.  For each speech, it includes:

      - President Name
      - Date of Speech
      - Title of Speech
      - Transcript of Speech
      - Sentiment (Polarity and Subjectivity)
      - Speech Topic Category
      - Sophistication Level of Words

- **Relationship between files**:
    * Files listed above are in order of collection and build from each other, but csvs and pickles have been made so that each file can be pulled independent of the other.  Note most pickles and csvs created in the notebooks have been removed due to size limitations, but the files will appear once running the notebooks.

- **Presentation Deck**:
    * [PDF version](Presentation/Presentation_PDF.zip)
    * [Google Slides version](https://docs.google.com/presentation/d/13ajT7wo3lqLfZNRxJ899g3k6y6apVoLt1-c4uePJu3k/edit?usp=sharing)
    * [PPT version](Presentation/Presentation_PPT.zip)

## SHARING/ACCESS INFORMATION

 - Licenses/restrictions placed on the data: None, open for usage.

 - Links to other publicly accessible locations of the data: The Miller Center at the University of Virginia's [website](https://millercenter.org/the-presidency/presidential-speeches)

 - Was data derived from another source? Yes, [Kaggle.com](https://www.kaggle.com/littleotter/united-states-presidential-speeches)

 - Recommended citation for this dataset:
    - Data Source: The Miller Center at the University of Virginia's [website](https://millercenter.org/the-presidency/presidential-speeches)
    - Data Collection: Joseph Lilleberg collected data and placed on [Kaggle.com](https://www.kaggle.com/littleotter/united-states-presidential-speeches) in csv for public use.


## Technologies/Packages Used
  * collections
  * gensim
  * Google Cloud Platform
  * matplotlib
  * nltk
  * Python
  * pandas
  * pickle
  * re
  * scipy
  * seaborn
  * sklearn
  * string
  * Tableau
  * textblob
  * textstat



## Presentation Materials Used
  * Slidesgo - Template
  * freepik - Photos
  * Google Slides
