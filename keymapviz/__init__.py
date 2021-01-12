# -*- coding: utf-8 -*-

import io
import os
import sys
import json

import regex as re

import keymapviz.keyboards.crkbd
import keymapviz.keyboards.ergo42
import keymapviz.keyboards.ergodash
import keymapviz.keyboards.ergodox
import keymapviz.keyboards.fortitude60
import keymapviz.keyboards.lets_split
import keymapviz.keyboards.kinesis
import keymapviz.keyboards.helix
import keymapviz.keyboards.mint60
import keymapviz.keyboards.kaishi65
import keymapviz.keyboards.kyria


KEYBOARDS = {
    'crkbd': keymapviz.keyboards.crkbd,
    'ergo42': keymapviz.keyboards.ergo42,
    'ergodash': keymapviz.keyboards.ergodash,
    'ergodone': keymapviz.keyboards.ergodox,
    'ergodox': keymapviz.keyboards.ergodox,
    'ergodox_ez': keymapviz.keyboards.ergodox,
    'fortitude60': keymapviz.keyboards.fortitude60,
    'helix': keymapviz.keyboards.helix,
    'kinesis': keymapviz.keyboards.kinesis,
    'lets_split': keymapviz.keyboards.lets_split,
    'mint60': keymapviz.keyboards.mint60,
    'kaishi65': keymapviz.keyboards.kaishi65,
    'kyria': keymapviz.keyboards.kyria
}


class Keymapviz():
    def __init__(self, keyboard, keymap_c, legends = None):
        self.__keymap_c = keymap_c.read()
        self.keyboard = KEYBOARDS[keyboard]
        self.keymaps = self.__parse_keymap_c()
        self.legends = legends if legends else {}


    def __parse_keymap_c(self):
        src = self.__keymap_c.split('\n')
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
        return aa.lstrip().rstrip()


    def __legends(self, keymap):
        return [self.legends.get(_, re.sub(r'^KC_', '', _)) for _ in keymap] + [''] * 100  # FIXME :_(


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
        self.__ascii_art = [aa.format(*self.__legends(_)) for _ in self.keymaps]
        return self.__ascii_art


    def layout_editor_json(self):
        path_ = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_, self.keyboard.layout_editor_json)) as f:
            json_ = json.load(f)
        return [self.__json_format(json_, _) for _ in self.keymaps]


    def keymap_c(self):
        class Repl():
            def __init__(self, list_):
                self.__list = list_
                self.__gen  = self.__generator()

            def __generator(self):
                for _ in self.__list:
                    yield _

            def next(self, matchobj):
                try:
                    ret = next(self.__gen)
                except StopIteration:
                    ret = matchobj[0]
                return ret

        pattern = r'^[ \t\r\f\v]*?/\*((?!\*/).)*?\[keymapviz\].*?\*/\s*?$'
        repl = Repl(self.__ascii_art)
        kc = re.sub(pattern, repl.next, self.__keymap_c, flags=re.MULTILINE|re.DOTALL)
        return kc
