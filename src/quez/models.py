import re
import sqlite3
from json import load, loads

from django.db import models

# Create your models here.


class ChoiceQuestions(models.Model):

    def __init__(self, data):
        self.data = str(data)

    def _remove_non_alphanum_char(self, string):
        return re.sub(r'\W+', ' ', string)

    def _translate_numbers(self, current, new, string):
        translation_table = str.maketrans(current, new)
        return string.translate(translation_table)

    def normalize_string(self, student_data, intorstr=False):
        """gets a string and standardize it as following:
        >> converts(removes others) all chars to persionChar or 
        >> converts(removes others) all chars to EnglishDigits"""

        student_data = self._remove_non_alphanum_char(str(student_data))
        student_data = student_data.upper()

        persian_numerals = '۱۲۳۴۵۶۷۸۹۰'
        arabic_numerals = '١٢٣٤٥٦٧٨٩٠'
        english_numerals = '1234567890'

        student_data = self._translate_numbers(
            persian_numerals, english_numerals, student_data)
        student_data = self._translate_numbers(
            arabic_numerals, english_numerals, student_data)

        if intorstr != False:
            all_digit = "".join(re.findall("\d", student_data))
            return int(all_digit)
        else:
            all_alpha = "".join(re.findall("[آ-ی- ]", student_data))
            return all_alpha

    def cmp(self, first_dict, second_dict):
        """Comparison first_dict and
        second_dict and scoreing Input's"""

        try:
            # If The user enters something other then dictionary,
            # the program says: Please Enter the dictionary.
            score = 0

            for num in first_dict:
                if first_dict[num] == second_dict[num]:
                    score += 1
            return score
        except ValueError:
            return "ValueError. Please Enter The dictionary"

    def json_render_score(self, test_input):
        """json read in parent_file and Comparison """

        # TODO: The User it self make this Json
        parent_file = open("quez/json/valed.json", "r")
        parent = load(parent_file)["test"]
        return self.cmp(parent, test_input)

    def get_data_json(self):
        """This Func work is get json data in client
        and proccesing data. In the End, return Procced data's"""
        try:
            # call data's in json

            data = f'{self.data}'
            data = data.replace("'", '"')

            data = loads(data)
            # add data to varble
            num = self.normalize_string(data["num"], intorstr=True)
            user_name = self.normalize_string(data["stdudent_name"])
            if "  " in user_name:
                user_name = None

            test_input = data["test"]

            print(num, user_name)
            score = self.json_render_score(test_input)
            # connect sqlite DB
            conn = sqlite3.connect("score.db")
            cur = conn.cursor()
            # create DataBase and add data to DataBase
            cur.execute('''CREATE TABLE IF NOT EXISTS students(
                num INTEGER PRIMARY KEY,
                user_name TEXT,
                test_input JSON,
                socre TEXT);
                ''')

            # Add json File and socre to DB
            query = f'INSERT INTO students VALUES("{num}", "{user_name}", "{test_input}", "{score}")'

            cur.execute(query)
            conn.commit()

            conn.close()
            return f"{num}, {user_name}, {test_input}, {score}"

        except:
            return '{"Success":"False"}'
