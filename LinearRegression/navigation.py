'''
This is a portion of the code for dataAnalysis.py meant to :

Enable simple file selection from the terminal
'''

import os
import PyInquirer

def list_files_and_folders(path="."):
    items = os.listdir(path)
    items.sort()
    items.insert(0, ".. retrun to prior directory")
    return items

def is_csv_file(filename):
    return filename.endswith('.csv')

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
                    #print(f'CSV file selected: {selection}')
                    return selection
                else:
                    print("Error: Please select a CSV file.")


#option = navigation()
#print(option)
