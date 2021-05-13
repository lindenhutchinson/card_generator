from data_formatter import Formatter

if __name__ == '__main__':
    format_dir = "../../src/data/"
    data_dir = "../data/"
    cards = [
        # CREATIVE CAT
        {
            'data_files': [data_dir + 'expressions_data.json'],
            'output_file': format_dir + 'cloodle.json',
        },
        {
            'data_files': [data_dir + 'expressions_data.json'],
            'output_file': format_dir + 'sensosketch.json',
        },
        {
            'data_files': [data_dir + 'expressions_data.json'],
            'output_file': format_dir + 'sculptorades.json',
        },
        # STAR PERFORMER
        {
            'data_files': [data_dir + 'song_data.json', data_dir + 'singalong_song.json'],
            'output_file': format_dir + 'humdinger.json',
        },
        {
            'data_files': [data_dir + 'celebrity_data.json'],
            'output_file': format_dir + 'copy_cat.json'
        },
        {
            'data_files': [data_dir + 'charades_data.json'],
            'output_file': format_dir + 'cameo.json'
        },
        {
            'data_files': [data_dir + 'celebrity_data.json'],
            'output_file': format_dir + 'sideshow.json'
        },
        # WORD WORM
        {
            'data_files': [data_dir + 'spelling_data.json'],
            'output_file': format_dir + 'gnilleps.json'
        },
        # DATA HEAD
        {
            'data_files': [data_dir + 'mc_trivia_data.json'],
            'output_file': format_dir + 'selectaquest.json'
        },
        {
            'data_files': [data_dir + 'bool_trivia_data.json'],
            'output_file': format_dir + 'polygraph.json'
        },
    ]

    for card_data in cards:
        f = Formatter(card_data['data_files'], card_data['output_file'])
        f.write_cards_to_json()
