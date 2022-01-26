from scipy.stats import normaltest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alpha = 1e-3

def fill_in_nan_ages(train):
    for index, row in train.iterrows():
        if pd.isnull(row['Age']):
            pclass = row['Pclass']
            sex = row['Sex']
            title = row['title']
            subset_test = train[train['Pclass'] == pclass][train['Sex']==sex][train['title'] == title]['Age']
            #string = 'Hist for ',sex, 'with title ',title, 'and pclass ',pclass
            if np.random.choice(range(0,15)) == 5: # Will randomly show a graph of each population to choose the mean/median from
                subset_test.plot.hist(title = 'Hist for '+sex+' with title '+title+ ' and pclass '+str(pclass))
                plt.show()
            if len(subset_test) >= 8: # normaltest requires at least 8 samples
                results = normaltest(subset_test, nan_policy = 'omit')
                if results[1] > alpha: #null hypothesis cannot be rejected that distribution is normal. Take mean of gaussian
                    age = np.nanmean(subset_test)
                elif results[1] < alpha:
                    age = np.nanmedian(subset_test)
            else:
                print('less than 8 samples')
                mean = np.nanmean(subset_test)
                median = np.nanmedian(subset_test)
                print(mean, median)
                if np.abs((mean-median)/mean)*100 < 10: # Mean and median are close together -- can pick either, will pick mean
                    age = mean
                else: # Pick median -- not close together possibly due to outliers
                    age = median
            print('Changing ',train.loc[index, 'Age'], 'to ', round(age), 'for ', sex, 'with pclass ',pclass,'and title ', title)
            train.loc[index, 'Age'] = round(age)
    return train
            