'''
This is a portion of the code for dataAnalysis.py meant to :

Pull data from a CSV convert it to a pandas data frame
Return the proper headers and the amount of data missing from each.
Present options for filling the data that is missing
Detect qualitative fields and present options to quantify them
Reveiw data base fields and repeat
'''

import pandas as pd
import sqlite3
from navigation import navigation

option = navigation()
#print(option)
pandasdf = pd.read_csv(option)
print(pandasdf)
conn = sqlite3.connect('insurance_data.db')
pandasdf.to_sql('insurance_data', conn, if_exists='replace', index=False)
query = pd.read_sql_query("SELECT * FROM insurance_data WHERE total_claim_amount > 10000", conn)
print(query)
conn.close()
