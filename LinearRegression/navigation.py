'''
This is a portion of the code for dataAnalysis.py meant to :

Enable simple file selection from the terminal
'''

import os
import PyInquirer
'''
----------------------------------------------------------------------------------------------
#Lists files and folders in cwd
----------------------------------------------------------------------------------------------
'''
def list_files_and_folders(path="."):
    items = os.listdir(path)
    items.sort()
    items.insert(0, ".. retrun to prior directory")
    return items

'''
----------------------------------------------------------------------------------------------
#check if csv
----------------------------------------------------------------------------------------------
'''
def is_csv_file(filename):
    return filename.endswith('.csv')

'''
----------------------------------------------------------------------------------------------
#build menu from a current working directory
----------------------------------------------------------------------------------------------
'''
def prompt_selection(path):
    items = list_files_and_folders(path)

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': f'Current directory: {path}. Select a file or folder:',
            'choices': items
        }
    ]

    answers = PyInquirer.prompt(questions)
    return answers['selection']
'''
----------------------------------------------------------------------------------------------
#displays and enables user selection of path as menu in terminal
----------------------------------------------------------------------------------------------
'''
def navigation():
    current_path = os.getcwd()

    while True:
        selection = prompt_selection(current_path)
        if selection == ".. retrun to prior directory":
            current_path = os.path.dirname(current_path)
        else:
            full_path = os.path.join(current_path, selection)
            if os.path.isdir(full_path):
                current_path = full_path
            else:
                if is_csv_file(selection):
                    full_path = os.path.join(current_path, selection)
                    #print(f'CSV file selected: {selection}')
                    return full_path
                else:
                    print("Error: Please select a CSV file.")


'''
----------------------------------------------------------------------------------------------
#build menu from a dictionary
----------------------------------------------------------------------------------------------
'''
def menu_selection(options):
    items = [{'name': str(option)} for option in options]

    questions = [
        {
            'type': 'list',
            'name': 'selection',
            'message': 'Select Linear Regression Target Variable',
            'choices': items
        }
    ]

    answers = PyInquirer.prompt(questions)
    return answers['selection']

'''
----------------------------------------------------------------------------------------------
#build runs menu and returns selection from a list
----------------------------------------------------------------------------------------------
'''
def menu(options):

    while True:
        selection = menu_selection(options)
        return selection

def get_input_int(text):
    
    while True:
        number_str = input(text)
        try:
            number = float(number_str)
            #print("You entered:", number)
            return number
        except ValueError:
            print("Invalid input. Please enter an float.")


#options_list = [1,2,3,4,5]
#selected = menu(options_list)
#print(selected)

#option = navigation()
#print(option)
#number = get_input_int("Please enter threshold value: ",)
#print(number)

