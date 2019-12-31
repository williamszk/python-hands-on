#191226 chap1

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
from random import sample
from createTable import viewCsv


pwd()
# Load the data
#where the data comes from and readme
#https://github.com/ageron/handson-ml2/tree/master/datasets/lifesat
fileOecd = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/lifesat/oecd_bli_2015.csv"
oecdBli = pd.read_csv(fileOecd, thousands=',')
fileGpd = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/lifesat/gdp_per_capita.csv"
gdpPerCapita = pd.read_csv(fileGpd,thousands=',',delimiter='\t',
encoding='latin1', na_values="n/a")

viewCsv(oecdBli,oecdBli)
#https://www.tadviewer.com/
tad oecdBli.csv

viewCsv(gdpPerCapita,gdpPerCapita)
tad gdpPerCapita.csv
gdpPerCapita.shape
#csvtool readable gdpPerCapita.csv | view -

"""
The prepare_countryStats() function’s definition 
is not shown here (see this chapter’s Jupyter notebook if
you want all the gory details). It’s just boring Pandas 
code that joins the life satisfaction data from the OECD
with the GDP per capita data from the IMF.
"""
#https://github.com/ageron/handson-ml2/blob/master/01_the_machine_learning_landscape.ipynb

oecdBli.columns
oecdBli = oecdBli[oecdBli["INEQUALITY"]=="TOT"]
oecdBli["Indicator"]
type(oecdBli["Indicator"])

table1 = pd.crosstab(index=oecdBli["Indicator"],columns='count')
table1
#all possible values in "indicador"
type(table1) #data frame
table1.shape

oecdBli.shape
oecdBli = oecdBli.pivot(index="Country", columns="Indicator", values="Value")
oecdBli.shape

viewCsv(oecdBli,oecdBli)
tad oecdBli.csv

gdpPerCapita.rename(columns={"2015": "GDP per capita"}, inplace=True)
gdpPerCapita.set_index("Country", inplace=True)

fullCountryStats = pd.merge(left=oecdBli, right=gdpPerCapita,
                              left_index=True, right_index=True)

fullCountryStats.sort_values(by="GDP per capita", inplace=True)
fullCountryStats

removeIndices = [0, 1, 6, 8, 33, 34, 35]  #index for observations

set1 = set(range(36))
type(set1)
set2 = set(removeIndices)
set1 - set2

keepIndices = list(set(range(36)) - set(removeIndices))


fullCountryStats2 = fullCountryStats[["GDP per capita", 'Life satisfaction']].iloc[keepIndices]
pwd()
viewCsv(fullCountryStats2,"fullCountryStats2.csv")
tad fullCountryStats2.csv

# -------------------

from prepareCountry import prepareCountryStats

# Prepare the data
countryStats = prepareCountryStats(oecdBli, gdpPerCapita)

X = np.c_[countryStats["GDP per capita"]]
#np.c_ transforms a series into a np.array
aa = countryStats["GDP per capita"]
type(aa)

y = np.c_[countryStats["Life satisfaction"]]


# Visualize the data
countryStats.plot(kind='scatter', x="GDP per capita", y='Life satisfaction')
plt.show()

# Select a linear model
model = sklearn.linear_model.LinearRegression()

# Train the model
model.fit(X, y)

# Make a prediction for Cyprus
X_new = [[22587]] # Cyprus' GDP per capita
print(model.predict(X_new)) # outputs [[ 5.96242338]]


import sklearn.neighbors
model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)
X_new = [[22587]] # Cyprus' GDP per capita
print(model.predict(X_new)) # outputs [[ 5.96242338]]
















