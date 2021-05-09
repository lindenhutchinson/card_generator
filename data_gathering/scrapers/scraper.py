import requests
from bs4 import BeautifulSoup
import json
import re
import os

def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))

class Scraper:
    def __int__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def get_soup(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, "lxml")

    def write_to_json(self, data):
        json_data = json.dumps(data)

        with open(f"{get_current_path()}/{self.output_file}", "w", encoding="utf8") as fn:
            fn.writelines(json_data)
