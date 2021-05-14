import requests
from bs4 import BeautifulSoup
import os

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0, parentdir)
from utils.common import Common

import numpy as np

class Scraper(Common):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

    def print_progress(self, current, total):
        os.system('cls')
        print(f"scraping data {current}/{total}")

    def get_soup(self, url=''):
        if url:
            page = requests.get(url)
        else:
            page = requests.get(self.url)
            
        return BeautifulSoup(page.content, "lxml")

    def get_data_from_sibling(self, soup, sibling_tag, desired_tag):
        """Uses a sibling_tag (such as a h3) and finds data in its siblings using the desired_tag (such as table)

        Args:
            soup (BeautifulSoup()): An instance of a BeautifulSoup class
            sibling_tag (string): The tag identifying the sibling of the desired data
            desired_tag (string): The tag identifying the element that contains the desired data

        Returns:
            data (array): a list containing the scraped string data
        """
        data = []

        sibling_container = soup.find_all(sibling_tag)
        for root in sibling_container:
            for sib in root.next_siblings:
                if hasattr(sib, 'contents'):
                    ele_list = sib.find_all(desired_tag)
                    if len(ele_list):
                        data = np.concatenate((data, [ele.get_text()
                                                      for ele in ele_list])).tolist()

        return data
