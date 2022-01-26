import pandas as pd
import numpy as np

def assign_classes(train):
    max_fare = np.max(train['Fare'])
    train['Class'] = 0
    for index, row in train.iterrows():
        fare = row['Fare']
        if fare 