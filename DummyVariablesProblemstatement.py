# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:38:04 2022

@author: KATARI ADITHYA
"""

import numpy as np
import pandas as pd
d=pd.read_csv("D:/Desktop/datasets1/animal_category.csv")
d.dtypes
from sklearn.preprocessing import OneHotEncoder
enc=OneHotEncoder()
d1=pd.DataFrame(enc.fit_transform(d).toarray())
