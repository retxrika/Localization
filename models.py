import locale
import ctypes

from typing import List, Dict

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):

        return f'{self.name} {self.age} {self.salary}'

class Locale():
    __lang : str
    __data : Dict

    @staticmethod
    def get_default_lang(data : Dict):
        windll = ctypes.windll.kernel32
        windll.GetUserDefaultUILanguage()
        lang = locale.windows_locale[windll.GetUserDefaultUILanguage()]
        lang_iso = lang[:2]

        if lang_iso not in data['langs']:
            return 'en'
        return lang_iso

    def get_headers(self) -> List[str]:
        return [
                    self.__data['headers'][header][self.__lang] 
                    for header in self.__data['headers']
                ]

    def get_employees(self) -> List[Employee]:
        return [
                    Employee(self.__data['employees'][employee][self.__lang], 
                        self.__data['employees'][employee]['age'], 
                        self.__data['employees'][employee]['salary']) 
                    for employee in self.__data['employees']
                ]
    
    def get_input_num_emp(self) -> str:
        return self.__data['input'] \
                        ['enter employee number to terminate'] \
                        [self.__lang]
    
    @staticmethod
    def get_input_choose_lang(lang : str, data : Dict) -> str:
        return data['input'] \
                    ['select a language from the available'] \
                    [lang]

    def __init__(self, lang : str, data : Dict):
        self.__data = data
        lang = lang.lower()
        if lang not in self.__data['langs']:
            lang = Locale.get_default_lang(self.__data['langs'])
            error = self.__data['errors'] \
                               ['the language you selected does not exist in the database'] \
                               [lang]
            raise Exception(error)
        self.__lang = lang
