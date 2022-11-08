# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:48:17 2022

@author: KATARI ADITHYA
"""
import numpy as np
import pandas as pd
d1=pd.read_csv("D:/Desktop/datasets1/OnlineRetail.csv",encoding= 'unicode_escape')
dir(d1)
d1.dtypes

#Q1.TypeCastingconverting float to int
d1.CustomerID=d1.CustomerID.astype('object')
d1.UnitPrice=d1.UnitPrice.astype('object')


#Q2.Finding and removing duplicates.
d2=d1.duplicated()
sum(d2)
d1.drop_duplicates(inplace=True)

#Q3. Do the data analysis (EDA)?
#Such as histogram, boxplot, scatterplot etc

import matplotlib.pyplot as plt
plt.hist(d1.UnitPrice)
import seaborn as sns
sns.boxplot(d1.UnitPrice)
plt.scatter(d1.UnitPrice, d1.UnitPrice)


    
    