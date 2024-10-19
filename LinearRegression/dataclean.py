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

'''
----------------------------------------------------------------------------------------------
#get file path
----------------------------------------------------------------------------------------------
'''
def get_csv():
    option_selected = navigation()
    #print(option)
    return option_selected 

'''
----------------------------------------------------------------------------------------------
#convert to database function
----------------------------------------------------------------------------------------------
'''
def database(option): 
    pandasdf = pd.read_csv(option)
    #print(pandasdf)
    conn = sqlite3.connect('insurance_data.db')
    pandasdf.to_sql('insurance_data', conn, if_exists='replace', index=False)
    return conn

'''
----------------------------------------------------------------------------------------------
#reconnects to database when connection is closed
----------------------------------------------------------------------------------------------
'''
def connect():
    conn = sqlite3.connect('insurance_data.db')
    return conn

'''
----------------------------------------------------------------------------------------------
#reconnects to database when connection is closed
----------------------------------------------------------------------------------------------
'''
def close(conn):
    conn.close()

'''
----------------------------------------------------------------------------------------------
#extract table info cursor
----------------------------------------------------------------------------------------------
'''
def extract_table_info(conn):
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(insurance_data)")
    headers_info = cursor.fetchall()
    #print(headers_info)
    fields = []
    quant = []
    qual = []
    for header in headers_info:
        print(f"Header Name: {header[1]}, Data Type: {header[2]}")
        fields.append(header[1])
        dataType = header[2]
        match dataType:
            case "INTEGER":
                quant.append(header[1])
            case "FLOAT":
                quant.append(header[1])
            case "REAL":
                quant.append(header[1])
            case "TEXT":
                qual.append(header[1])
    #print(fields)
    return qual, quant, fields

'''
----------------------------------------------------------------------------------------------
#query missing data
----------------------------------------------------------------------------------------------
'''
def find_missing_data(conn, fields, missing_param):
    missing_data= []
    for field in fields:
        search_string = "SELECT * FROM insurance_data WHERE {f} = '{m}'".format(f = field, m = missing_param)
        #print(search_string)
        query = pd.read_sql_query(search_string, conn)
        #print(query)
        if query.empty:
            #print(f"No missing data found for field {field}")
            continue
        else:
            #print(f"Missin Data found for field: {field}")
            missing_data.append(field)
    #print(missing_data)

'''
----------------------------------------------------------------------------------------------
#unique qualitative
----------------------------------------------------------------------------------------------
'''
def unique_qualitative_values(conn, qual):
    dynamic_dict_qual = {}
    for field in qual:
        #field_name = field
        search_string = "SELECT DISTINCT {f} FROM insurance_data".format(f = field)
        dict_name = "{f}_dict".format(f=field)
        query = pd.read_sql_query(search_string, conn)
        print(query[field])
        dynamic_dict_qual[dict_name] = {i: value for i, value in enumerate(query[field])}
    for name, content in dynamic_dict_qual.items():
        print(f"{name}: {content}")


'''
----------------------------------------------------------------------------------------------
#query
----------------------------------------------------------------------------------------------
'''
'''
query = pd.read_sql_query("SELECT * FROM insurance_data WHERE total_claim_amount > 10000", conn)
#print(query)
'''



'''
----------------------------------------------------------------------------------------------
# Test of functions in code
----------------------------------------------------------------------------------------------
'''

'''
csv_path = get_csv()
connection = database(csv_path)
connection = connect()
qualitative, quantitative, headers = extract_table_info(connection)
print(qualitative)
print(quantitative)
print(headers)
missing_data_paramater = "?"
missing_data = find_missing_data(connection, headers, missing_data_paramater)
print(missing_data)
unique_values = unique_qualitative_values(connection, qualitative)
close(connection)
'''

'''
----------------------------------------------------------------------------------------------
#close
----------------------------------------------------------------------------------------------
'''

'''
connection.close()
'''
