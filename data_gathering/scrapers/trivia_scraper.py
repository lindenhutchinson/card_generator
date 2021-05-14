from scraper import Scraper
import requests
import random
import numpy as np
import json
from urllib.parse import unquote
import os


class TriviaScraper(Scraper):
    def __init__(self, output_file, url_list):
        self.output_file = output_file
        self.data = {
            'game_text': [],
            'answers': []
        }
        self.url_list = url_list

    def get_data_from_api(self, url):
        data = []
        trivia_data = json.loads(requests.get(url).content)

        for td in trivia_data['results']:
            answer = unquote(td['correct_answer'])
            game_text = unquote(td['question'])

            if 'the following' in game_text:
                continue

            data.append({
                'answers': [answer],
                'game_text': game_text
            })

        return data

    def run(self):
        data = []
        for i, url in enumerate(self.url_list):
            self.print_progress(i, len(self.url_list))
            data = np.concatenate((data, self.get_data_from_api(url))).tolist()

        self.write_to_json(data)


if __name__ == "__main__":
    token = json.loads(requests.get(
        'https://opentdb.com/api_token.php?command=request').content)
    urls = [
        f"https://opentdb.com/api.php?amount=50&difficulty=easy&type=multiple&encode=url3986&token={token['token']}" for _ in range(50)]

    scraper = TriviaScraper('../data/trivia_data.json', urls)
    scraper.run()
