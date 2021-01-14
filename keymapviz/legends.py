# -*- coding: utf-8 -*-
import configparser

legends = {
    'XXXXXXX': '',
    '_______': '',
    'KC_TRNS': '',
    'KC_NO': '',
    'LCTL(KC_Z)': 'UNDO',
    'LCTL(KC_Y)': 'REDO',
    'LCTL(KC_C)': 'COPY',
    'LCTL(KC_V)': 'PASTE',
    'LCTL(KC_X)': 'CUT',
    'KC_PSCREEN': 'PSc',

    'MO(LOWER)': 'LOWER',
    'MO(RAISE)': 'RAISE',
    'RSFT_T(KC_ENT)': 'ET/SFT',
    'LALT(KC_TAB)': 'ALT-TAB',
    'LCTL(KC_G)': 'Ctrl-G',
    'LSFT(KC_SPACE)': 'Sft-SPC',
}

def read_config(config_file_path):
    if config_file_path:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read_file(config_file_path)
        if 'legends' in config._sections:
            config_legends = config._sections.get("legends")
            legends.update(config_legends)
    return legends