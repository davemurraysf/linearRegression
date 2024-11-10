from dataRegression import clean_data_return
from dataclean import get_csv, database
import navigation as n
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt

option = get_csv()
database(option)
data = clean_data_return()
headers = data.columns
while True:
    n.menu(headers)



