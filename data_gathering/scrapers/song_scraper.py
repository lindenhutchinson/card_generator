import requests
from bs4 import BeautifulSoup
import json
import re
from scraper import Scraper


class WikiSongScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def append_to_song_data(self, row_data, song_data):
        """
        Appends data from the table row to the passed song_data array and returns it back

        Args:
            row_data (array): A row of the wiki song table containing 7 tds 
            song_data (array): An array of song_artist dictionaries {song: string, artist: string}

        Returns:
            song_data (array): The same array but with the relevent song_artist data from the row appended

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
                # some necessary cleaning as the encoding leaves dirty strings on our data
                song = s_a[0].strip("\n").replace('\"', '').replace(
                    '\u2013', '-').replace('\u00e9', 'e')
                artist = s_a[1].strip("\n").replace('\u00e9', 'e')
                if song == prev_song:
                    continue
                prev_song = song
                single = {
                    'artist': artist,
                    'song': song
                }

                song_data.append(single)

        return song_data

    def write_table_to_json(self):
        '''


        '''
        soup = self.get_soup()
        table = soup.find("table")
        song_data = []
        for tr in table.find_all("tr"):
            td_list = tr.find_all("td")
            if len(td_list) == 7:
                song_data = self.append_to_song_data(td_list, song_data)

        self.write_to_json(song_data)


if __name__ == "__main__":
    url = "https://en.m.wikipedia.org/wiki/List_of_Billboard_Year-End_number-one_singles_and_albums"
    scraper = WikiSongScraper(url, '../data/song_data.json')
    scraper.write_table_to_json()
