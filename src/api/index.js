import cCatData from "../data/creative_cat_cards.json";
import songData from "../data/hum_cards.json";
import gameData from "../data/game_data.json";
import celebData from "../data/sideshow_cards.json";
import charadesData from "../data/charades_cards.json";
import _ from "lodash";

// TODO: use an enum of colours rather than the ridiculous mess that's going on down there
// const card_colours = {
//     'creative_cat':'blue',
//     'word_worm':'yellow darken-2',
//     'star_performer':'green',
//     'data_head':'red',
// };
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
            colour: 'blue',
        },
        'sensosketch': {
            label: 'Sensosketch',
            value: 'sensosketch',
            colour: 'blue',
        },
        'cloodle': {
            label: 'Cloodle',
            value: 'cloodle',
            colour: 'blue',
        },
    },
    'star_performer': {
        'humdinger': {
            label: 'Humdinger',
            value: 'humdinger',
            colour: 'green',
        },
        'cameo': {
            label: 'Cameo',
            value: 'cameo',
            colour: 'green',
        },
        'sideshow': {
            label: 'Sideshow',
            value: 'sideshow',
            colour: 'green',
        },
        'copycat': {
            label: 'Copycat',
            value: 'copycat',
            colour: 'green',
        },
    },
    'data_head': {
        'polygraph': {
            label: 'Polygraph',
            value: 'polygraph',
            colour: 'red',
        },
    },
    'word_worm': {
        'zelpuz': {
            label: 'Zelpuz',
            value: 'zelpuz',
            colour: 'yellow darken-2',
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
        'cameo': charadesData,
        'sideshow': charadesData,
        'copycat' : celebData
    },
    'data_head': [],
    'word_worm': [],
}

export function get_type(card_type) {
    if(card_type === 'random') {
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
    if(data) {
        const card = _.sample(data);
        card['game_info'] = g_info;
        card['game_type'] = g_type;
        card['card_type'] = {
            'value':card_type,
            'label':card_types[card_type].label
        }
        return card;
    }
    return [];
}
