#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# In[19]:


def make_model_df(url):
    '''
    make_car should be a string
    
    model_rank should be number in a string, 
    unique for each model
    
    url should be a string
    '''
    results = requests.get(url)
    page = results.text

    soup = BeautifulSoup(page, "html5lib")

    #initiate data storage
    years = []
    makes = []
    models = []
    vol_caps = []
    cylinders = []
    transmissions = []
    powers = []
    gges =[]
    mpgs = []


    for element in soup.find_all('td', colspan="8"):

        #year
        for element_car in element.find_all('a'):
            year = element_car.text.split()[0]
            years.append(int(year))

        #make
        for element_car in element.find_all('a'):
            make = element_car.text.split()[1]
            makes.append(make)
        
        #model NOTE THESE WILL NEED TO BE CLEANED IF MAKE HAD TWO WORDS
        for element_car in element.find_all('a'):
            model = ' '.join(element_car.text.split()[2:])
            models.append(model)

        # car combined volume capacity (vol_cap)
        for element_description in element.find_all('span', class_="config"):
            vol_cap = element_description.text.split(',')[0]
            vol_caps.append(vol_cap)
            
        # cylinders
        for element_description in element.find_all('span', class_="config"):
            cylinder = element_description.text.split(',')[1]
            cylinders.append(cylinder)
            
        # transmission
        for element_description in element.find_all('span', class_="config"):
            transmission = (element_description.text.split(',')[2]).split(' ')[1]
            transmissions.append(transmission)
            
        # power/fuel source
        for element_description in element.find_all('span', class_="config"):
            power = element_description.text.split(',')[-1]
            powers.append(power)
    
    
    #greenhouse gas emissions (tailpipe)
    for element_description in soup.find_all('div', class_="ghg-score"):
        gge = element_description.text
        gges.append(gge)
            
    # CAR MPG
    for element_mpg in soup.find_all('td', class_="mpg-comb"):
        mpg = element_mpg.text
        mpgs.append(int(mpg))


    #full dataframe        
    cars = pd.DataFrame({
    'year': years,
    'make': makes,
    'model': models,
    'vol_caps': vol_caps,
    'cylinders': cylinders,
    'transmission': transmissions,
    'power': powers,
    'gge': gges,
    'mpg': mpgs,
    })
    
    return cars


# In[20]:


def get_car_urls(make, models_list):
    '''
    Inputs: ([make], [list of models for make of car])
    Output: List of urls for all models under make inputted.
    '''
    url = "https://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&path=1&year1=1984&year2=2021&make={}&baseModel={}&srchtyp=ymm"
    urls = []
    for model in models_list:
        file_url = url.format(make, model)
        urls.append(file_url)
    return urls

