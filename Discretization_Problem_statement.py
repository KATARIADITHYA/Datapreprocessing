# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:52:12 2022

@author: KATARI ADITHYA
"""

import pandas as pd
import numpy as np
d1=pd.read_csv("D:/Desktop/datasets1/iris.csv")
d1.dtypes
d2=d1.iloc[:,1:5]
#finding min and maximum of each columns
for i in d2.columns:
    print(d2[i].min(),d2[i].max())
    
#diving into three parts by bins=3 and categorise as"low","medium","high"
for i in d2.columns:
    d1[i]=pd.cut(d2[i],3,labels=['l','m','h'])
    
    
for i in d2.columns:
    print('column='+i)
    print(d1[i].value_counts())
d1.dtypes

    