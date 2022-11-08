# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 19:45:12 2022

@author: KATARI ADITHYA
"""
import numpy as np
import pandas as pd
d1=pd.read_csv("D:/Desktop/datasets1/calories_consumed.csv")
d1.columns

#Q-Q Plot
import scipy.stats as stats
import pylab

stats.probplot(d1['Weight gained (grams)'],dist='norm',plot=pylab)#not normal
stats.probplot(d1['Calories Consumed'], dist='norm',plot=pylab)#normal

stats.probplot(np.log(d1['Weight gained (grams)']),dist='norm',plot=pylab)#transformation
