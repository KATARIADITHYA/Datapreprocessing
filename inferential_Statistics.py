# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:45:29 2022

@author: KATARI ADITHYA
"""


import pandas as pd
import numpy as np
d1=pd.read_excel("D:/Desktop/datasets1/Inferential_Statistics.xlsx")
import matplotlib.pyplot as plt
import numpy as np
plt.hist(d1['Measure X'])
import seaborn as sns
d1.columns
sns.boxplot(d1['Measure X'])
q3=d1['Measure X'].quantile(0.75)
q1=d1['Measure X'].quantile(0.25)
iqr=q3-q1
ll=d1['Measure X'].quantile(0.25)-(1.5*iqr)
ul=d1['Measure X'].quantile(0.75)+(1.5*iqr)
print("----------outlier points-------")
print(d1[d1['Measure X']>ul])
d1['Measure X'].mean()
d1['Measure X'].var()
d1['Measure X'].std()
d1['Measure X'].skew()
