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

config = configparser.ConfigParser()
props = config.read('/home/daan/legends.properties')
propsLegends = config['legends']

print("legends: ")
print(legends.values())
print("props: ")
print(propsLegends)

for key in propsLegends:
    legends.update()
#legend = {'ESC': 'bla'}
#legends.update(legend)
