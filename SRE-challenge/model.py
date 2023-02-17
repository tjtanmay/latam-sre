# Importing the libraries
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import requests
import json
import re
# Importing the dataset
dataset = pd.read_csv('datasets/flightdata.csv')

# Clean and prepare dataset
dataset = dataset[["year","month","day","sched_dep_time","sched_arr_time","carrier","origin","dest","dep_delay","arr_delay"]]
dataset.isnull().sum()

dataset = dataset.fillna({"dep_delay": 1})
dataset = dataset.fillna({"arr_delay": 1})

number = preprocessing.LabelEncoder()
dataset['carrier'] = number.fit_transform(dataset.carrier)
dataset['origin'] = number.fit_transform(dataset.origin)
dataset['dest'] = number.fit_transform(dataset.dest)


# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(dataset.drop('dep_delay', axis=1), dataset['dep_delay'], test_size=0.2)
# Fitting Simple Linear Regression to the Training set
regressor = LogisticRegression(class_weight = 'balanced') 
regressor.fit(X_train, y_train)
# Predicting the Test set results
y_pred = regressor.predict(X_test)
# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))
# Loading model to compare the results