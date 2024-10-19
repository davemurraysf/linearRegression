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
import numpy as np
import pandas as pd
import sqlite3


def unique_values(dataframe: pd.DataFrame ,field):
    unique_values = dataframe[field].nunique()
    total_records = len(dataframe)
    unique_percentage = unique_values/total_records
    return unique_percentage

def check_qualitative(conn, target, qualitative, threshold):
    search_string = "SELECT * FROM insurance_data"
    df = pd.read_sql_query(search_string, conn)
    qualitative_check = {}
    exclusion_list = []
    for quals in qualitative:
        percentage_unique = unique_values(df, quals)
        contingency_table = pd.crosstab(df[quals], df[target])
        chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)
        if percentage_unique > threshold:
            qualitative_check[quals] = f'"Exclude: High cardinality ({percentage_unique:.2%} unique values)"'
            exclusion_list.append(quals)
        elif p_value > 0.05:
            qualitative_check[quals] = f"Exclude: Low significance (p-value={p_value:.4f})"
            exclusion_list.append(quals)
        else:
            qualitative_check[quals] = "Keep: Column is relevant"
    return qualitative_check, exclusion_list

def check_quantitative(conn, target, quantitative, threshold):
    search_string = "SELECT * FROM insurance_data"
    df = pd.read_sql_query(search_string, conn)
    quantitative_check = {}
    exclusion_list = []
    for quants in quantitative:
        #removed cardinality check for quantitative numbers due to the uniqueness of real numbers.
        contingency_table = pd.crosstab(df[quants], df[target])
        chi2, p_value, _, _ = stats.chi2_contingency(contingency_table)
        if p_value > 0.05:
            quantitative_check[quants] = f"Exclude: Low significance (p-value={p_value:.4f})"
            exclusion_list.append(quants)
        else:
            quantitative_check[quants] = "Keep: Column is relevant"
    return quantitative_check, exclusion_list

def combine_list(l1: list, l2: list) -> list:
    l3 = l1 + l2
    return l3

def remove_from_list(l1: list, l2: list) -> list: 
    l3 = [x for x in l1 if x not in l2]
    return l3

def handle_missing_data(conn, fields: list, missing_paramater: str, strategy: int)-> pd.DataFrame:
    search_string = "SELECT * FROM insurance_data"
    dataframe = pd.read_sql_query(search_string, conn)
    dataframe.replace(missing_paramater, np.nan, inplace=True)
    for field in fields:
        field_type = dataframe[field].dtype
        match field_type:
            case "float64" | "int64":
                match strategy:
                    case 1: #mean
                        dataframe[field].fillna(dataframe[field].mean(), inplace=True)
                        continue
                    case 2: #median
                        dataframe[field].fillna(dataframe[field].median(), inplace=True)
                        continue
                    case 3: #mode
                        dataframe[field].fillna(dataframe[field].mode()[0], inplace=True)
                        continue
            case "object":
                match strategy:
                    case 1: #mode
                        dataframe[field].fillna(dataframe[field].mode()[0], inplace=True)
                        continue
                    case 2: #unkown
                        dataframe[field].fillna('Unknown', inplace=True)
                        print(dataframe[field])
                        continue
                    case 3:
                        print("invalid input")
                        continue
    return dataframe

        


def clean_data_return () -> pd.DataFrame:
    connection = dc.connect()
    qualitative, quantitative, headers = dc.extract_table_info(connection)
    target = n.menu(headers)
    thresh = n.get_input_int("Please enter threshold value: ")
    check_quals, exclude_quals = check_qualitative(connection, target, qualitative, thresh)
    check_quants, exclude_quants = check_quantitative(connection, target, quantitative, thresh)
    exclusion_list = combine_list(exclude_quals, exclude_quants)
    paramater_list = remove_from_list(headers,exclusion_list)
    missing_paramater = input("What character is used to display missing data? ")
    incomplete_paramaters = dc.find_missing_data(connection, paramater_list, missing_paramater)
    complete_data = handle_missing_data(connection,incomplete_paramaters,missing_paramater,1)
    clean_data = complete_data.drop(columns=exclusion_list)
    return(clean_data)

data = clean_data_return()
print(data)




        




