# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 18:09:57 2025

@author: Shinjini Banerjee
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#reading excelorxlsx file
data=pd.read_excel('articles.xlsx')
data.describe
data.info()

#counting  the number of articles per source
data.groupby(['source_id'])['article_id'].count()
data.groupby(['source_id'])['article_id'].sum()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()
data=data.drop('engagement_comment_plugin_count',axis=1)

#functions in python
def thisfunction():
    print('this_is_my_first_function')
thisfunction()

#with var
def aboutMe(name,surname,location):
    print('This is '+name+' my surname is '+surname+' I am from '+ location)
    return name,surname,location


a=aboutMe('Shinjo','banerjee','kolkata')

#using forloopsin functions
def favfood(food):
    for x in food:
        print('Top food is '+x)

fastfood=['burgers','pizza','pie']
favfood(fastfood)

healthy=['salad','greens','avocado toast']
favfood(healthy) 


#creating a keyword flag
keyword='crash'
keyword_flag=[]
for x in range(0,10):
    heading=data['title'][x]
    if keyword in heading:
        flag=1
    else:
        flag=0
    keyword_flag.append(flag)

def keywordflag(keyword):
    length=len(data)
    keyword_flag=[]
    for x in range(0,length):
        heading=data['title'][x]
        try:
           if keyword in heading:
              flag=1
           else:
              flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag
k=keywordflag('murder')

data['keyword_flag']=pd.Series(k)
data['checking']=k

data=data.drop('checking',axis=1)

sent_int= SentimentIntensityAnalyzer()
text=data['title'][16]
sent=sent_int.polarity_scores(text)

neg=sent['neg']
pos=sent['pos']
neu=sent['neu']


length=len(data)
title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]
for x in range(0,length):
    try:
        text= data['title'][x]
        sent_int= SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)
    
data['title_neg_sentiment']=pd.Series(title_neg_sentiment)
data['title_pos_sentiment']=pd.Series(title_pos_sentiment)
data['title_neu_sentiment']=pd.Series(title_neu_sentiment)

#writing the data

data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata',index=False)
