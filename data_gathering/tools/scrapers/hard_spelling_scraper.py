from .scraper import Scraper
import re
import numpy as np


class HardSpellingScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

    def run(self):
        soup = self.get_soup()
        self.data['answers'] = self.get_data_from_sibling(soup, "h3", "td")
        self.write_to_json(self.data)


def run_hard_spelling_scraper():
    url = "https://grammar.yourdictionary.com/spelling-and-word-lists/high-school-level-spelling-words.html"
    scraper = HardSpellingScraper(url, '../data/spelling_data1.json')
    scraper.run()
    print("finished hard spelling words scraper")

if __name__ == "__main__":
    run_hard_spelling_scraper()
