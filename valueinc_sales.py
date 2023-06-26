# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 11:18:32 2023

@author: BANU MATHI
"""

# import pandas
import pandas as pd

# read the csv file
data=pd.read_csv('transaction2.csv',sep=';')
data.info()

# Adding columns
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']

data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

data['ProfitPerTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']
data['Markup']=data['ProfitPerTransaction']/data['CostPerTransaction']

# Combining columns
day=data['Day'].astype(str)
year=data['Year'].astype(str)

data['date']=day+'-'+data['Month']+'-'+year
data.iloc[0] # views row with index = 0
data.iloc[0:3] # first 3 rows
data.iloc[-5:] # last 5 rows

data.head(5)
data.iloc[:,2] # all rows second column
data.iloc[4,2] # 4th row, 2nd col

# using split to split the client_keywords field
# new_var = column.str.split('sep',expand=True)

split_col = data['ClientKeywords'].str.split(',',expand=True)

# Creating new columns for the split columns in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

# remove square brackets
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

data['ItemDescription']=data['ItemDescription'].str.lower()

# How to merge files
# bring the new dataset

seasons=pd.read_csv('value_inc_seasons.csv',sep=';')

# merging files: merge_df = pd.merge(df_old,df_new,on='key)

data = pd.merge(data,seasons,on='Month')

# dropping columns (axis=1 => drop a col if=0 => drop a row)
data = data.drop('ClientKeywords',axis=1)
data = data.drop(['Day','Month','Year'],axis=1)

# export into csv

data.to_csv('ValueInc_Cleaned.csv',index=False)










