
# Keymapviz

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](PythonVersion)
[![MIT License](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)

Keymapviz can convert keymap.c in [qmk_firmware](https://github.com/qmk/qmk_firmware) to ascii art or json file.

Following keyboards are supported.

- [crkbd](https://github.com/qmk/qmk_firmware/tree/master/keyboards/crkbd)
- [ergo42](https://github.com/qmk/qmk_firmware/tree/master/keyboards/ergo42)
- [ergodash](https://github.com/qmk/qmk_firmware/tree/master/keyboards/ergodash)
- [ergodone](https://github.com/qmk/qmk_firmware/tree/master/keyboards/ergodone)(ergodox)
- [ergodox_ez](https://github.com/qmk/qmk_firmware/tree/master/keyboards/ergodox_ez)(ergodox)
- [fortitude60](https://github.com/qmk/qmk_firmware/tree/master/keyboards/fortitude60)
- [helix](https://github.com/qmk/qmk_firmware/tree/master/keyboards/helix)
- [kaishi65](https://github.com/qmk/qmk_firmware/tree/master/keyboards/kbdclack/kaishi65)  
- [kinesis](https://github.com/qmk/qmk_firmware/tree/master/keyboards/kinesis)
- [kyria](https://github.com/qmk/qmk_firmware/tree/master/keyboards/kyria)
- [lets_split](https://github.com/qmk/qmk_firmware/tree/master/keyboards/lets_split)
- [lily58](https://github.com/qmk/qmk_firmware/tree/master/keyboards/lily58)
- [mint60](https://github.com/qmk/qmk_firmware/tree/master/keyboards/mint60)
- [sweet16](https://github.com/qmk/qmk_firmware/tree/master/keyboards/1upkeyboards/sweet16)
- [dactyl_manuform5x6](https://github.com/qmk/qmk_firmware/tree/master/keyboards/handwired/dactyl_manuform/5x6)

## Install

Keymapviz works with ***Python3***.

```sh
$ pip3 install keymapviz
```

## Usage

Output ascii art.

```sh
$ keymapviz qmk_firmware/keyboards/ergodox_ez/keymaps/default/keymap.c

/*
 *
 * .---------------------------------------------. .---------------------------------------------.
 * |  EQL  |  1  |  2  |  3  |  4  |  5  | LEFT  | ! RGHT  |  6  |  7  |  8  |  9  |  0  | MINS  |
 * !-------+-----+-----+-----+-----+-------------! !-------+-----+-----+-----+-----+-----+-------!
 * | DELT  |  Q  |  W  |  E  |  R  |  T  |TG(SYMB| !TG(SYMB|  Y  |  U  |  I  |  O  |  P  | BSLS  |
 * !-------+-----+-----+-----x-----x-----!       ! !       !-----x-----x-----+-----+-----+-------!
 * | BSPC  |  A  |  S  |  D  |  F  |  G  |-------! !-------!  H  |  J  |  K  |  L  |LT(MD|GUI_T(K|
 * !-------+-----+-----+-----x-----x-----!ALL_T(K! !MEH_T(K!-----x-----x-----+-----+-----+-------!
 * | LSFT  |CTL_T|  X  |  C  |  V  |  B  |       | !       |  N  |  M  |COMM | DOT |CTL_T| RSFT  |
 * '-------+-----+-----+-----+-----+-------------' '-------------+-----+-----+-----+-----+-------'
 *  |LT(SYM|QUOT |LALT(|LEFT |RGHT |                             ! UP  |DOWN |LBRC |RBRC | FN1  |
 *  '------------------------------'                             '------------------------------'
 *                               .---------------. .---------------.
 *                               |ALT_T(K| LGUI  | ! LALT  |CTL_T(K|
 *                       .-------+-------+-------! !-------+-------+-------.
 *                       !  SPC  ! BSPC  | HOME  | ! PGUP  |  TAB  !  ENT  !
 *                       !       !       !-------! !-------!       !       !
 *                       |       |       |  END  | ! PGDN  |       |       |
 *                       '-----------------------' '-----------------------'
 */


/*
 *
 * .---------------------------------------------. .---------------------------------------------.
 * | VRSN  | F1  | F2  | F3  | F4  | F5  |       | !       | F6  | F7  | F8  | F9  | F10 |  F11  |
 * !-------+-----+-----+-----+-----+-------------! !-------+-----+-----+-----+-----+-----+-------!
 * |       |EXLM | AT  |LCBR |RCBR |PIPE |       | !       | UP  |  7  |  8  |  9  |ASTR |  F12  |
 * !-------+-----+-----+-----x-----x-----!       ! !       !-----x-----x-----+-----+-----+-------!
 * |       |HASH | DLR |LPRN |RPRN | GRV |-------! !-------!DOWN |  4  |  5  |  6  |PLUS |       |
 * !-------+-----+-----+-----x-----x-----!       ! !       !-----x-----x-----+-----+-----+-------!
 * |       |PERC |CIRC |LBRC |RBRC |TILD |       | !       |AMPR |  1  |  2  |  3  |BSLS |       |
 * '-------+-----+-----+-----+-----+-------------' '-------------+-----+-----+-----+-----+-------'
 *  | EPRM |     |     |     |     |                             !     | DOT |  0  | EQL |      |
 *  '------------------------------'                             '------------------------------'
 *                               .---------------. .---------------.
 *                               |RGB_MOD|       | !RGB_TOG|RGB_SLD|
 *                       .-------+-------+-------! !-------+-------+-------.
 *                       !RGB_VAD!RGB_VAI|       | !       |RGB_HUD!RGB_HUI!
 *                       !       !       !-------! !-------!       !       !
 *                       |       |       |       | !       |       |       |
 *                       '-----------------------' '-----------------------'
 */


/*
 *
 * .---------------------------------------------. .---------------------------------------------.
 * |       |     |     |     |     |     |       | !       |     |     |     |     |     |       |
 * !-------+-----+-----+-----+-----+-------------! !-------+-----+-----+-----+-----+-----+-------!
 * |       |     |     |MS_U |     |     |       | !       |     |     |     |     |     |       |
 * !-------+-----+-----+-----x-----x-----!       ! !       !-----x-----x-----+-----+-----+-------!
 * |       |     |MS_L |MS_D |MS_R |     |-------! !-------!     |     |     |     |     | MPLY  |
 * !-------+-----+-----+-----x-----x-----!       ! !       !-----x-----x-----+-----+-----+-------!
 * |       |     |     |     |     |     |       | !       |     |     |MPRV |MNXT |     |       |
 * '-------+-----+-----+-----+-----+-------------' '-------------+-----+-----+-----+-----+-------'
 *  |      |     |     |BTN1 |BTN2 |                             !VOLU |VOLD |MUTE |     |      |
 *  '------------------------------'                             '------------------------------'
 *                               .---------------. .---------------.
 *                               |       |       | !       |       |
 *                       .-------+-------+-------! !-------+-------+-------.
 *                       !       !       |       | !       |       ! WBAK  !
 *                       !       !       !-------! !-------!       !       !
 *                       |       |       |       | !       |       |       |
 *                       '-----------------------' '-----------------------'
 */
```

Legend replacements.
A config file containing legend replacements can be provided to change the legends to your liking. It should have a section named 'legends' and e.g. look like:
```
[legends]
KC_BLSLS=\
KC_QUOT='
```
It can then be provided on the commandline like:
```
$ keymapviz qmk_firmware/keyboards/lets_split/keymaps/default/keymap.c -c /path/to/config.properties
```
An example file is provided in the root of this project, named `config.properties`.

Output json file.
This json file can be used in [http://www.keyboard-layout-editor.com/](http://www.keyboard-layout-editor.com/).


```sh
$ keymapviz qmk_firmware/keyboards/lets_split/keymaps/default/keymap.c -t json -o 'lets_split{}.json'
$ ls lets_split*.json
lets_split0.json  lets_split1.json  lets_split2.json  lets_split3.json  lets_split4.json  lets_split5.json
```

Output fancy ascii art.
Uses unicode symbols for drawing the box outlines.

```sh
$ keymapviz  -t fancy ~/qmk_firmware/keyboards/kbdclack/kaishi65/keymaps/default/keymap.c

/*┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┬────┐
 *│ES │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │ 0 │ MI│ EQ│  BS   │ GR │
 *├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┼────┤
 *│ TA  │ Q │ W │ E │ R │ T │ Y │ U │ I │ O │ P │ LB│ RB│ BS  │ DE │
 *├─────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─────┼────┤
 *│  CA   │ A │ S │ D │ F │ G │ H │ J │ K │ L │ SC│ QU│  EN   │ PG │
 *├───────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴───┬───┼────┤
 *│   LS   │ Z │ X │ C │ V │ B │ N │ M │ CO│ DO│ SL│  RS  │ UP│ PG │
 *├────┬───┴┬──┴─┬─┴───┴───┴───┴───┴───┴─┬─┴─┬─┴─┬─┴──┬───┼───┼────┤
 *│ LC │ LG │ LA │          SP           │ RA│ MO│ RC │ LE│ DO│ RG │
 *└────┴────┴────┴───────────────────────┴───┴───┴────┴───┴───┴────┘
 * generated by [keymapviz]
 */

/*┌───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───┬───────┬────┐
 *│   │ F1│ F2│ F3│ F4│ F5│ F6│ F7│ F8│ F9│ F1│ F1│ F1│  DE   │    │
 *├───┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─────┼────┤
 *│     │ BT│ MS│ BT│   │   │   │   │   │   │   │   │   │     │ IN │
 *├─────┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─┬─┴─────┼────┤
 *│       │ MS│ MS│ MS│   │   │   │   │   │   │   │   │       │ HO │
 *├───────┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴┬──┴───┬───┼────┤
 *│        │   │   │   │   │   │   │ MU│   │   │   │      │ VO│ EN │
 *├────┬───┴┬──┴─┬─┴───┴───┴───┴───┴───┴─┬─┴─┬─┴─┬─┴──┬───┼───┼────┤
 *│    │    │    │                       │   │   │    │ MP│ VO│ MN │
 *└────┴────┴────┴───────────────────────┴───┴───┴────┴───┴───┴────┘
 * generated by [keymapviz]
 */
```

Replace ascii-art in keymap.c. (Generate backup as keymap.c.bac)

```sh
$ keymapviz -r keymap.c
```

## License

This software is released under the MIT License, see LICENSE.
