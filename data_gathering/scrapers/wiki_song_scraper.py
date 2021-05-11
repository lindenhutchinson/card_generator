import requests
from bs4 import BeautifulSoup
import json
import re
from scraper import Scraper


class WikiSongScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

    def append_to_data(self, row_data):
        """
        Appends data from the table row to the object's data dictionary

        Args:
            row_data (array): A row of the wiki song table containing 7 tds 

        """
        # genre definitions and their magic numbers corresponding to their position in the table
        genres = [
            {
                'name': 'pop',
                'num': 1
            },
            {
                'name': 'hiphop',
                'num': 3
            },
            {
                'name': 'country',
                'num': 5
            },
        ]
        # regex pattern for retrieving the song and artist from the table text
        song_artist_re = re.compile(r'"(.+)"[\[\d*\]]+([\w\s]+)')
        prev_song = ''

        for genre in genres:
            text = row_data[genre['num']].get_text().strip("\n")
            song_artist = song_artist_re.findall(text)
            for s_a in song_artist:
                song = s_a[0].strip("\n").replace('\"', '')
                artist = s_a[1].strip("\n")
                if song == prev_song:
                    continue
                prev_song = song
                single = f"{song} - {artist}"

                self.data['answers'].append(single)

    def write_table_to_json(self):
        soup = self.get_soup()
        table = soup.find("table")

        for tr in table.find_all("tr"):
            td_list = tr.find_all("td")
            if len(td_list) == 7:
                self.append_to_data(td_list)

        self.write_to_json(self.data)

    def run(self):
        self.write_table_to_json()


if __name__ == "__main__":
    url = "https://en.m.wikipedia.org/wiki/List_of_Billboard_Year-End_number-one_singles_and_albums"
    scraper = WikiSongScraper(url, '../data/song_data.json')
    scraper.run()
