#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import datetime as dt


# In[5]:


# Function that will do bulk-pull of MTA data for 
# multiple weeks.  Function used in
# get_yearly_data_station_only(), 
# get_yearly_data_fulton(), 
# get_yearly_data_chambers():

def get_data(week_nums):
    '''
    Input: List of dates in format YYMMDD that 
    are ending of MTA raw data files.
    Output: Concatenated datframe of MTA dates
    inputed.
    '''
    url = "http://web.mta.info/developers/data/nyct/turnstile/turnstile_{}.txt"
    dfs = []
    for week_num in week_nums:
        file_url = url.format(week_num)
        dfs.append(pd.read_csv(file_url))
    return pd.concat(dfs)


# In[6]:


# Function used in
# get_yearly_data_station_only(), 
# get_yearly_data_fulton(), 
# get_yearly_data_chambers():

def get_day_entry_counts(row, max_counter):
    '''
    Input: Raw entries for MTA data.
    Output: Daily numbers for entries in MTA data.
    '''
    counter = row["ENTRIES"] - row["PREV_ENTRIES"]
    if counter < 0:
        counter = -counter
    if counter > max_counter:
        counter = min(row["ENTRIES"], row["PREV_ENTRIES"])
    if counter > max_counter:
        return 0
    return counter


# In[7]:


# Function used in
# get_yearly_data_station_only(), 
# get_yearly_data_fulton(), 
# get_yearly_data_chambers():

def get_day_exit_counts(row, max_counter):
    '''
    Input: Raw entries for MTA data.
    Output: Daily numbers for entries in MTA data.
    '''
    counter = row["EXITS"] - row["PREV_EXITS"]
    if counter < 0:
        counter = -counter
    if counter > max_counter:
        counter = min(row["EXITS"], row["PREV_EXITS"])
    if counter > max_counter:
        return 0
    return counter


# In[8]:


# 'Master' function to get data for target stations
# that are not line-dependent


def get_yearly_data_station_only(list_of_weeks):
    '''
    Input: A list of dates that match the end of the 
    MTA raw data files that you want to pull from in the 
    format YYMMDD, such as "200104."
    
    Output: will be a dataframe that lists only data
    for the stations: Times Sq, Grand Central, Lexington,
    34 St. Herald, St.Union, 59 St Columbus, and Penn
    Station.  For those stations will also see:
    1. Date
    2. Daily Entries
    3. Daily Exits
    4. Week Of date
    5. Total Traffic (Entries + Exits)
    '''
    df = get_data(list_of_weeks)
    
    # create df with only stations focusing on
    df_stations = df[(df.STATION == 'TIMES SQ-42 ST')
                     |(df.STATION == 'GRD CNTRL-42 ST')
                     |(df.STATION == 'LEXINGTON AV/53')
                     |(df.STATION == '34 ST-HERALD SQ')
                     |(df.STATION == '14 ST-UNION SQ')
                     |(df.STATION == '59 ST COLUMBUS')
                     |(df.STATION == '34 ST-PENN STA')]


    df_stations.rename(columns={df_stations.columns[10]: 'EXITS'}
                       , inplace=True)

    
    # find first entry for entries and exits
    day_counts_df = df_stations.groupby(['C/A','UNIT','SCP','STATION','DATE']
                                    ,as_index=False)[['ENTRIES','EXITS']].first()
    
    # get the ENTRY daily summary data of each turnstile
    day_counts_df[['PREV_ENTRY_DATE', 'PREV_ENTRIES']] = (day_counts_df
                                                          .groupby(['C/A', 'UNIT', 'SCP', 'STATION'])['DATE', 'ENTRIES']
                                                          .apply(lambda grp: grp.shift(1)))
   
    # get the EXIT daily summary data of each turnstile
    day_counts_df[['PREV_EXIT_DATE', 'PREV_EXITS']] = (day_counts_df
                                                       .groupby(['C/A', 'UNIT', 'SCP', 'STATION'])['DATE', 'EXITS']
                                                       .apply(lambda grp: grp.shift(1)))
    
    
    # drop nan where applicable in new previous date columns for entries & exits
    day_counts_df.dropna(subset=['PREV_ENTRY_DATE'], inplace=True)
    day_counts_df.dropna(subset=['PREV_EXIT_DATE'], inplace=True)
    

    #create new columns for daily entries and daily exits
    day_counts_df["DAILY_ENTRIES"] = (day_counts_df
                                            .apply(get_day_entry_counts, axis=1, max_counter=100_000))
    
    day_counts_df["DAILY_EXITS"] = (day_counts_df
                                    .apply(get_day_exit_counts, axis=1, max_counter=100_000))
    
    
    # set datetime data
    day_counts_df['DATE'] = pd.to_datetime(day_counts_df['DATE'])
    
    
    # get the daily summary data of station
    daily_sum_stations = day_counts_df.groupby(
        ['STATION','DATE'])[['DAILY_ENTRIES','DAILY_EXITS']].sum().reset_index()
    
    # get the fist day of the week & place in new 'WeekOf' column
    daily_sum_stations['weekday'] = daily_sum_stations['DATE'].dt.dayofweek
    daily_sum_stations['WeekOf'] = daily_sum_stations['DATE']
    daily_sum_stations.loc[daily_sum_stations.weekday != 0, 'WeekOf'] = ''
    daily_sum_stations = daily_sum_stations.replace('',np.nan).ffill()
    daily_sum_stations['WeekOf'] = pd.to_datetime(daily_sum_stations['WeekOf']).dt.date
