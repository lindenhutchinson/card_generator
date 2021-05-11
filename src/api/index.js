import cCatData from "../data/creative_cat_cards.json";
import songData from "../data/hum_cards.json";
import gameData from "../data/game_data.json";

import _ from "lodash";

export const card_types = {
    creative_cat: {
        label: 'Creative Cat',
        value: 'creative_cat',
        colour: 'blue darken-3',
    },
    word_worm: {
        label: 'Word Worm',
        value: 'word_worm',
        colour: 'yellow darken-3',
    },
    star_performer: {
        label: 'Star Performer',
        value: 'star_performer',
        colour: 'green darken-3',
    },
    data_head: {
        label: 'Data Head',
        value: 'data_head',
        colour: 'red darken-3',
    },
}
export const game_types = {
    'creative_cat': {
        'sculptorades': {
            label: 'Sculptorades',
            value: 'sculptorades',
            colour: 'blue darken-3',
        },
        'sensosketch': {
            label: 'Sensosketch',
            value: 'sensosketch',
            colour: 'blue darken-3',
        },
        'cloodle': {
            label: 'Cloodle',
            value: 'cloodle',
            colour: 'blue darken-3',
        },
    },
    'star_performer': {
        'humdinger': {
            label: 'Humdinger',
            value: 'humdinger',
            colour: 'green darken-3',
        },
        'cameo': {
            label: 'Cameo',
            value: 'cameo',
            colour: 'green darken-3',
        },
        'sideshow': {
            label: 'Sideshow',
            value: 'sideshow',
            colour: 'green darken-3',
        },
    },
    'data_head': {
        'polygraph': {
            label: 'Polygraph',
            value: 'polygraph',
            colour: 'red darken-3',
        },
    },
    'word_worm': {
        'zelpuz': {
            label: 'Zelpuz',
            value: 'zelpuz',
            colour: 'yellow darken-3',
        },
    },
}
const game_types_data = {
    'creative_cat': {
        'sculptorades': cCatData,
        'sensosketch': cCatData,
        'cloodle': cCatData,
    },
    'star_performer': {
        'humdinger': songData,
        'cameo': '',
        'sideshow': '',
    },
    'data_head': [],
    'word_worm': [],
}

export function get_random_card(card_type, game_type) {
    if (card_type === 'random') {
        card_type = _.sample(card_types).value;
    }
    if (game_type === 'random') {
        game_type = _.sample(game_types[card_type]).value;
    }
    const data = game_types_data[card_type][game_type];
    const g_type = gameData[card_type][game_type]["game_type"];
    const g_info = gameData[card_type][game_type]["game_info"];
    if(data) {
        const card = _.sample(data);
        card['game_info'] = g_info;
        card['game_type'] = g_type;
        return card;
    }
    return [];
}
