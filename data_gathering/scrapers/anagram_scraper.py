from scraper import Scraper
import re
import numpy as np


class AnagramScraper(Scraper):
    def __init__(self, output_file, url_list=[]):
        self.output_file = output_file
        self.url_list = url_list

    def get_data_from_siblings(self, soup, first_sibling, second_sibling, desired_tag):
        # uses two siblings of the desired element to locate it
        first = soup.find(first_sibling)
        data = []
        if hasattr(first, 'contents'):
            if second_sibling == first.next_sibling.name:
                header_patterns = [r'\bof\b\s(.+)', r'[-](.+)']
                header = first.next_sibling.get_text()

                for pat in header_patterns:
                    hint = re.findall(pat, header)
                    if len(hint) == 1:
                        hint = hint[0]
                        break

                p_ele = first.find_next(desired_tag)
                for span in p_ele.find_all('span'):
                    if hasattr(span, 'contents'):
                        if len(span.contents) > 10:
                            for text in span.contents:
                                answer_anagram = re.findall(
                                    r"(^[\w\s,’']+)\s*[:-=]\s*([\w\s,’']+)", str(text))
                                if len(answer_anagram) == 1:
                                    answer, anagram = answer_anagram[0]
                                    data.append(
                                        {'answer': [answer], 'game_text': [f"Hint: {hint}", anagram]})

        return data

    def run(self):
        big_data = []
        for url in self.url_list:
            soup = self.get_soup(url)
            data = self.get_data_from_siblings(soup, "h2", "h3", "p")
            if data:
                big_data = np.concatenate((data, big_data)).tolist()

        self.write_to_json(big_data)


if __name__ == "__main__":
    urls = ['http://www.english-for-students.com/Anagram-Movies.html',
            'http://www.english-for-students.com/Anagrams-of-TV-World.html',
            'http://www.english-for-students.com/Anagrams-of-famous-people.html',
            'http://www.english-for-students.com/Anagrams-of-Food-and-Drinks.html',
            'http://www.english-for-students.com/Anagrams-Politics.html']

    scraper = AnagramScraper('../../src/data/zelpuz.json', urls)
    scraper.run()
