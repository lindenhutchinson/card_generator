from formatter import Formatter


class HumgdingerFormatter(Formatter):
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.card_game = 'Humdinger'
        self.game_info = 'This humdinger blah blah blah hum a song'
        self.game_text = ''
        self.answers = ''

    def get_answers_text(self):
        card_data = self.load_json_data()
        return [f"{c['song']} - {c['artist']}" for c in card_data]

    def get_cards_list(self):
        cards = []
        for a in self.get_answers_text():
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
    hf = HumgdingerFormatter('../data/song_data.json', '../data/song_cards.json')
    hf.write_cards_to_json()
