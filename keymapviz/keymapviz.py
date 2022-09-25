#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse

import keymapviz
from keymapviz.legends import *


VERSION = 'v1.13.0'

TYPES = {
    'ascii': 'ascii_art',
    'json': 'layout_editor_json',
    'fancy': 'fancy_art',
}


def split_path(path):
    head, tail = os.path.split(path)
    if (not head) or (head == '/'):
        return [tail]
    return split_path(head) + [tail]

def get_epilog(keyboard_keys):
    keyboard_layouts_pairs = []
    for key in keyboard_keys:
        layout_keys = list(keymapviz.KEYBOARDS[key].ascii_art.keys())
        keyboard_layouts_pairs.append((key, layout_keys))
    layouts_dict = dict(keyboard_layouts_pairs)

    keyboard_descriptions = []
    for key in keyboard_keys:
        desc = '{} ({})'.format('{:20}'.format(key), ', '.join(layouts_dict[key]))
        keyboard_descriptions.append(desc)

    header = 'Following keyboards (and layouts) are supported.'
    keyboard_description = '\n * '.join(keyboard_descriptions)
    epilog = header + '\n * ' + keyboard_description
    return epilog

def parse_arg():
    keyboard_keys = sorted(keymapviz.KEYBOARDS.keys())
    types = list(TYPES.keys())

    desc = 'keymap.c visualizer'
    epilog = get_epilog(keyboard_keys)
    parser = argparse.ArgumentParser(description=desc,
                                     epilog=epilog,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-c', '--config',   type=argparse.FileType('r'), help='configuration file')
    parser.add_argument('-k', '--keyboard', type=str, choices=keyboard_keys, help='keyboard of keymap.c', metavar='keyboards')
    parser.add_argument('-l', '--layout',   type=str, help='keyboard layout', metavar='layout')
    parser.add_argument('-o', '--output',   type=str, help='output file name("{}" is replaced index)')
    parser.add_argument('-r', '--replace',  action='store_true', help='replace comment block including "[keymapviz]" with ascii art. (make *.bac)')
    parser.add_argument('-t', '--type',     dest='type_', type=str, choices=types, default=types[0], help='type of output(default:ascii)')
    parser.add_argument('-v', '--version',  action='version', version='%(prog)s {}'.format(VERSION))
    parser.add_argument('keymap_c',         type=argparse.FileType('r', encoding='utf-8'), help='keymap.c file name')

    arg = parser.parse_args()

    # Search keyboard name in 'keymap_c' path, if '-k' option is empty.
    if arg.keyboard is None:
        path = split_path(os.path.abspath(arg.keymap_c.name))
        pset = list(set(path) & set(keyboard_keys))  # product set
        if not pset:
            print('Sorry. Please choose your keyboard(-k/--keyboard).', file=sys.stderr)
            sys.exit(1)
        else:
            arg.keyboard = pset[0]

    return arg


def output_keymaps(output_filename, keymaps):
    if output_filename is None:
        # Output for stdout
        [print(_ + '\n') for _ in keymaps]
    else:
        # Output for file
        for i in range(len(keymaps)):
            f = output_filename.format(i)
            if os.path.exists(f):
                os.remove(f)

        for i, k in enumerate(keymaps):
            f = output_filename.format(i)
            with open(f, 'a') as file_:
                print(k, file=file_)


def output_keymap_c(output_filename, keymap_c):
    if os.path.exists(output_filename):
        os.rename(output_filename, output_filename + ".bac")
    with open(output_filename, 'w') as f:
        print(keymap_c, file=f, end='')


def main():
    arg = parse_arg()
    kmvz = keymapviz.Keymapviz(arg.keyboard, arg.keymap_c, arg.layout, read_config(arg.config))

    keymaps = getattr(kmvz, TYPES[arg.type_])()
    output_keymaps(arg.output, keymaps)
    if arg.replace:
        output_keymap_c(arg.keymap_c.name, kmvz.keymap_c())

