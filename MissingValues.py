# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 23:03:58 2022

@author: KATARI ADITHYA
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
d1=pd.read_csv("D:/Desktop/datasets1/claimants.csv")
d1.isnull().sum()
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
d1=pd.DataFrame(mean_imputer.fit_transform(d1))
d1.isnull().sum()

