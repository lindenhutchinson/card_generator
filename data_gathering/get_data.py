from tools.scrapers.anagram_scraper import run_anagram_scraper
from tools.scrapers.boolean_trivia_scraper import run_bool_trivia_scraper
from tools.scrapers.celebrity_scraper import run_celeb_scraper
from tools.scrapers.charades_scraper import run_charades_scraper
from tools.scrapers.common_mispelled_scraper import run_mispelled_scraper
from tools.scrapers.easy_spelling_scraper import run_easy_spelling_scraper
from tools.scrapers.expressions_scraper import run_expressions_scraper
from tools.scrapers.hard_spelling_scraper import run_hard_spelling_scraper
from tools.scrapers.movie_scraper import run_movie_scraper
from tools.scrapers.random_object_scraper import run_rand_object_scraper
from tools.scrapers.rock_n_roll_scraper import run_rocknroll_scraper
from tools.scrapers.singalong_song_scraper import run_singalong_scraper
from tools.scrapers.trivia_scraper import run_trivia_scraper
from tools.scrapers.wiki_song_scraper import run_wiki_song_scraper
from tools.scrapers.mc_trivia_scraper import run_mc_trivia_scraper

from tools.formatters.run_formatters import run_formatters

import threading

if __name__ == "__main__":

    scrapers = {
        'Anagram': run_anagram_scraper,
        'True or False Trivia': run_bool_trivia_scraper,
        'Celebrity': run_celeb_scraper,
        'Charades': run_charades_scraper,
        'Commonly mispelled words': run_mispelled_scraper,
        'Easy spelling words': run_easy_spelling_scraper,
        'Common expressions': run_expressions_scraper,
        'Hard spelling words': run_hard_spelling_scraper,
        'IMDB top movie list': run_movie_scraper,
        'Top 1000 rock n roll songs': run_rocknroll_scraper,
        'Random objects': run_rand_object_scraper,
        'Top singalong songs': run_singalong_scraper,
        'Trivia question': run_trivia_scraper,
        'Wikipedia top song list': run_wiki_song_scraper,
        'Multiple choice trivia questions': run_mc_trivia_scraper,
    }

    threads = []

    print("Running scrapers, this can take a while...")
    for name in scrapers.keys():
        t=threading.Thread(target=scrapers[name])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
    print("Finished scraping - formatting data")
    run_formatters()
