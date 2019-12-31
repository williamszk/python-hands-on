#191226 handson notebook chap1
#https://github.com/ageron/handson-ml2/blob/master/01_the_machine_learning_landscape.ipynb
# Python ≥3.5 is required
import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn ≥0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"
import pandas as pd
"""
Python’s assert statement is a debugging aid that tests a 
condition. If the condition is true, it does nothing and 
your program just continues to execute. But if the assert 
condition evaluates to false, it raises an AssertionError 
exception with an optional error message.
"""

#https://github.com/ageron/handson-ml2/blob/master/01_the_machine_learning_landscape.ipynb

def prepareCountryStats(oecdBli, gdpPerCapita):
    oecdBli = oecdBli[oecdBli["INEQUALITY"]=="TOT"]
    oecdBli = oecdBli.pivot(index="Country", columns="Indicator", values="Value")
    gdpPerCapita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdpPerCapita.set_index("Country", inplace=True)
    fullCountryStats = pd.merge(left=oecdBli, right=gdpPerCapita,
                                  left_index=True, right_index=True)
    fullCountryStats.sort_values(by="GDP per capita", inplace=True)
    removeIndices = [0, 1, 6, 8, 33, 34, 35]
    keepIndices = list(set(range(36)) - set(removeIndices))
    return fullCountryStats[["GDP per capita", 'Life satisfaction']].iloc[keepIndices]












































