import sqlite3
from json import load, loads

from django.db import models

# Create your models here.


class ChoiceQuestions(models.Model):

    def __init__(self, data):
        self.data = str(data)

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
            num = data["num"]
            user_name = data["stdudent_name"]
            test_input = data["test"]
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
