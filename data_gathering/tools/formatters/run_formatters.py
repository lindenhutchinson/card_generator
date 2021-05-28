from .data_formatter import Formatter


def run_formatters():
    format_dir = "../../../src/data/"
    data_dir = "../data/"
    cards = [
        # CREATIVE CAT
        {
            'data_files': [data_dir + 'expressions_data.json', data_dir+'object_data.json'],
            'output_file': format_dir + 'draw.json',
        },
        {
            'data_files': [data_dir + 'expressions_data.json', data_dir+'object_data.json'],
            'output_file': format_dir + 'draw_blind.json',
        },
        {
            'data_files': [data_dir + 'expressions_data.json', data_dir+'object_data.json'],
            'output_file': format_dir + 'sculpt.json',
        },
        # STAR PERFORMER
        {
            'data_files': [data_dir + 'song_data.json', data_dir + 'singalong_song.json', data_dir+'rocknroll_data.json'],
            'output_file': format_dir + 'humalong.json',
        },
        {
            'data_files': [data_dir + 'celebrity_data.json'],
            'output_file': format_dir + 'copy.json'
        },
        {
            'data_files': [data_dir + 'charades_data.json'],
            'output_file': format_dir + 'charades.json'
        },
        {
            'data_files': [data_dir + 'celebrity_data.json'],
            'output_file': format_dir + 'puppet.json'
        },
        # WORD WORM
        {
            'data_files': [data_dir + 'spelling_data.json'],
            'output_file': format_dir + 'spelling.json'
        },
        # DATA HEAD
        {
            'data_files': [data_dir + 'mc_trivia_data.json'],
            'output_file': format_dir + 'multiple_choice.json'
        },
        {
            'data_files': [data_dir + 'bool_trivia_data.json'],
            'output_file': format_dir + 'true_false.json'
        },
        {
            'data_files': [data_dir + 'trivia_data.json'],
            'output_file': format_dir + 'fact_me.json'
        },
    ]

    for card_data in cards:
        f = Formatter(card_data['data_files'], card_data['output_file'])
        f.write_cards_to_json()


if __name__ == '__main__':
    run_formatters()