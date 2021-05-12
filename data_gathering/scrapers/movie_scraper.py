from scraper import Scraper
import re


class MovieScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

    def get_movies(self):
        soup = self.get_soup()
        h3_list = soup.find_all("h3", class_="lister-item-header")

        for h3 in h3_list:
            a = h3.find("a")
            self.data['answers'].append([a.get_text()])

    def run(self):
        self.data['game_text'] = "Hint: Movie"
        url = self.url
        for i in range(1, 6):
            self.url = f"{url}?page={i}"
            self.get_movies()

        self.write_to_json(self.data)


if __name__ == "__main__":
    url = "https://www.imdb.com/list/ls006266261/"
    scraper = MovieScraper(url, '../data/movie_data.json')
    scraper.run()
