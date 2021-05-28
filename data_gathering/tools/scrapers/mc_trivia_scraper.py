from .scraper import Scraper
import requests
import random
import numpy as np
import json
from urllib.parse import unquote


class MultipleChoiceScraper(Scraper):
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
            answers = [ans for ans in td['incorrect_answers']]
            answers.append(td['correct_answer'])
            random.shuffle(answers)
            correct_answer = ''
            f_answers = []
            for i, ans in enumerate(answers):
                answer = unquote(ans)
                answer = f"{chr(65+i)}: {answer}"

                f_answers.append(answer)
                if i == answers.index(td['correct_answer']):
                    correct_answer = answer

            game_text = [unquote(td['question'])]
            game_text = np.concatenate((game_text, f_answers)).tolist()
            data.append({
                'answers': [correct_answer],
                'game_text': game_text
            })

        return data

    def run(self):
        data = []
        for i, url in enumerate(self.url_list):
            # self.print_progress(i, len(self.url_list))
            data = np.concatenate((data, self.get_data_from_api(url))).tolist()

        self.write_to_json(data)


def run_mc_trivia_scraper():
    token = json.loads(requests.get(
        'https://opentdb.com/api_token.php?command=request').content)
    urls = [
        f"https://opentdb.com/api.php?amount=50&type=multiple&encode=url3986&token={token['token']}" for _ in range(10)]

    scraper = MultipleChoiceScraper('../data/mc_trivia_data.json', urls)
    scraper.run()
    print("finished multiple choice trivia scraper")

if __name__ == "__main__":
    run_mc_trivia_scraper()