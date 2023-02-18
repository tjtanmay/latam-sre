import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

from sklearn.ensemble import AdaBoostClassifier

import datetime
import time
from datetime import timedelta

import os
import pickle
import requests
import json
import flask


# Importing the dataset
df = pd.read_csv('datasets/flightdata.csv', parse_dates=[0], infer_datetime_format=True)

# New Column and Format
df['Scheduled DateTime'] = pd.to_datetime(df['Scheduled DateTime'], infer_datetime_format=True)
df['Scheduled Time'] = df['Scheduled DateTime'].dt.strftime('%H:00')
df['Delay? (20 min)'] = np.where(df['Minute Delay'] >= 20, 'Yes', 'No')


traindf = df.drop(['Flight No.', 'Delay Type', 'Minute Delay', 'Month', 'Scheduled Date','Scheduled DateTime', 'Real Departure Time'], axis=1)
traindf = traindf.dropna()
traindf['Origin'] = "Dublin"
traindf.head(3)

# getting airline, weeekday and destination list

list_airlines = traindf.Airline.unique()
list_destination = traindf.Destination.unique()

# weekdays = Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

newtraindf = pd.get_dummies(traindf)

# Split Data
x_data = newtraindf.drop(['Delay? (20 min)_No', 'Delay? (20 min)_Yes'],axis=1)
y_data = newtraindf['Delay? (20 min)_Yes']
x_train, x_test, y_train, y_test = train_test_split(x_data,y_data,test_size=0.26)


adamodel = AdaBoostClassifier()
adamodel.fit(x_train, y_train)

y_pred = adamodel.predict(x_test)

with open('model_v1.pkl', 'wb') as fid:
    pickle.dump(adamodel, fid,2) 

# get dictionary for reference later in form
index_dict = dict(zip(x_data.columns,range(x_data.shape[1])))

with open('x_data', 'wb') as fid:
    pickle.dump(index_dict, fid,2) 