# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 07:32:56 2023

@author: BANU MATHI
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading excel or xlsx files
data = pd.read_excel('articles.xlsx')

# summary of data
data.describe()

# summary of columns
data.info()

# counting the number of articles per source
# df.groupby(['column_to_group])['column_to_count'].count()
data.groupby(['source_id'])['article_id'].count()

# number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# droping a column
data = data.drop('engagement_comment_plugin_count',axis=1)


def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag=keywordflag('murder')

data['keyword_flag']=pd.Series(keywordflag)

# classes in python

class Car:
    type = 'Automobile' # class attributes
    def __init__(self,name,make,color):
        self.carname = name # instance attributes
        self.carmake = make
        self.carcolor = color
        
mycar = Car('gclass','mercedes','black')
carname = mycar.carname
carmake = mycar.carmake
carcolor = mycar.carcolor

sent_int=SentimentIntensityAnalyzer()
text=data['title'][15]
sent = sent_int.polarity_scores(text)


neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# adding a for loop to extract sentiment per title

title_neg_sen = []
title_pos_sen = []
title_neu_sen = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sen.append(neg)
    title_pos_sen.append(pos)
    title_neu_sen.append(neu)
    
title_neg_sentiment = pd.Series(title_neg_sen)
title_pos_sentiment = pd.Series(title_pos_sen)
title_neu_sentiment = pd.Series(title_neu_sen)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata',index=False)
