import re
import numpy as np
import pandas as pd


def clean_names(dat):
    new_names = []
    for names in dat['Name']:
        to_add = ""
        for splits in names.split(" "):
            to_add += re.sub(r'[^\w]', '', splits) + " "
        new_names.append(to_add[:-1])
    return new_names

def check_for_missing_honorifics(cleaned_names, honorifics):
    misseds = []
    for names in cleaned_names:
        to_look_for_honorific = names.split(" ")
        if all([words not in honorifics for words in to_look_for_honorific]):
            misseds.append(cleaned_names.index(names))
    return misseds
        
def fix_missed_honorifics(train, missed):
    for vals in missed:
        to_scan = train.iloc[vals]
        sex = to_scan['Sex']
        pclass = to_scan['Pclass']
        subset = train[train['Sex'] == sex][train['Pclass'] == pclass]
        print(subset)



def append_honorifics(train):
    cleaned_names = clean_names(train)
    #to_add = check_for_missing_honorifics(cleaned_names, honorifics)
    #honorifics = honorifics + to_add
    #check_for_missing_honorifics(cleaned_names, honorifics)
    honorifics = list(pd.read_csv('files/honorifics.csv').columns)
    train['title'] = 0
    for index, name in zip(train.index, cleaned_names):
        for words in name.split(" "):
            if words in honorifics:
                train.loc[index, words] = 1
                train.loc[index, 'title'] = words
    missed = check_for_missing_honorifics(cleaned_names, honorifics)
    fix_missed_honorifics(train, missed)
    return train, missed

