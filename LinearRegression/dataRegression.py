'''
This is a portion of the code for dataAnalysis.py meant to :

Have the user select the target variable
Choose paramaters
Run replacements of missing data
Clean selected paramaters
Run a linear regression
'''

import dataclean as dc
import navigation as n
import scipy.stats as stats
import pandas as pd
import sqlite3

connection = dc.connect()
#print(connection)
qualitative, quantitative, headers = dc.extract_table_info(connection)
#print(headers)
target = n.menu(headers)
print("regression target: "target)

def check_qualitative(conn):

