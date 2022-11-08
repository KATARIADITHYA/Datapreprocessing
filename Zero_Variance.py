# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 13:29:03 2022

@author: KATARI ADITHYA
"""

import numpy as np
import pandas as pd
d1=pd.read_csv("D:/Desktop/datasets1/Z_dataset.csv")
d1.columns
#creating a empty list
l=[]
#Only taking numerical columns. Ignoring first column because it is Id coulmn
d1=d1.iloc[:,1:5]

#finding whether the variance of column is zero or not.
for i in d1.columns:
    l.append(d1[i].var()==0)