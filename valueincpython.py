# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:59:58 2024

@author: Shinjini Banerjee
"""

import pandas as pd 

#filename=pd.read_csv('file.csv')or paste a whole path<---format of read csv
data=pd.read_csv('transaction2.csv')
data=pd.read_csv('transaction2.csv',sep=';')
#summary of the data
data.info()
#working with calculations 
#defining variables
CostPerItem=11.73
SellingPricePerItem=21.11
NumberofItemspurchased=6
#math
prf=21.11-11.73
prf=21.11-11.73
prf=SellingPricePerItem-CostPerItem
prfpt=prf*NumberofItemspurchased
cpt=NumberofItemspurchased*CostPerItem
spt=NumberofItemspurchased*SellingPricePerItem

#cpt col
#variable=dataframe[col name]
CostPerItem=data['CostPerItem']
Number=data['NumberOfItemsPurchased']
cpt=CostPerItem*Number

#adding a new col
data['CostPerTransaction']=cpt
#sales per transaction 
data['SalesperTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']
data['profitPerTransaction']=data['SalesperTransaction']-data['CostPerTransaction']
data['markup']=data['profitPerTransaction']/data['CostPerTransaction']
data['markup']=(data['SalesperTransaction']-data['CostPerTransaction'])/data['CostPerTransaction']

#roundinhmarkup



roundmarkup=round(data['markup'],2)
data['markup']=roundmarkup

#combining data fields
my_name='shinjo'+'baner'
my_date=data['Day']+'-'

print(data['Day'].dtype)

#change column type
day=data['Day'].astype(str)
print(day.dtype)
year=data['Year'].astype(str)
print(year.dtype)
my_date=day+'-'+data['Month']+'-'+year
data['date']=my_date

#using iloc toviewcolumnsorrows
data.iloc[0] #views row with index 0
data.iloc[0:3]
data.iloc[-5:]
data.head(5)
data.iloc[:,2]
data.iloc[4,2]

#using split function

#new_variable=column.str.split('sep',expand=True)

split_col=data['ClientKeywords'].str.split(',', expand=True)

#creating new columns forthe split columns 

data['ClientAge']= split_col[0]
data['ClientType']=split_col[1]
data['LengthofContract']=split_col[2]

#using the replace function 

data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthofContract']=data['LengthofContract'].str.replace(']','')

#using the lower function 

data['ItemDescription']=data['ItemDescription'].str.lower()

#merging files or joining files

#bringing in anew data set
seasons=pd.read_csv('value_inc_seasons.csv',sep=';')
#merge.df=pd.merge(old,new,o='key')

data=pd.merge(data, seasons, on='Month')

#dropping orremoving columns

#df.drop('col,axis=1)

data=data.drop('ClientKeywords',axis=1)
data=data.drop('Day',axis=1)
data=data.drop(['Month','Year'],axis=1)

#export into csv 

data.to_csv('ValueInc_Cleaned.csv',index= False)
