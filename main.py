import os
import json

from models import *
from texttable import Texttable

def print_table(headers : List[str], employees : List[Employee]):
    table = Texttable()
    table.add_row(headers)
    for i in range(len(employees)):
        table.add_row([
                        str(i + 1), 
                        employees[i].name, 
                        employees[i].age, 
                        employees[i].salary
                    ])
    
    os.system('cls')
    print(table.draw())

def choose_lang(text : str, default_lang : str) -> str:
    os.system('cls')
    lang = input(text.capitalize() + '\n' +
                '1 - en.\n' +
                '2 - ru.\n' +
                ': ')
    os.system('cls')

    match lang:
        case '1':
            return 'en'
        case '2':
            return 'ru'
        case _:
            return default_lang

f = open("employees.json")
data = json.load(f)

default_lang = Locale.get_default_lang(data)
input_choose_lang_msg = Locale.get_input_choose_lang(default_lang, data)
lang = choose_lang(input_choose_lang_msg, default_lang)
_ = Locale(lang, data)

headers : List[str] = [header.capitalize() for header in _.get_headers()]
employees : List[Employee] = _.get_employees()

employees.sort(key=lambda x: x.salary)

print_table(headers, employees)

print()
emp_rm = int(input(_.get_input_num_emp().capitalize() + ': '))
employees.pop(emp_rm - 1)

print_table(headers, employees)