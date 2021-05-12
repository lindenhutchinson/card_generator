from scraper import Scraper
import re


class CharadesScraper(Scraper):
    def __init__(self, url, output_file):
        self.url = url
        self.output_file = output_file
        self.data = {
            'game_text': '',
            'answers': []
        }
        self.data_list = []

    def get_charades(self):
        soup = self.get_soup()
        h2_list = soup.find_all("h2")
        for h2 in h2_list:
            charade_ideas = []
            hint = h2.get_text()
            if 'Emoji' in hint:
                continue

            found_sib = False
            for sib in h2.next_siblings:
                if hasattr(sib, 'contents'):
                    li_list = sib.contents
                    for li in li_list:
                        matches = re.findall(r'<li>([-\w\s]+)<\/li>', str(li))
                        if len(matches) == 1:
                            charade_ideas.append([matches[0]])
                            found_sib = True
                if found_sib:
                    break
                            

            if len(charade_ideas):
                hint_text = hint.split(' ')
                if 'Charades' == hint_text[0]:
                    game_text = 'Adult'
                elif 'BONUS' in hint_text[0]:
                    game_text = 'Coronavirus'
                else:
                    game_text = hint_text[0]

                self.data_list.append({
                    'game_text': f"Hint: {game_text}",
                    'answers': charade_ideas
                })
                charade_ideas = []

    def run(self):
        self.get_charades()
        self.write_to_json(self.data_list)


if __name__ == "__main__":
    url = "https://psycatgames.com/magazine/party-games/charades-ideas/"
    scraper = CharadesScraper(url, '../data/charades_data.json')
    scraper.run()
