from .scraper import Scraper
import re
import numpy as np


class EasySpellingScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

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
                        data = np.concatenate((data, [ele.get_text() for ele in ele_list if len(ele.get_text().split(' ')) == 1 and len(ele.get_text()) > 5])).tolist()

        return data

    def run(self):
        soup = self.get_soup()
        data = self.get_data_from_sibling(soup, "h2", "a")
        self.data['answers'] = [[d] for d in data]
        self.write_to_json(self.data)

def run_easy_spelling_scraper():
    url = "https://grammar.yourdictionary.com/spelling-and-word-lists/misspelled.html"
    scraper = EasySpellingScraper(url, '../data/easy_speling_data.json')
    scraper.run()
    print("finished easy spelling words scraper")

if __name__ == "__main__":
    run_easy_spelling_scraper()
