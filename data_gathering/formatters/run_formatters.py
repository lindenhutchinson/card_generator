from data_formatter import Formatter

if __name__ == '__main__':
    cards = [
        {
            'data_files': ['../data/song_data.json', '../data/singalong_song.json'],
            'output_file': '../formatted_data/hum_cards.json',
        },
        {
            'data_files': ['../data/celebrity_data.json'],
            'output_file': '../formatted_data/sideshow_cards.json'
        },
        {
            'data_files': ['../data/expressions_data.json', '../data/movie_data.json'],
            'output_file': '../formatted_data/cloodle.json',
        },
        {
            'data_files': ['../data/expressions_data.json'],
            'output_file': '../formatted_data/sculptorades.json',
        },
        {
            'data_files':['../data/charades_data.json'],
            'output_file': '../formatted_data/charades_cards.json'
        },
    ]

    for card_data in cards:
        f = Formatter(card_data['data_files'], card_data['output_file'])
        f.write_cards_to_json()
