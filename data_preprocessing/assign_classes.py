import pandas as pd
import numpy as np
from scipy.stats import percentileofscore

def assign_classes(train):
    train['Class'] = 0
    for index, row in train.iterrows():
        fare = row['Fare']
        if np.isnan(fare):
            pclass = row['Pclass']
            sex = row['Sex']
            fare = np.nanmedian(train[train['Pclass'] == pclass][train['Sex'] == sex]['Fare'])
        percentile = percentileofscore(train['Fare'], fare)
        #print('Fare of ',fare,'has a percentile score of ', percentile)
        if percentile <= 25:
            train.loc[index, 'Class'] = 1
        elif 50 >= percentile > 25:
            train.loc[index, 'Class'] = 2
        elif 75 >= percentile > 50:
            train.loc[index, 'Class'] = 3
        elif percentile > 75:
            train.loc[index, 'Class'] = 4
    return train