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
import keymapviz.keyboards.lily58
import keymapviz.keyboards.sweet16
import keymapviz.keyboards.dactyl_manuform5x6


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
    'lily58': keymapviz.keyboards.lily58,
    'mint60': keymapviz.keyboards.mint60,
    'kaishi65': keymapviz.keyboards.kaishi65,
    'kyria': keymapviz.keyboards.kyria,
    'sweet16': keymapviz.keyboards.sweet16,
    'dactyl_manuform5x6': keymapviz.keyboards.dactyl_manuform5x6,
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


    def __get_final_ascii_art(self, ascii_art):
        aa = self.__parse_ascii_art(ascii_art)
        self.__ascii_art = [aa.format(*self.__legends(_)) for _ in self.keymaps]
        return self.__ascii_art

    def ascii_art(self):
        return self.__get_final_ascii_art(self.keyboard.ascii_art)


    def layout_editor_json(self):
        path_ = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(path_, self.keyboard.layout_editor_json)) as f:
            json_ = json.load(f)
        return [self.__json_format(json_, _) for _ in self.keymaps]

    __non_outline_chars = '*{} 0123456789'

    def __get_box_drawing(self, left, down, up, right, center):
        horizontal_ascii_chars = '-=_~'
        corner_ascii_chars = '\'.,`'
        # The usecase for this verification is to avoid linking the thumb cluster with the alpha cluster
        # if the bottom edge of the alpha cluster is on one line and the top edge of the thumb cluster is on the next line.
        if center in horizontal_ascii_chars+corner_ascii_chars and down in horizontal_ascii_chars+corner_ascii_chars:
            down = ' '
        if center in horizontal_ascii_chars+corner_ascii_chars and up in horizontal_ascii_chars+corner_ascii_chars:
            up = ' '
        ldur = tuple(map(lambda c: c not in self.__non_outline_chars, (left, down, up, right)))
        box_drawing_table = {
            (0, 0, 0, 0): ' ', # SPACE
            (0, 0, 0, 1): '╶', # BOX DRAWINGS LIGHT RIGHT
            (0, 0, 1, 0): '╵', # BOX DRAWINGS LIGHT UP
            (0, 0, 1, 1): '└', # BOX DRAWINGS LIGHT UP AND RIGHT
            (0, 1, 0, 0): '╷', # BOX DRAWINGS LIGHT DOWN
            (0, 1, 0, 1): '┌', # BOX DRAWINGS LIGHT DOWN AND RIGHT
            (0, 1, 1, 0): '│', # BOX DRAWINGS LIGHT VERTICAL
            (0, 1, 1, 1): '├', # BOX DRAWINGS LIGHT VERTICAL AND RIGHT
            (1, 0, 0, 0): '╴', # BOX DRAWINGS LIGHT LEFT
            (1, 0, 0, 1): '─', # BOX DRAWINGS LIGHT HORIZONTAL
            (1, 0, 1, 0): '┘', # BOX DRAWINGS LIGHT UP AND LEFT
            (1, 0, 1, 1): '┴', # BOX DRAWINGS LIGHT UP AND HORIZONTAL
            (1, 1, 0, 0): '┐', # BOX DRAWINGS LIGHT DOWN AND LEFT
            (1, 1, 0, 1): '┬', # BOX DRAWINGS LIGHT DOWN AND HORIZONTAL
            (1, 1, 1, 0): '┤', # BOX DRAWINGS LIGHT VERTICAL AND LEFT
            (1, 1, 1, 1): '┼', # BOX DRAWINGS LIGHT VERTICAL AND HORIZONTAL
            }
        return box_drawing_table[ldur]

    def fancy_art(self):
        if hasattr(self.keyboard, 'fancy_ascii_art'):
            # There already exists a man-made fancy ascii art for this keyboard.
            return self.__get_final_ascii_art(self.keyboard.fancy_ascii_art)
        aa = self.keyboard.ascii_art
        keymapviz_signature_pattern = r'[A-Za-z ]*\[keymapviz\].*\*/\s*$'
        # If the keymapviz signature is adjacent to certain outline characters,
        # self.__get_box_drawing will incorrectly interpret the characters composing the signature
        # as other outline characters and will attempt to link them together, which is undesired.
        # To bypass this issue, the signature is temporarily replaced with an arbitrary placeholder composed of
        # "illegal" outline characters (see __non_outline_chars) that is unlikely to appear in the source ascii art.
        kmvz_signature = re.search(keymapviz_signature_pattern, aa, flags=re.MULTILINE|re.DOTALL).group(0)
        kmvz_signature_placeholder = '}* *{'
        aa = re.sub(keymapviz_signature_pattern, kmvz_signature_placeholder, aa, flags=re.MULTILINE|re.DOTALL)
        aa_lines = aa.splitlines()
        line_count = len(aa_lines)
        max_line_len = max(map(lambda line: len(line), aa_lines))
        fa_matrix = list(map(lambda line: list(line.ljust(max_line_len)), aa_lines))
        aa_matrix = list(map(lambda line: list(line.ljust(max_line_len)), aa_lines))
        # Adding an empty line at the top and bottom of fa_matrix to avoid complicated code
        # correctly handling IndexErrors when assigning down and up in the loop.
        fa_matrix = [[' '] * max_line_len] + fa_matrix + [[' '] * max_line_len]
        aa_matrix = [[' '] * max_line_len] + aa_matrix + [[' '] * max_line_len]
        # Starting on row 1 because row 0 is filled with empty space chars.
        for i in range(1, line_count):
            # The first two chars of each line are ' *' (C block comment)
            # so we can ignore them.
            for j in range(2, max_line_len):
                left   = aa_matrix[i][j-1]
                down   = aa_matrix[i+1][j]
                up     = aa_matrix[i-1][j]
                try:
                    right  = aa_matrix[i][j+1]
                except IndexError:
                    right = ' '
                center = fa_matrix[i][j]
                if center in self.__non_outline_chars:
                    continue
                else:
                    fa_matrix[i][j] = self.__get_box_drawing(left, down, up, right, center)


        fa = '\n'.join(map(lambda line: ''.join(line).rstrip(), fa_matrix))
        fa = fa.replace(kmvz_signature_placeholder, kmvz_signature)
        return self.__get_final_ascii_art(fa)


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
