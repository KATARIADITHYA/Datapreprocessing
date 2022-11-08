# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:05:18 2022

@author: KATARI ADITHYA
"""
#Reading the data
import numpy as np
import pandas as pd
d1=pd.read_csv("D:/Desktop/datasets1/boston_data.csv",encoding= 'unicode_escape')
dir(d1)
d1.dtypes

#['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad',
#       'tax', 'ptratio', 'black', 'lstat', 'medv'], dtype=object)
#box plots for all columns

import seaborn as sns
sns.boxplot(data=d1[['crim', 'zn', 'indus']])
sns.boxplot(data=d1[['chas', 'nox']])
sns.boxplot(data=d1[['rm', 'age', 'dis']])
sns.boxplot(data=d1[['rad','tax', 'ptratio', 'black']])
sns.boxplot(data=d1[['lstat', 'medv']])

#getting columns of d1
d2=np.array(d1.columns)

#adding the structure of d2 to d3
d3=pd.DataFrame(columns=d2)

#Finding IQR and replacing the outliers
for i in d2:
    IQR=(d1[i].quantile(0.75))-(d1[i].quantile(0.25))
    ll=d1[i].quantile(0.25)-(1.5*IQR)
    ul=d1[i].quantile(0.75)+(1.5*IQR)
    d3[i]=np.where(d1[i]>ul,ul,np.where(d1[i]<ll,ll,d1[i]))

#dataframe after removing outliers
d3

#comparing dataframes.
d1.describe()
d3.describe()

#reconfirming whether outliers are present or not
sns.boxplot(data=d3)




    
    