#     daily_sum_stations = daily_sum_stations[daily_sum_stations.WeekOf.notnull()]
    
    # get total Traffic (= entries + exits) & place in new 'TotalTraffic' column
    daily_sum_stations['TotalTraffic'] = (daily_sum_stations['DAILY_ENTRIES'] 
                                          + daily_sum_stations['DAILY_EXITS'])
    
    
    return daily_sum_stations


# In[9]:


def get_yearly_data_fulton(list_of_weeks):
    '''
    Input: A list of dates that match the end of the 
    MTA raw data files that you want to pull from in the 
    format YYMMDD, such as "200104."
    
    Output: will be a dataframe that lists only data
    for the Fulton St's lines: 'ACJZ2345'
    and '2345ACJZ'.  Data for two lines will be 
    combined under Fulton as one.  Will also see:
    1. Date
    2. Daily Entries
    3. Daily Exits
    4. Week Of date
    5. Total Traffic (Entries + Exits)
    '''
    df = get_data(list_of_weeks)
    
    # create df with only stations focusing on
    df_stations = df[(df.STATION == "FULTON ST")]
    # get the lines we need for "FULTON ST"
    df_stations = df_stations[(df_stations.LINENAME == 'ACJZ2345')
                                     |(df_stations.LINENAME == '2345ACJZ')]

    df_stations.rename(columns={df_stations.columns[10]: 'EXITS'}
                       , inplace=True)

    
    # find first entry for entries and exits
    day_counts_df = df_stations.groupby(['C/A','UNIT','SCP','STATION','DATE']
                                    ,as_index=False)[['ENTRIES','EXITS']].first()
    
    # get the ENTRY daily summary data of each turnstile
    day_counts_df[['PREV_ENTRY_DATE', 'PREV_ENTRIES']] = (day_counts_df
                                                          .groupby(['C/A', 'UNIT', 'SCP', 'STATION'])['DATE', 'ENTRIES']
                                                          .apply(lambda grp: grp.shift(1)))
   
    # get the EXIT daily summary data of each turnstile
    day_counts_df[['PREV_EXIT_DATE', 'PREV_EXITS']] = (day_counts_df
                                                       .groupby(['C/A', 'UNIT', 'SCP', 'STATION'])['DATE', 'EXITS']
                                                       .apply(lambda grp: grp.shift(1)))
    
    
    # drop nan where applicable in new previous date columns for entries & exits
    day_counts_df.dropna(subset=['PREV_ENTRY_DATE'], inplace=True)
    day_counts_df.dropna(subset=['PREV_EXIT_DATE'], inplace=True)
    

    #create new columns for daily entries and daily exits
    day_counts_df["DAILY_ENTRIES"] = (day_counts_df
                                            .apply(get_day_entry_counts, axis=1, max_counter=100_000))
    
    day_counts_df["DAILY_EXITS"] = (day_counts_df
                                    .apply(get_day_exit_counts, axis=1, max_counter=100_000))
    
    
    # set datetime data
    day_counts_df['DATE'] = pd.to_datetime(day_counts_df['DATE'])
    
    
    # get the daily summary data of station
    daily_sum_stations = day_counts_df.groupby(
        ['STATION','DATE'])[['DAILY_ENTRIES','DAILY_EXITS']].sum().reset_index()
    
    # get the fist day of the week & place in new 'WeekOf' column
    daily_sum_stations['weekday'] = daily_sum_stations['DATE'].dt.dayofweek
    daily_sum_stations['WeekOf'] = daily_sum_stations['DATE']
    daily_sum_stations.loc[daily_sum_stations.weekday != 0, 'WeekOf'] = ''
    daily_sum_stations = daily_sum_stations.replace('',np.nan).ffill()
    daily_sum_stations['WeekOf'] = pd.to_datetime(daily_sum_stations['WeekOf']).dt.date
    daily_sum_stations = daily_sum_stations[daily_sum_stations.WeekOf.notnull()]
    
    # get total Traffic (= entries + exits) & place in new 'TotalTraffic' column
    daily_sum_stations['TotalTraffic'] = (daily_sum_stations['DAILY_ENTRIES'] 
                                          + daily_sum_stations['DAILY_EXITS'])
    
    
    return daily_sum_stations


