import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from utils.common import Common 

class Formatter(Common):
    def __init__(self, input_files, output_file):
        self.input_files = input_files
        self.output_file = output_file
        self.game_text = ''
        self.answers = ''

    def get_cards_list(self):
        cards = []
        for fn in self.input_files:
            json_data = self.load_json_data(fn)

            for a in json_data['answers']:
                card = {
                    'game_text': json_data['game_text'],
                    'answer': a
                }
                cards.append(card)

        return cards

    def write_cards_to_json(self):
        cards = self.get_cards_list()
        self.write_to_json(cards)

