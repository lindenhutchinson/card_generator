from scraper import Scraper
import re


class CelebrityScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

    def get_celebs(self):
        soup = self.get_soup()
        h3_list = soup.find_all("h3", class_="lister-item-header")

        for h3 in h3_list:
            a = h3.find("a")
            text = a.get_text().replace("\n", "").strip()
            self.data['answers'].append(text)

    def run(self):
        self.data['game_text'] = "Hint: Actor"
        self.get_celebs()
        self.write_to_json(self.data)


if __name__ == "__main__":
    url = "https://www.imdb.com/list/ls052283250/"
    scraper = CelebrityScraper(url, '../data/celebrity_data.json')
    scraper.run()
