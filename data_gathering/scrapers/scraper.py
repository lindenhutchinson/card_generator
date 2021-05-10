import requests
from bs4 import BeautifulSoup
import json
import re
import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)

from utils.common import Common


class Scraper(Common):
    def __int__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def get_soup(self):
        page = requests.get(self.url)
        return BeautifulSoup(page.content, "lxml")

