import cloodleData from "../data/cloodle.json";
import songData from "../data/hum_cards.json";
import gameData from "../data/game_data.json";
import celebData from "../data/sideshow_cards.json";
import charadesData from "../data/charades_cards.json";
import spellingData from "../data/spelling_cards.json";

import _ from "lodash";

export const card_types = {
    creative_cat: {
        label: 'Creative Cat',
        value: 'creative_cat',
        colour: 'blue',
    },
    word_worm: {
        label: 'Word Worm',
        value: 'word_worm',
        colour: 'yellow darken-2',
    },
    star_performer: {
        label: 'Star Performer',
        value: 'star_performer',
        colour: 'green',
    },
    data_head: {
        label: 'Data Head',
        value: 'data_head',
        colour: 'red',
    },
}
export const game_types = {
    'creative_cat': {
        'sculptorades': {
            label: 'Sculptorades',
            value: 'sculptorades',
        },
        'sensosketch': {
            label: 'Sensosketch',
            value: 'sensosketch',
        },
        'cloodle': {
            label: 'Cloodle',
            value: 'cloodle',
        },
    },
    'star_performer': {
        'humdinger': {
            label: 'Humdinger',
            value: 'humdinger',
        },
        'cameo': {
            label: 'Cameo',
            value: 'cameo',
        },
        'sideshow': {
            label: 'Sideshow',
            value: 'sideshow',
        },
        'copycat': {
            label: 'Copycat',
            value: 'copycat',
        },
    },
    'data_head': {
        'polygraph': {
            label: 'Polygraph',
            value: 'polygraph',
        },
        'odd_couple': {
            label: 'Odd Couple',
            value: 'odd_couple',
        },
        'factoid': {
            label: 'Factoid',
            value: 'factoid',
        },
        'selectaquest': {
            label: 'Selectaquest',
            value: 'selectaquest',
        },
    },
    'word_worm': {
        'zelpuz': {
            label: 'Zelpuz',
            value: 'zelpuz',
        },
        'team_gnilleps': {
            label: 'Team Gnilleps',
            value: 'team_gnilleps',
        },
        'gnilleps': {
            label: 'Gnilleps',
            value: 'gnilleps',
        },
    },
}
const game_types_data = {
    'creative_cat': {
        'sculptorades': cloodleData,
        'sensosketch': cloodleData,
        'cloodle': cloodleData,
    },
    'star_performer': {
        'humdinger': songData,
        'cameo': charadesData,
        'sideshow': charadesData,
        'copycat': celebData
    },
    'data_head': {
        'odd_couple': songData,
        'selectaquest': songData,
        'factoid': songData,
        'polygraph': songData,
    },
    'word_worm': {
        'team_gnilleps': spellingData,
        'gnilleps': spellingData,
        'zelpuz': spellingData,
    }
}
function get_sorted_obj(obj) {
    var keys = Object.keys(obj);
    keys.sort();
    var sorted = {};
    for (let k of keys) { sorted[k] = obj[k]; }
    return sorted;
}
export function get_card_types() {  
    return get_sorted_obj(card_types);
}

export function get_game_types() {
    var sorted = get_sorted_obj(game_types);
    for (let type of Object.keys(game_types)) {
        sorted[type] = get_sorted_obj(sorted[type])
    }
    return sorted;
}

export function get_type(card_type) {
    if (card_type === 'random') {
        return {
            label: 'Random',
            value: 'random',
            colour: 'purple',
        }
    }
    return card_types[card_type];
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
    if (data) {
        const card = _.sample(data);
        card['game_info'] = g_info;
        card['game_type'] = g_type;
        card['card_type'] = {
            'value': card_type,
            'label': card_types[card_type].label
        }
        return card;
    }
    return [];
}
