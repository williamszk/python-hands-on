#191226 reproduce

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
from random import sample
from createTable import viewCsv
from prepareCountry import prepareCountryStats

# Load the data
#where the data comes from and readme
#https://github.com/ageron/handson-ml2/tree/master/datasets/lifesat
fileOecd = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/lifesat/oecd_bli_2015.csv"
oecdBli = pd.read_csv(fileOecd, thousands=',')
fileGpd = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/lifesat/gdp_per_capita.csv"
gdpPerCapita = pd.read_csv(fileGpd,thousands=',',delimiter='\t',
encoding='latin1', na_values="n/a")

# Prepare the data
countryStats = prepareCountryStats(oecdBli, gdpPerCapita)
X = np.c_[countryStats["GDP per capita"]]
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

#use knn
import sklearn.neighbors
model = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
model.fit(X, y)
X_new = [[22587]] # Cyprus' GDP per capita
print(model.predict(X_new)) # outputs [[ 5.96242338]]









