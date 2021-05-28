import json
import re
from .scraper import Scraper


class RocknRollScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

    def clean_text(self, text):
        return text.replace('\r', '').replace('\n', '').replace('\t', '').replace('\xa0', '').strip()

    def get_songs(self):
        soup = self.get_soup()
        for tr in soup.find_all('tr')[1:]:
            td_list = tr.find_all('td')
            song = self.clean_text(td_list[1].get_text())
            artist = self.clean_text(td_list[2].get_text())
            backwards_name = re.findall(r'([\w]+),\s([\w]+)', artist)
            if len(backwards_name) == 1:
                artist = f"{backwards_name[0][1]} {backwards_name[0][0]}"
            self.data['answers'].append([f"{song} - {artist}"])



    def run(self):
        self.get_songs()
        self.write_to_json(self.data)


def run_rocknroll_scraper():
    url = "https://rocknrollamerica.net/Top1000.html"
    scraper = RocknRollScraper(url, '../data/rocknroll_data.json')
    scraper.run()
    print("finished rock n roll scraper")

if __name__ == "__main__":
    run_rocknroll_scraper()
