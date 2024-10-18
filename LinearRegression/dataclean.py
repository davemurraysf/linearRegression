'''
This is a portion of the code for dataAnalysis.py meant to :

Pull data from a CSV convert it to a pandas data frame
Return the proper headers and the amount of data missing from each.
Present options for filling the data that is missing
Detect qualitative fields and present options to quantify them
Reveiw data base fields and repeat
'''

import pandas
import sqlite3
from navigation import navigation

option = navigation()
print(option)