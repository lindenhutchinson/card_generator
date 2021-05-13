import cloodleData from "../data/cloodle.json";
import sculptoradesData from "../data/sculptorades.json";
import sensosketchData from "../data/sensosketch.json";
import humdingerData from "../data/humdinger.json";
import sideshowData from "../data/sideshow.json";
import cameoData from "../data/cameo.json";
import copycatData from "../data/copy_cat.json";
import spellingData from "../data/gnilleps.json";
import zelpuzData from "../data/zelpuz.json";
import selectaquestData from "../data/selectaquest.json";
import polygraphData from "../data/polygraph.json"

export const game_types_data = {
    'creative_cat': {
        'sculptorades': sculptoradesData,
        'sensosketch': sensosketchData,
        'cloodle': cloodleData,
    },
    'star_performer': {
        'humdinger': humdingerData,
        'cameo': cameoData,
        'sideshow': sideshowData,
        'copycat': copycatData
    },
    'data_head': {
        'odd_couple': selectaquestData,
        'selectaquest': selectaquestData,
        'factoid': polygraphData,
        'polygraph': polygraphData,
    },
    'word_worm': {
        'team_gnilleps': spellingData,
        'gnilleps': spellingData,
        'zelpuz': zelpuzData,
    }
}

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