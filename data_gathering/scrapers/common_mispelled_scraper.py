from scraper import Scraper
import re
import numpy as np


class CommonMispelledScraper(Scraper):
    def __init__(self, url, output_file, url_list=[]):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }
        self.url_list = url_list

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
                        data = np.concatenate((data, [ele.get_text() for ele in ele_list if len(
                            ele.get_text().split(' ')) == 1 and len(ele.get_text()) > 5])).tolist()

        return data

    def run(self):
        for url in self.url_list:
            soup = self.get_soup(url)
            data = self.get_data_from_sibling(soup, "h2", "a")
            for d in data:
                split_string = ""
                for i, char in enumerate(d):
                    if i == len(d)-1:
                        split_string += char
                    else:
                        split_string += f"{char} - "

                split_string = split_string[::-1]
                answer_text = [d, split_string]
                self.data['answers'].append(answer_text)

        self.write_to_json(self.data)


if __name__ == "__main__":
    urls = ['https://grammar.yourdictionary.com/spelling-and-word-lists/misspelled.html',
            'https://grammar.yourdictionary.com/spelling-and-word-lists/150more.html']

    scraper = CommonMispelledScraper(
        'url', '../data/spelling_data.json', urls)
    scraper.run()
