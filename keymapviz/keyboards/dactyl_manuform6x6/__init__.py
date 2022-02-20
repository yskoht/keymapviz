# -*- coding: utf-8 -*-

keymap_keyword = '(?:KEYMAP|LAYOUT_6x6)'
layout_editor_json = {
  'default': 'keyboards/dactyl_manuform6x6/layout_editor/default.json',
}

ascii_art = {
  'default': '''
/*                 ,-------------------------------. ,-------------------------------.
 * ,---------------|{   2 }|{   3 }|{   4 }|{   5 }| |{   6 }|{   7 }|{   8 }|{   9 }|--------------.
 * |{   0 }|{   1 }|-------+-------+-------+-------| |-------+-------+-------+-------|{  10 }|{ 11 }|
 * |-------+-------|{  14 }|{  15 }|{  16 }|{  17 }| |{  18 }|{  19 }|{  20 }|{  21 }|-------+------|
 * |{  12 }|{  13 }|-------+-------+-------+-------| |-------+-------+-------+-------|{  22 }|{ 23 }|
 * |-------+-------|{  26 }|{  27 }|{  28 }|{  29 }| |{  30 }|{  31 }|{  32 }|{  33 }|-------+------|
 * |{  24 }|{  25 }|-------+-------+-------+-------| |-------+-------+-------+-------|{  34 }|{ 35 }|
 * |-------+-------|{  38 }|{  39 }|{  40 }|{  41 }| |{  42 }|{  43 }|{  44 }|{  45 }|-------+------|
 * |{  36 }|{  37 }|-------+-------+---------------' `---------------+-------+-------|{  46 }|{ 47 }|
 * |-------+-------|{  50 }|{  51 }|{  52 }|{  53 }| |{  54 }|{  55 }|{  56 }|{  57 }|-------+------|
 * |{  48 }|{  49 }|-------+-------+---------------' `---------------+-------+-------|{  58 }|{ 59 }|
 * `---------------|{  60 }|{  61 }|                                 |{  62 }|{  63 }|--------------'
 *                 `---------------'                                 `---------------'
 *                                 ,---------------. ,---------------.
 *                                 |{  64 }|{  65 }| |{  66 }|{  67 }|
 *                                 |-------+-------| |-------+-------|
 *                                 |{  68 }|{  69 }| |{  70 }|{  71 }|
 *                                 |-------+-------| |-------+-------|
 *                                 |{  72 }|{  73 }| |{  74 }|{  75 }|
 *                                 `---------------' `---------------'       generated by [keymapviz] */
''',
}

fancy_ascii_art = {
  'default': '''
/*                 ┌───────┬───────┬───────┬───────┐ ┌───────┬───────┬───────┬───────┐
 * ┌───────┬───────┤{   2 }│{   3 }│{   4 }│{   5 }│ │{   6 }│{   7 }│{   8 }│{   9 }├───────┬──────┐
 * │{   0 }│{   1 }├───────┼───────┼───────┼───────┤ ├───────┼───────┼───────┼───────┤{  10 }│{ 11 }│
 * ├───────┼───────┤{  14 }│{  15 }│{  16 }│{  17 }│ │{  18 }│{  19 }│{  20 }│{  21 }├───────┼──────┤
 * │{  12 }│{  13 }├───────┼───────┼───────┼───────┤ ├───────┼───────┼───────┼───────┤{  22 }│{ 23 }│
 * ├───────┼───────┤{  26 }│{  27 }│{  28 }│{  29 }│ │{  30 }│{  31 }│{  32 }│{  33 }├───────┼──────┤
 * │{  24 }│{  25 }├───────┼───────┼───────┼───────┤ ├───────┼───────┼───────┼───────┤{  34 }│{ 35 }│
 * ├───────┼───────┤{  38 }│{  39 }│{  40 }│{  41 }│ │{  42 }│{  43 }│{  44 }│{  45 }├───────┼──────┤
 * │{  36 }│{  37 }├───────┼───────┼───────┴───────┘ └───────┴───────┼───────┼───────┤{  46 }│{ 47 }│
 * ├───────┼───────┤{  50 }│{  51 }│{  52 }│{  53 }│ │{  54 }│{  55 }│{  56 }│{  57 }├───────┼──────┤
 * │{  48 }│{  49 }├───────┼───────┼───────┴───────┘ └───────┴───────┼───────┼───────┤{  58 }│{ 59 }│
 * └───────┴───────┤{  60 }│{  61 }│                                 │{  62 }│{  63 }├───────┴──────┘
 *                 └───────┴───────┘                                 └───────┴───────┘
 *                                 ┏━━━━━━━┳━━━━━━━┓ ┏━━━━━━━┳━━━━━━━┓
 *                                 ┃{  64 }┃{  65 }┃ ┃{  66 }┃{  67 }┃
 *                                 ┡━━━━━━━╋━━━━━━━┫ ┣━━━━━━━╋━━━━━━━┩
 *                                 │{  68 }┃{  69 }┃ ┃{  70 }┃{  71 }│
 *                                 ├───────╄━━━━━━━┩ ┡━━━━━━━╃───────┤
 *                                 │{  72 }│{  73 }│ │{  74 }│{  75 }│
 *                                 └───────┴───────┘ └───────┴───────┘       generated by [keymapviz] */
''',
}
