import os
import json


class Common:
    """For loading and writing json files.


        This class uses its current path to determine the location of the passed files. Do not use a leading / in the path.
        Always pass a relative path

    Args:
        input_file (string): a relative path to a json file eg: '../data.json'

        output_file (string): a relative path to a json file eg: '../card.json'
    """

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def get_current_path(self):
        return os.path.dirname(os.path.abspath(__file__))

    def write_to_json(self, data):
        json_data = json.dumps(data)

        with open(f"{self.get_current_path()}/{self.output_file}", "w", encoding="utf8") as fn:
            fn.writelines(json_data)

    def append_to_json(self, data):
        json_data = json.dumps(data)

        with open(f"{self.get_current_path()}/{self.output_file}", "a+", encoding="utf8") as fn:
            fn.writelines(json_data)

    def load_json_data(self, file):
        string_data = ''
        with open(f"{self.get_current_path()}/{file}", 'r', encoding="utf8") as fn:
            string_data = fn.read()

        return json.loads(string_data)
