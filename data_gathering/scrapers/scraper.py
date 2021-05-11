import requests
from bs4 import BeautifulSoup
import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from utils.common import Common


class Scraper(Common):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text':'',
            'answers':[]
        }

    def get_soup(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, "lxml")

