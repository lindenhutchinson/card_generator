from .scraper import Scraper
import re


class ExpScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }

    def get_expressions(self):
        soup = self.get_soup()
        for h5 in soup.find_all('h5'):
            text = h5.get_text()
            expr_match = re.findall(r'\d{1,3}\.(.+)', text)
            if len(expr_match) == 1:
                expr_text = expr_match[0].strip().lower().capitalize()
                self.data['answers'].append([expr_text])

        self.data['game_text'] = 'Hint: Expression'
        self.write_to_json(self.data)

    def run(self):
        self.get_expressions()

def run_expressions_scraper():
    url = 'https://onlineteachersuk.com/english-idioms/'
    es = ExpScraper(url, '../data/expressions_data.json')
    es.run()
    print("finished expressions scraper")

if __name__ == '__main__':
    run_expressions_scraper()
