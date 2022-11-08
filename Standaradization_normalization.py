# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 15:03:30 2022

@author: KATARI ADITHYA
"""

import numpy as np
import pandas as pd
d1=pd.read_csv("D:/Desktop/datasets1/Seeds_data.csv",encoding= 'unicode_escape')

#Stadarlization 

def stnd(i):
    x=(i-i.mean())/i.std()
    return x

d2=stnd(d1)

#Normalization

def norm(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

d3=norm(d1)
