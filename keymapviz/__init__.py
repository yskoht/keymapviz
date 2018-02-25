# -*- coding: utf-8 -*-

import io
import os
import sys
import json

import regex as re

import keymapviz.ergodox
import keymapviz.lets_split


KEYBOARDS = {
    'ergodox': keymapviz.ergodox,
    'ergodox_ez': keymapviz.ergodox,
    'lets_split': keymapviz.lets_split
}


class Keymapviz():
    def __init__(self, keyboard, keymap_c, legends = None):
        self.keyboard = KEYBOARDS[keyboard]
        self.keymaps = self.__parse_keymap_c(keymap_c)
        self.legends = legends if legends else {}


    def __parse_keymap_c(self, keymap_c):
        src = [_ for _ in keymap_c]
        src = [re.sub(r'\s*//.*$', '', _) for _ in src]  # remove line comment
        src = [_.rstrip() for _ in src]                  # remove CRLF
        src = ''.join(src)
        src = re.sub(r'/\*.*?\*/', '', src)              # remove block comment
        src = re.sub(r'\s', '', src)                     # remove space
        src = re.sub(r'\\', '', src)                     # remove backslash

        keymap_regexp = re.compile(
            self.keyboard.keymap_keyword + r'(?<rec>\((?:[^()]|(?&rec))*\))'
        )
        keycode_regexp = re.compile(
            r'\s*(\w+(?<rec>\((?:[^()]|(?&rec))*\))*)\s*,?'
        )
        keymaps = keymap_regexp.findall(src)
        keymaps = [_.lstrip('(').rstrip(')') for _ in keymaps]
        keymaps = [[__[0] for __ in keycode_regexp.findall(_)] for _ in keymaps]
        return keymaps


    def __parse_ascii_art(self, aa):
        regexp = re.compile(r'{.*?}')
        matches = regexp.findall(aa)
        for i, match in enumerate(matches):
            s = match.lstrip('{').rstrip('}').strip()
            n = int(s) if s.isdigit() else i
            len_ = len(match)
            aa = aa.replace(match, '{{{0}:^{1}.{1}}}'.format(n, len_), 1)
        return aa


    def __legends(self, keymap):
        return [self.legends.get(_, re.sub(r'^KC_', '', _)) for _ in keymap]


    def __json_format(self, json_, keymap):
        legends = self.__legends(keymap)
        ret = [[_.format(*legends) if isinstance(_, str) else _ for _ in __]
               for __ in json_]
        with io.StringIO() as sio:
            json.dump(ret, sio, indent=4)
            ret_str = sio.getvalue()
        return ret_str


    def ascii_art(self):
        aa = self.__parse_ascii_art(self.keyboard.ascii_art)
        return [aa.format(*self.__legends(_)) for _ in self.keymaps]


    def layout_editor_json(self):
        path_ = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_, self.keyboard.layout_editor_json)) as f:
            json_ = json.load(f)
        return [self.__json_format(json_, _) for _ in self.keymaps]

