'''
This is the main code file of the linear regression program it will call from other files to perform actions like
-data cleaning
-data visualization
-data regression
The goal is to build the foundations of a linear regression program for connecting to an Electron React UI at a later date

It should:
Pull data; 1
Capture hearders; 1
Detect missing data; 1
Present options for filling missing data; 1
Change qualitative data into quantitative data; 1
Enable user to pick what variable to add and perform a linear regression on; 1
Provide the output of the regression; 0

Packages used: 

ETA: 5 hours
Created by: David M Murray
Date: 10/18/2024

To do:

1. create classes for data and model
2. Add visualization of dataset vs model
3. Add input value and expected out put
4. see what processes can be converted to metal to learn gpu programing

'''


from dataRegression import clean_data_return
from dataclean import get_csv, database
import navigation as n
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
import os

'''
----------------------------------------------------------------------------------------------
Calls get csv from dataclean.py using the navigation in the terminal from navigaition.py to 
create the insurance_data.db and load the dat into th program
----------------------------------------------------------------------------------------------
'''

option = get_csv()
database(option)

'''
----------------------------------------------------------------------------------------------
Calls the clead data return function from dataRegression.py to clean and replace data 
takes in database option and returns a pandas dataframe of all data that will be useful based
on a p-value threshold to a target input then also returns the target of the regression as a string
----------------------------------------------------------------------------------------------
'''
data, tar = clean_data_return()

'''
----------------------------------------------------------------------------------------------
Creates multiple data frames to prepare for running linear regression model on target using variables
----------------------------------------------------------------------------------------------
'''

variables = data.drop(columns=[tar])
target = data[tar]
print(variables)
print(target)
variables = pd.get_dummies(variables, drop_first=True)
print(variables)

'''
----------------------------------------------------------------------------------------------
Splits data inton training and testing sets based on portion and randomness
----------------------------------------------------------------------------------------------
'''
variables_train, variables_test, target_train, target_test = train_test_split(variables, target, test_size=0.2, random_state=42)


'''
----------------------------------------------------------------------------------------------
Builds linear regression model using data
----------------------------------------------------------------------------------------------
'''
model = LinearRegression()
model.fit(variables_train, target_train)
target_pred = model.predict(variables_test)

mse = mean_squared_error(target_test, target_pred)
r2 = r2_score(target_test, target_pred)
'''
----------------------------------------------------------------------------------------------
output
----------------------------------------------------------------------------------------------
'''

print("Coefficients (Feature Weights):", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

output = pd.DataFrame({'Actual': target_test, 'Predicted': target_pred})
output.to_csv('LinearRegression/datasets/predictions.csv', index=False)
print("Predictions saved to 'predictions.csv'")
