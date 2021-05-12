from data_formatter import Formatter

if __name__ == '__main__':
    format_dir = "../../src/data/"
    data_dir = "../data/"
    cards = [
        {
            'data_files': [data_dir + 'song_data.json', data_dir + 'singalong_song.json'],
            'output_file': format_dir + 'hum_cards.json',
        },
        {
            'data_files': [data_dir + 'celebrity_data.json'],
            'output_file': format_dir + 'sideshow_cards.json'
        },
        {
            'data_files': [data_dir + 'expressions_data.json', data_dir + 'movie_data.json'],
            'output_file': format_dir + 'cloodle.json',
        },
        {
            'data_files': [data_dir + 'expressions_data.json'],
            'output_file': format_dir + 'sculptorades.json',
        },
        {
            'data_files':[data_dir + 'charades_data.json'],
            'output_file': format_dir + 'charades_cards.json'
        },
        {
            'data_files':[data_dir + 'spelling_data.json'],
            'output_file': format_dir + 'spelling_cards.json'
        },
    ]

    for card_data in cards:
        f = Formatter(card_data['data_files'], card_data['output_file'])
        f.write_cards_to_json()
