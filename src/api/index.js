import { game_types, card_types, game_types_data } from "../constants";
import gameData from "../constants/game_data.json";
import _ from "lodash";


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

function get_game_types_data(card_type, game_type) {
    return game_types_data[card_type][game_type];
}
function get_game_data(card_type, game_type) {
    return gameData[card_type][game_type]
}
export function get_random_card(card_type, game_type) {
    if (card_type === 'random') {
        card_type = _.sample(card_types).value;
    }
    if (game_type === 'random') {
        game_type = _.sample(game_types[card_type]).value;
    }
    const game_types_data = get_game_types_data(card_type, game_type)
    const game_data = get_game_data(card_type, game_type);

    if (game_types_data) {
        const card = _.sample(game_types_data);
        card['game_info'] = game_data["game_info"];
        card['game_type'] = game_data["game_type"];
        card['card_type'] = {
            'value': card_type,
            'label': card_types[card_type].label
        }
        return card;
    }
    return [];
}
