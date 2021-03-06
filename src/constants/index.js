import drawData from "../data/draw.json";
import sculptData from "../data/sculpt.json";
import draw_blindData from "../data/draw_blind.json";
import bumFlingerData from "../data/humalong.json";
import puppetData from "../data/puppet.json";
import charadesData from "../data/charades.json";
import copyData from "../data/copy.json";
import spellingData from "../data/spelling.json";
import anagramData from "../data/anagram.json";
import selecting_questData from "../data/multiple_choice.json";
import poly_gData from "../data/true_false.json";
import factMeData from "../data/fact_me.json";

export const game_types_data = {
    'creative': {
        'sculpt': sculptData,
        'draw_blind': draw_blindData,
        'draw': drawData,
    },
    'performer': {
        'humalong': bumFlingerData,
        'charades': charadesData,
        'puppet': puppetData,
        'copy': copyData
    },
    'trivia': {
        'multiple_choice': selecting_questData,
        'fact_me': factMeData,
        'true_false': poly_gData,
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
        'humalong': {
            label: 'Humalong',
            value: 'humalong',
        },
        'charades': {
            label: 'Charades',
            value: 'charades',
        },
        'puppet': {
            label: 'Puppet',
            value: 'puppet',
        },
        'copy': {
            label: 'Copy',
            value: 'copy',
        },
    },
    'trivia': {
        'true_false': {
            label: 'True or False',
            value: 'true_false',
        },
        'fact_me': {
            label: 'Fact Me',
            value: 'fact_me',
        },
        'multiple_choice': {
            label: 'Multiple Choice',
            value: 'multiple_choice',
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