import re
import numpy as np
import pandas as pd
from scipy.stats import normaltest
import csv

alpha = 1e-3


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
        
def fix_missed_honorifics(train, missed,cleaned_names):
    for vals in missed:
        to_scan = train.iloc[vals]
        sex = to_scan['Sex']
        pclass = to_scan['Pclass']
        wealth_group = to_scan['Class']
        most_common_title = train[train['Sex'] == sex][train['Pclass'] == pclass][train['Class'] == wealth_group].title.mode()[0]
        print('Giving name ', cleaned_names[vals], 'title of ', most_common_title)
        train.loc[missed, 'title'] = most_common_title
    train = train.fillna(0)
    return train



def append_honorifics(train):
    cleaned_names = clean_names(train)
    #to_add = check_for_missing_honorifics(cleaned_names, honorifics)
    #honorifics = honorifics + to_add
    #check_for_missing_honorifics(cleaned_names, honorifics)
    honorifics = list(pd.read_csv('files/honorifics.csv').columns)
    train['title'] = 0
    try:
        columns_to_use = pd.read_csv('files/honorifics_used.csv')
        print('Found honorifics file')
        columns_to_use = list(columns_to_use.columns)
        for cols in columns_to_use:
            train[cols] = 0
        for index, name in zip(train.index, cleaned_names):
            for words in name.split(" "):
                if words in columns_to_use:
                    train.loc[index, words] = 1
                    train.loc[index, 'title'] = words
    except FileNotFoundError:
        print('Need to make new honorifics file...')
        honorifics_used = []
        for index, name in zip(train.index, cleaned_names):
            for words in name.split(" "):
                if words in honorifics:
                    train.loc[index, words] = 1
                    train.loc[index, 'title'] = words
                    honorifics_used.append(words)
        honorifics_used = list(set(honorifics_used))
        with open('files/honorifics_used.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(honorifics_used)

    missed = check_for_missing_honorifics(cleaned_names, honorifics)
    train = fix_missed_honorifics(train, missed, cleaned_names)
    return train

