import os
import sys

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir)
from utils.common import Common 

class Formatter(Common):
    def __init__(self, card_game, game_info, input_files, output_file):
        self.input_files = input_files
        self.output_file = output_file
        self.card_game = card_game
        self.game_info = game_info
        self.game_text = ''
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
    hf = Formatter('Humdinger', 'This humdinger blah blah blah hum a song', ['../data/song_data.json', '../data/singalong_song.json'], '../formatted_data/song_cards.json')
    hf.write_cards_to_json()
