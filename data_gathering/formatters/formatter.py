import json
import os


def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))
    
# TODO: Should create a common utils class for loading and writing json data

class Formatter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def load_json_data(self):
        string_data = ''
        with open(f"{get_current_path()}/{self.input_file}", 'r', encoding="utf8") as fn:
            string_data = fn.read()

        return json.loads(string_data)

    def write_to_json(self, data):
        json_data = json.dumps(data)

        with open(f"{get_current_path()}/{self.output_file}", "w", encoding="utf8") as fn:
            fn.writelines(json_data)