# In[10]:


def get_yearly_data_chambers(list_of_weeks):
    '''
    Input: A list of dates that match the end of the 
    MTA raw data files that you want to pull from in the 
    format YYMMDD, such as "200104."
    
    Output: will be a dataframe that lists only data
    for the Chambers' lines: 'JZ456'and 'ACE23'.  Data 
    for two lines will be combined under Chambers as one.  
    Will also see:
    1. Date
    2. Daily Entries
    3. Daily Exits
    4. Week Of date
    5. Total Traffic (Entries + Exits)
    '''
    df = get_data(list_of_weeks)
    
    # create df with only stations focusing on
    df_stations = df[(df.STATION == "CHAMBERS ST")]
    # get the lines we need for "CHAMBERS ST"
    df_stations = df_stations[(df_stations.LINENAME == 'JZ456')
                                     |(df_stations.LINENAME == 'ACE23')]

    df_stations.rename(columns={df_stations.columns[10]: 'EXITS'}
                       , inplace=True)

    
    # find first entry for entries and exits
    day_counts_df = df_stations.groupby(['C/A','UNIT','SCP','STATION','DATE']
                                    ,as_index=False)[['ENTRIES','EXITS']].first()
    
    # get the ENTRY daily summary data of each turnstile
    day_counts_df[['PREV_ENTRY_DATE', 'PREV_ENTRIES']] = (
        day_counts_df
        .groupby(['C/A', 'UNIT', 'SCP', 'STATION'])['DATE', 'ENTRIES']
        .apply(lambda grp: grp.shift(1)))
   
    # get the EXIT daily summary data of each turnstile
    day_counts_df[['PREV_EXIT_DATE', 'PREV_EXITS']] = (
        day_counts_df
        .groupby(['C/A', 'UNIT', 'SCP', 'STATION'])['DATE', 'EXITS']
        .apply(lambda grp: grp.shift(1)))
    
    
    # drop nan where applicable in new previous date columns for entries & exits
    day_counts_df.dropna(subset=['PREV_ENTRY_DATE'], inplace=True)
    day_counts_df.dropna(subset=['PREV_EXIT_DATE'], inplace=True)
    

    #create new columns for daily entries and daily exits
    day_counts_df["DAILY_ENTRIES"] = (
        day_counts_df
        .apply(get_day_entry_counts, axis=1, max_counter=100_000))
    
    day_counts_df["DAILY_EXITS"] = (
        day_counts_df
        .apply(get_day_exit_counts, axis=1, max_counter=100_000))
    
    
    # set datetime data
    day_counts_df['DATE'] = pd.to_datetime(day_counts_df['DATE'])
    
    
    # get the daily summary data of station
    daily_sum_stations = day_counts_df.groupby(
        ['STATION','DATE'])[['DAILY_ENTRIES','DAILY_EXITS']].sum().reset_index()
    
    # get the fist day of the week & place in new 'WeekOf' column
    daily_sum_stations['weekday'] = daily_sum_stations['DATE'].dt.dayofweek
    daily_sum_stations['WeekOf'] = daily_sum_stations['DATE']
    daily_sum_stations.loc[daily_sum_stations.weekday != 0, 'WeekOf'] = ''
    daily_sum_stations = daily_sum_stations.replace('',np.nan).ffill()
    daily_sum_stations['WeekOf'] = pd.to_datetime(daily_sum_stations['WeekOf']).dt.date
    daily_sum_stations = daily_sum_stations[daily_sum_stations.WeekOf.notnull()]
    
    # get total Traffic (= entries + exits) & place in new 'TotalTraffic' column
    daily_sum_stations['TotalTraffic'] = (daily_sum_stations['DAILY_ENTRIES'] 
                                          + daily_sum_stations['DAILY_EXITS'])
    
    
    return daily_sum_stations

