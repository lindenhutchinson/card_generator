from .scraper import Scraper
import requests
import random
import numpy as np
import json
from urllib.parse import unquote
import os


class ObjectScraper(Scraper):
    def __init__(self, output_file, url='',url_list=[]):
        self.output_file = output_file
        self.data = {
            'game_text': [],
            'answers': []
        }
        self.url = url
        self.url_list = url_list

    def get_data_from_api(self, url):
        data = []
        seen_objects = []

        for i in range(10):
            # self.print_progress(i, 10)
            object_data = json.loads(requests.get(url).content)
            for odata in object_data['data']:
                answer = unquote(odata['name'])
                if answer in seen_objects:
                    continue
                seen_objects.append(answer)
                game_text = 'Hint: Object/Animal'

                data.append({
                    'answers': [answer],
                    'game_text': game_text
                })
        # print(len(data))
        return data

    def run(self):
        data = self.get_data_from_api(self.url)

        self.write_to_json(data)


def run_rand_object_scraper():
    url = 'https://story-shack-cdn.glitch.me/generators/random-object-generator?count=100'
    scraper = ObjectScraper('../data/object_data.json', url=url)
    scraper.run()
    print("finished random object scraper")

if __name__ == "__main__":
    run_rand_object_scraper()