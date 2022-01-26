import pandas as pd
import numpy as np

def handle_nan_embarked(train):
    for index, row in train.iterrows():
        if not isinstance(row['Embarked'], str):
            pclass = row['Pclass']
            sex = row['Sex']
            embarked = train[train['Pclass'] == pclass][train['Sex'] == sex].Embarked.mode()[0]  
            print(embarked) 
            train.loc[index, 'Embarked'] = embarked
    return train     