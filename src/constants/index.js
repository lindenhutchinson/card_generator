import drawData from "../data/draw.json";
import sculptData from "../data/sculpt.json";
import draw_blindData from "../data/draw_blind.json";
import bum_flingerData from "../data/bum_flinger.json";
import puppetData from "../data/puppet.json";
import charadesData from "../data/charades.json";
import copierData from "../data/copier.json";
import spellingData from "../data/spelling.json";
import anagramData from "../data/anagram.json";
import selecting_questData from "../data/selecting_quest.json";
import poly_gData from "../data/poly_g.json"

export const game_types_data = {
    'creative': {
        'sculpt': sculptData,
        'draw_blind': draw_blindData,
        'draw': drawData,
    },
    'performer': {
        'bum_flinger': bum_flingerData,
        'charades': charadesData,
        'puppet': puppetData,
        'copier': copierData
    },
    'trivia': {
        'odd_bunch': selecting_questData,
        'selecting_quest': selecting_questData,
        'fact_me': poly_gData,
        'poly_g': poly_gData,
    },
    'words': {
        'team_spelling': spellingData,
        'spelling': spellingData,
        'anagram': anagramData,
    }
}

export const card_types = {
    creative: {
        label: 'Creative',
        value: 'creative',
        colour: 'blue',
    },
    words: {
        label: 'Words',
        value: 'words',
        colour: 'yellow darken-2',
    },
    performer: {
        label: 'Performer',
        value: 'performer',
        colour: 'green',
    },
    trivia: {
        label: 'Trivia',
        value: 'trivia',
        colour: 'red',
    },
}
export const game_types = {
    'creative': {
        'sculpt': {
            label: 'Sculpt',
            value: 'sculpt',
        },
        'draw_blind': {
            label: 'Draw Blind',
            value: 'draw_blind',
        },
        'draw': {
            label: 'Draw',
            value: 'draw',
        },
    },
    'performer': {
        'bum_flinger': {
            label: 'Bum Flinger',
            value: 'bum_flinger',
        },
        'charades': {
            label: 'Charades',
            value: 'charades',
        },
        'puppet': {
            label: 'Puppet',
            value: 'puppet',
        },
        'copier': {
            label: 'Copier',
            value: 'copier',
        },
    },
    'trivia': {
        'poly_g': {
            label: 'Poly G',
            value: 'poly_g',
        },
        'odd_bunch': {
            label: 'Odd Bunch',
            value: 'odd_bunch',
        },
        'fact_me': {
            label: 'Fact Me',
            value: 'fact_me',
        },
        'selecting_quest': {
            label: 'Selecting Quest',
            value: 'selecting_quest',
        },
    },
    'words': {
        'anagram': {
            label: 'Anagram',
            value: 'anagram',
        },
        'team_spelling': {
            label: 'Team Spelling',
            value: 'team_spelling',
        },
        'spelling': {
            label: 'Spelling',
            value: 'spelling',
        },
    },
}