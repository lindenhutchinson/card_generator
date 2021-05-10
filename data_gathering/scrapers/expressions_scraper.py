from scraper import Scraper
import re

class ExpScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file

    def get_expressions(self):
        soup = self.get_soup()
        expressions=[]
        for h5 in soup.find_all('h5'):
            text = h5.get_text()
            expr_match = re.findall(r'\d{1,3}\.(.+)', text)
            if len(expr_match) == 1:
                expr_text = expr_match[0].strip().lower().capitalize()       
                expressions.append(expr_text)

        self.write_to_json(expressions)


if __name__ == '__main__':
    url = 'https://onlineteachersuk.com/english-idioms/'
    outfile = '../data/expressions_data.json'
    es = ExpScraper(url, outfile)
    es.get_expressions()