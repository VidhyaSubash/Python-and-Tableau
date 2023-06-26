# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 12:29:33 2023

@author: BANU MATHI
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# method 1 to read json file
json_file = open('loan_data_json.json')
data = json.load(json_file)

# method 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
    
# transform to dataframe
loandata = pd.DataFrame(data)

# finding unique values
loandata['purpose'].unique()

# describe the data
print(loandata.describe())

print(loandata['int.rate'].describe())
print(loandata['fico'].describe())
print(loandata['dti'].describe())

# using EXP() to get the anual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income


# Working with arrays
# 1D array
arr = np.array([1,2,3,4])

# 0D array
arr = np.array(43)
print(arr)



length = len(loandata)
ficocat = []

for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category>=300 and category<400:
            cat='very poor'
        elif category>=400 and category<600:
            cat='poor'
        elif category>=601 and category<660:
            cat='fair'
        elif category>=660 and category<700:
            cat='good'
        elif category>=700:
            cat='excellent'
        else:
            cat='unknown'
    except:
        cat='unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

# df.loc as conditional statements
# df.loc[df[columnname] condition,newcolumnname]='value if cond is met'

loandata.loc[loandata['int.rate']>0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']<=0.12,'int.rate.type']= 'Low'

# number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='green')
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red',width=0.2)
plt.show()

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint,ypoint)
plt.show()

loandata.to_csv('loan_cleaned.csv',index=True)














