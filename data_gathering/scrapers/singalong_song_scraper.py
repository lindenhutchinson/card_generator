from scraper import Scraper
import re
import os
import sys

class SingalongSongScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def get_songs(self):
        soup = self.get_soup()
        pattern = r"“(.+)”[–\s]+(.+)"
        li_list = soup.find(class_="entry-content").find_all("li")
        song_data = []
        for li in li_list:
            text = li.get_text()
            matches = re.findall(pattern, text)
            if len(matches) == 1:
                song_data.append(f"{matches[0][0]} - {matches[0][1]}")

        self.write_to_json(song_data)


if __name__ == "__main__":
    url = "https://takelessons.com/blog/best-songs-to-sing-along-to"
    scraper = SingalongSongScraper(url, '../data/singalong_song.json')
    scraper.get_songs()