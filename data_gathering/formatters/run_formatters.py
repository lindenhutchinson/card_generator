from data_formatter import Formatter

if __name__ == '__main__':
    h_card_data = {
        'data_files': ['../data/song_data.json', '../data/singalong_song.json'],
        'output_file': '../formatted_data/hum_cards.json',
    }
    s_card_data = {
        'data_files': ['../data/expressions_data.json', '../data/movie_data.json'],
        'output_file': '../formatted_data/creative_cat_cards.json',
    }

    for card_data in [h_card_data, s_card_data]:
        f = Formatter(card_data['data_files'], card_data['output_file'])
        f.write_cards_to_json()
