#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import argparse

import keymapviz
from legends import *


VERSION = 'v1.0.0'

TYPES = {
    'ascii': 'ascii_art',
    'json': 'layout_editor_json',
}


def split_path(path):
    head, tail = os.path.split(path)
    if not head:
        return [tail]
    return split_path(head) + [tail]


def parse_arg():
    keyboards = keymapviz.KEYBOARDS.keys()
    types = list(TYPES.keys())

    desc = 'keymap.c visualizer'
    parser = argparse.ArgumentParser(description=desc,
                                     epilog='Following keyboards are supported.\n * '+'\n * '.join(keyboards),
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-k', '--keyboard', type=str, choices=keyboards, help='keyboard of keymap.c', metavar='keyboards')
    parser.add_argument('-o', '--output',   type=str, help='output file name("{}" is replaced index)')
    parser.add_argument('-t', '--type',     dest='type_', type=str, choices=types, default=types[0], help='type of output(default:ascii)')
    parser.add_argument('-v', '--version',  action='version', version='%(prog)s {}'.format(VERSION))
    parser.add_argument('keymap_c',         type=argparse.FileType('r'), help='keymap.c file name')

    arg = parser.parse_args()

    # Search keyboard name in 'keymap_c' path, if '-k' option is empty.
    if arg.keyboard is None:
        path = split_path(arg.keymap_c.name)
        pset = list(set(path) & set(keyboards))  # product set
        if not pset:
            print('Sorry. Please choise your keyboard(-k/--keyboard).', file=sys.stderr)
            sys.exit(1)
        else:
            arg.keyboard = pset[0]

    return arg


def output_keymaps(output_filename, keymaps):
    if output_filename is None:
        # Output for stdout
        [print(_) for _ in keymaps]
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


if __name__ == '__main__':
    arg = parse_arg()
    kmvz = keymapviz.Keymapviz(arg.keyboard, arg.keymap_c, legends)

    keymaps = getattr(kmvz, TYPES[arg.type_])()
    output_keymaps(arg.output, keymaps)

