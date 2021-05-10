import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from utils.common import Common 

class SculptFormatter(Common):
    def __init__(self, card_game, game_info, input_files, output_file):
        self.input_files = input_files
        self.output_file = output_file
        self.card_game = card_game
        self.game_info = game_info
        self.game_text = 'HINT: Expression'
        self.answers = ''

    def get_cards_list(self):
        cards = []
        for fn in self.input_files:
            answers = self.load_json_data(fn)

            for a in answers:
                card = {
                    'card_game': self.card_game,
                    'game_info': self.game_info,
                    'game_text': self.game_text,
                    'answer': a
                }
                cards.append(card)

        return cards

    def write_cards_to_json(self):
        cards = self.get_cards_list()
        self.write_to_json(cards)


if __name__ == '__main__':
    hf = SculptFormatter('Sculptorades', 'To win this sculptorades, sculpt an expression and have your team guess it', ['../data/expressions_data.json'], '../formatted_data/sculpt_cards.json')
    hf.write_cards_to_json()
