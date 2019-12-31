#191226 experiment.py
#changing panas options
pd.set_option('display.max_rows',10)
pd.set_option('display.max_colwidth',2)
pd.set_option('display.width',None)
pd.set_option('display.max_columns',None)
oecdBli


#do not run - experiment ------------------------------------------

import ipywidgets as widgets
from IPython import display
import pandas as pd
import numpy as np

# sample data
df1 = pd.DataFrame(np.random.randn(8, 3))
df2 = pd.DataFrame(np.random.randn(8, 3))


# create output widgets
widget1 = widgets.Output()
widget2 = widgets.Output()

# render in output widgets
with widget1:
    display.display(df1)
with widget2:
    display.display(df2)

# create HBox
hbox = widgets.HBox([widget1, widget2])

# render hbox
hbox

from IPython.core.display import display, HTML

display(HTML(oecdBli.iloc[0:3,:].to_html()))
# -----------------------------------

#https://www.geeksforgeeks.org/python-pandas-pivot/
# Create a simple dataframe 
  
# importing pandas as pd 
import pandas as pd 
  
# creating a dataframe 
df = pd.DataFrame({'Name': ['John', 'Boby', 'Mina'], 
      'Degree': ['Masters', 'Graduate', 'Graduate'], 
      'Score': [27, 23, 21]}) 
df 

# values can be an object or a list 
df.pivot('Name', 'Degree', 'Score') 

#another example
df = pd.DataFrame({'Name': ['John', 'Boby', 'Mina','John', 'Boby', 'Mina'], 
      'Month': ['January', 'January', 'January','February', 'February', 'February'], 
      'Score': [27, 23, 21, 30, 22, 24]}) 
df.to_csv("test.csv",index=False)
tad test.csv
df 

df.pivot('Name','Month','Score')
#it automatically creates columns in alphabetical order
df.to_csv("test.csv",index=False)

#-----------------------

# Python3 program to demonstrate 
# the use of sample() function . 

# import random 
from random import sample 

# Prints list of random items of given length 
list1 = [1, 2, 3, 4, 5] 

print(sample(list1,3)) 

# ------------------------
#http://hamelg.blogspot.com/2015/11/python-for-data-analysis-part-19_17.html





































