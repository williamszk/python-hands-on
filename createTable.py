#createTable.py
from random import sample
import pandas as pd
import numpy as np
def viewCsv(df,name):
	len1 = df.shape[0] #length of table
	vv = list(np.arange(len1))
	obs1 = sample(vv,20)
	df.iloc[obs1,:].to_csv(name,index=False)
#tad oecdBli.csv

