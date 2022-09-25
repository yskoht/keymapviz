import sys
import subprocess

status = True


def exe(cmd):
    global status
    print(cmd)
    r = subprocess.run([cmd], shell=True).returncode
    status &= (r == 0)


# crkbd
exe('keymapviz ./qmk_firmware/keyboards/crkbd/keymaps/default/keymap.c -o crkbd.c')
exe('keymapviz ./qmk_firmware/keyboards/crkbd/keymaps/default/keymap.c -o crkbd_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/crkbd/keymaps/default/keymap.c -o crkbd_{}.json -t json')

exe('diff -u expect/crkbd.c       crkbd.c')
exe('diff -u expect/crkbd_fancy.c crkbd_fancy.c')
exe('diff -u expect/crkbd_0.json  crkbd_0.json')
exe('diff -u expect/crkbd_1.json  crkbd_1.json')
exe('diff -u expect/crkbd_2.json  crkbd_2.json')
exe('diff -u expect/crkbd_3.json  crkbd_3.json')

# dactyl_manuform5x6
exe('keymapviz -k dactyl_manuform5x6 ./qmk_firmware/keyboards/handwired/dactyl_manuform/5x6/keymaps/default/keymap.c -o dactyl_manuform5x6.c')
exe('keymapviz -k dactyl_manuform5x6 ./qmk_firmware/keyboards/handwired/dactyl_manuform/5x6/keymaps/default/keymap.c -o dactyl_manuform5x6_fancy.c -t fancy')
exe('keymapviz -k dactyl_manuform5x6 ./qmk_firmware/keyboards/handwired/dactyl_manuform/5x6/keymaps/default/keymap.c -o dactyl_manuform5x6_{}.json -t json')

exe('diff -u expect/dactyl_manuform5x6.c       dactyl_manuform5x6.c')
exe('diff -u expect/dactyl_manuform5x6_fancy.c dactyl_manuform5x6_fancy.c')
exe('diff -u expect/dactyl_manuform5x6_0.json  dactyl_manuform5x6_0.json')

# ergo42
exe('keymapviz ./qmk_firmware/keyboards/biacco42/ergo42/keymaps/default/keymap.c -o ergo42.c')
exe('keymapviz ./qmk_firmware/keyboards/biacco42/ergo42/keymaps/default/keymap.c -o ergo42_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/biacco42/ergo42/keymaps/default/keymap.c -o ergo42_{}.json -t json')

exe('diff -u expect/ergo42.c       ergo42.c')
exe('diff -u expect/ergo42_fancy.c ergo42_fancy.c')
exe('diff -u expect/ergo42_0.json  ergo42_0.json')
exe('diff -u expect/ergo42_1.json  ergo42_1.json')
exe('diff -u expect/ergo42_2.json  ergo42_2.json')

# ergodash
exe('keymapviz ./qmk_firmware/keyboards/omkbd/ergodash/rev1/keymaps/default/keymap.c -o ergodash.c')
exe('keymapviz ./qmk_firmware/keyboards/omkbd/ergodash/rev1/keymaps/default/keymap.c -o ergodash_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/omkbd/ergodash/rev1/keymaps/default/keymap.c -o ergodash_{}.json -t json')

exe('diff -u expect/ergodash.c       ergodash.c')
exe('diff -u expect/ergodash_fancy.c ergodash_fancy.c')
exe('diff -u expect/ergodash_0.json  ergodash_0.json')
exe('diff -u expect/ergodash_1.json  ergodash_1.json')
exe('diff -u expect/ergodash_2.json  ergodash_2.json')
exe('diff -u expect/ergodash_3.json  ergodash_3.json')

# ergodash (2u_inner)
exe('keymapviz ./qmk_firmware/keyboards/omkbd/ergodash/rev1/keymaps/default/keymap.c -l 2u_inner -o ergodash_L2u_inner.c')
exe('keymapviz ./qmk_firmware/keyboards/omkbd/ergodash/rev1/keymaps/default/keymap.c -l 2u_inner -o ergodash_L2u_inner_fancy.c -t fancy ')
exe('keymapviz ./qmk_firmware/keyboards/omkbd/ergodash/rev1/keymaps/default/keymap.c -l 2u_inner -o ergodash_L2u_inner_{}.json -t json')

exe('diff -u expect/ergodash_L2u_inner.c       ergodash_L2u_inner.c')
exe('diff -u expect/ergodash_L2u_inner_fancy.c ergodash_L2u_inner_fancy.c')
exe('diff -u expect/ergodash_L2u_inner_0.json  ergodash_L2u_inner_0.json')
exe('diff -u expect/ergodash_L2u_inner_1.json  ergodash_L2u_inner_1.json')
exe('diff -u expect/ergodash_L2u_inner_2.json  ergodash_L2u_inner_2.json')
exe('diff -u expect/ergodash_L2u_inner_3.json  ergodash_L2u_inner_3.json')

# ergodox_ez
exe('keymapviz ./qmk_firmware/keyboards/ergodox_ez/keymaps/default/keymap.c -o ergodox.c')
exe('keymapviz ./qmk_firmware/keyboards/ergodox_ez/keymaps/default/keymap.c -o ergodox_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/ergodox_ez/keymaps/default/keymap.c -o ergodox_{}.json -t json')

exe('diff -u expect/ergodox.c       ergodox.c')
exe('diff -u expect/ergodox_fancy.c ergodox_fancy.c')
exe('diff -u expect/ergodox_0.json  ergodox_0.json')
exe('diff -u expect/ergodox_1.json  ergodox_1.json')
exe('diff -u expect/ergodox_2.json  ergodox_2.json')

# fortitude60
exe('keymapviz ./qmk_firmware/keyboards/fortitude60/keymaps/default/keymap.c -o fortitude60.c')
exe('keymapviz ./qmk_firmware/keyboards/fortitude60/keymaps/default/keymap.c -o fortitude60_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/fortitude60/keymaps/default/keymap.c -o fortitude60_{}.json -t json')

exe('diff -u expect/fortitude60.c       fortitude60.c')
exe('diff -u expect/fortitude60_fancy.c fortitude60_fancy.c')
exe('diff -u expect/fortitude60_0.json  fortitude60_0.json')
exe('diff -u expect/fortitude60_1.json  fortitude60_1.json')
exe('diff -u expect/fortitude60_2.json  fortitude60_2.json')
exe('diff -u expect/fortitude60_3.json  fortitude60_3.json')
exe('diff -u expect/fortitude60_4.json  fortitude60_4.json')
exe('diff -u expect/fortitude60_5.json  fortitude60_5.json')

# helix
exe('keymapviz ./qmk_firmware/keyboards/helix/rev2/keymaps/default/keymap.c -o helix.c')
exe('keymapviz ./qmk_firmware/keyboards/helix/rev2/keymaps/default/keymap.c -o helix_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/helix/rev2/keymaps/default/keymap.c -o helix_{}.json -t json')

exe('diff -u expect/helix.c        helix.c')
exe('diff -u expect/helix_fancy.c  helix_fancy.c')
exe('diff -u expect/helix_0.json   helix_0.json')
exe('diff -u expect/helix_1.json   helix_1.json')
exe('diff -u expect/helix_2.json   helix_2.json')
exe('diff -u expect/helix_3.json   helix_3.json')
exe('diff -u expect/helix_4.json   helix_4.json')
exe('diff -u expect/helix_5.json   helix_5.json')
exe('diff -u expect/helix_6.json   helix_6.json')
exe('diff -u expect/helix_7.json   helix_7.json')
exe('diff -u expect/helix_8.json   helix_8.json')
exe('diff -u expect/helix_9.json   helix_9.json')
exe('diff -u expect/helix_10.json  helix_10.json')
exe('diff -u expect/helix_11.json  helix_11.json')

# kaishi65
exe('keymapviz ./qmk_firmware/keyboards/kbdclack/kaishi65/keymaps/default/keymap.c -o kaishi65.c')
exe('keymapviz ./qmk_firmware/keyboards/kbdclack/kaishi65/keymaps/default/keymap.c -o kaishi65_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/kbdclack/kaishi65/keymaps/default/keymap.c -o kaishi65_{}.json -t json')

exe('diff -u expect/kaishi65.c        kaishi65.c')
exe('diff -u expect/kaishi65_fancy.c  kaishi65_fancy.c')
exe('diff -u expect/kaishi65_0.json   kaishi65_0.json')
exe('diff -u expect/kaishi65_1.json   kaishi65_1.json')

# kinesis
exe('keymapviz ./qmk_firmware/keyboards/kinesis/keymaps/default/keymap.c -o kinesis.c')
exe('keymapviz ./qmk_firmware/keyboards/kinesis/keymaps/default/keymap.c -o kinesis_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/kinesis/keymaps/default/keymap.c -o kinesis_{}.json -t json')

exe('diff -u expect/kinesis.c       kinesis.c')
exe('diff -u expect/kinesis_fancy.c kinesis_fancy.c')
exe('diff -u expect/kinesis_0.json  kinesis_0.json')

# kyria
exe('keymapviz ./qmk_firmware/keyboards/splitkb/kyria/keymaps/default/keymap.c -o kyria.c')
exe('keymapviz ./qmk_firmware/keyboards/splitkb/kyria/keymaps/default/keymap.c -o kyria_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/splitkb/kyria/keymaps/default/keymap.c -o kyria_{}.json -t json')

exe('diff -u expect/kyria.c       kyria.c')
exe('diff -u expect/kyria_fancy.c kyria_fancy.c')
exe('diff -u expect/kyria_0.json  kyria_0.json')
exe('diff -u expect/kyria_1.json  kyria_1.json')
exe('diff -u expect/kyria_2.json  kyria_2.json')
exe('diff -u expect/kyria_3.json  kyria_3.json')
exe('diff -u expect/kyria_4.json  kyria_4.json')
exe('diff -u expect/kyria_5.json  kyria_5.json')
exe('diff -u expect/kyria_6.json  kyria_6.json')

# lets_split
exe('keymapviz ./qmk_firmware/keyboards/lets_split/keymaps/default/keymap.c -o lets_split.c')
exe('keymapviz ./qmk_firmware/keyboards/lets_split/keymaps/default/keymap.c -o lets_split_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/lets_split/keymaps/default/keymap.c -o lets_split_{}.json -t json')

exe('diff -u expect/lets_split.c       lets_split.c')
exe('diff -u expect/lets_split_fancy.c lets_split_fancy.c')
exe('diff -u expect/lets_split_0.json  lets_split_0.json')
exe('diff -u expect/lets_split_1.json  lets_split_1.json')
exe('diff -u expect/lets_split_2.json  lets_split_2.json')
exe('diff -u expect/lets_split_3.json  lets_split_3.json')
exe('diff -u expect/lets_split_4.json  lets_split_4.json')
exe('diff -u expect/lets_split_5.json  lets_split_5.json')

# lily58
exe('keymapviz ./qmk_firmware/keyboards/lily58/keymaps/default/keymap.c -o lily58.c')
exe('keymapviz ./qmk_firmware/keyboards/lily58/keymaps/default/keymap.c -o lily58_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/lily58/keymaps/default/keymap.c -o lily58_{}.json -t json')

exe('diff -u expect/lily58.c       lily58.c')
exe('diff -u expect/lily58_fancy.c lily58_fancy.c')
exe('diff -u expect/lily58_0.json  lily58_0.json')
exe('diff -u expect/lily58_1.json  lily58_1.json')
exe('diff -u expect/lily58_2.json  lily58_2.json')
exe('diff -u expect/lily58_3.json  lily58_3.json')

# mint60
exe('keymapviz ./qmk_firmware/keyboards/mint60/keymaps/default/keymap.c -o mint60.c')
exe('keymapviz ./qmk_firmware/keyboards/mint60/keymaps/default/keymap.c -o mint60_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/mint60/keymaps/default/keymap.c -o mint60_{}.json -t json')

exe('diff -u expect/mint60.c       mint60.c')
exe('diff -u expect/mint60_fancy.c mint60_fancy.c')
exe('diff -u expect/mint60_0.json  mint60_0.json')
exe('diff -u expect/mint60_1.json  mint60_1.json')

# moonlander
exe('keymapviz ./qmk_firmware/keyboards/moonlander/keymaps/default/keymap.c -o moonlander.c')
exe('keymapviz ./qmk_firmware/keyboards/moonlander/keymaps/default/keymap.c -o moonlander_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/moonlander/keymaps/default/keymap.c -o moonlander_{}.json -t json')

exe('diff -u expect/moonlander.c       moonlander.c')
exe('diff -u expect/moonlander_fancy.c moonlander_fancy.c')
exe('diff -u expect/moonlander_0.json  moonlander_0.json')
exe('diff -u expect/moonlander_1.json  moonlander_1.json')
exe('diff -u expect/moonlander_2.json  moonlander_2.json')

# sofle
exe('keymapviz ./qmk_firmware/keyboards/sofle/keymaps/default/keymap.c -o sofle.c')
exe('keymapviz ./qmk_firmware/keyboards/sofle/keymaps/default/keymap.c -o sofle_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/sofle/keymaps/default/keymap.c -o sofle_{}.json -t json')

exe('diff -u expect/sofle.c        sofle.c')
exe('diff -u expect/sofle_fancy.c  sofle_fancy.c')
exe('diff -u expect/sofle_0.json   sofle_0.json')
exe('diff -u expect/sofle_1.json   sofle_1.json')
exe('diff -u expect/sofle_2.json   sofle_2.json')
exe('diff -u expect/sofle_3.json   sofle_3.json')
exe('diff -u expect/sofle_4.json   sofle_4.json')

# sweet16
exe('keymapviz ./qmk_firmware/keyboards/1upkeyboards/sweet16/keymaps/default/keymap.c -o sweet16.c')
exe('keymapviz ./qmk_firmware/keyboards/1upkeyboards/sweet16/keymaps/default/keymap.c -o sweet16_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/1upkeyboards/sweet16/keymaps/default/keymap.c -o sweet16_{}.json -t json')

exe('diff -u expect/sweet16.c       sweet16.c')
exe('diff -u expect/sweet16_fancy.c sweet16_fancy.c')
exe('diff -u expect/sweet16_0.json  sweet16_0.json')

# replace option
exe('keymapviz -r -k lets_split ./input/replace_lets_split_keymap.c >/dev/null 2>&1')
exe('diff -u expect/replace_lets_split_keymap.c input/replace_lets_split_keymap.c')

exe('keymapviz -r -k lets_split -t fancy ./input/replace_lets_split_keymap_fancy.c >/dev/null 2>&1')
exe('diff -u expect/replace_lets_split_keymap_fancy.c input/replace_lets_split_keymap_fancy.c')

# custom config
exe('keymapviz -k lets_split ./input/custom_legends_lets_split_keymap.c -c ./input/custom_legends_config.properties -o custom_legends_lets_split.c')
exe('diff -u expect/custom_legends_lets_split.c custom_legends_lets_split.c')

# planck (default/grid)
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/default/keymap.c -o planck_default.c')
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/default/keymap.c -o planck_default_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/default/keymap.c -o planck_default_{}.json -t json')

exe('diff -u expect/planck_grid.c       planck_default.c')
exe('diff -u expect/planck_grid_fancy.c planck_default_fancy.c')
exe('diff -u expect/planck_grid_0.json  planck_default_0.json')
exe('diff -u expect/planck_grid_1.json  planck_default_1.json')
exe('diff -u expect/planck_grid_2.json  planck_default_2.json')
exe('diff -u expect/planck_grid_3.json  planck_default_3.json')
exe('diff -u expect/planck_grid_4.json  planck_default_4.json')
exe('diff -u expect/planck_grid_5.json  planck_default_5.json')

exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/default/keymap.c -o planck_grid.c -l grid')
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/default/keymap.c -o planck_grid_fancy.c -t fancy -l grid')
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/default/keymap.c -o planck_grid_{}.json -t json -l grid')

exe('diff -u expect/planck_grid.c       planck_grid.c')
exe('diff -u expect/planck_grid_fancy.c planck_grid_fancy.c')
exe('diff -u expect/planck_grid_0.json  planck_grid_0.json')
exe('diff -u expect/planck_grid_1.json  planck_grid_1.json')
exe('diff -u expect/planck_grid_2.json  planck_grid_2.json')
exe('diff -u expect/planck_grid_3.json  planck_grid_3.json')
exe('diff -u expect/planck_grid_4.json  planck_grid_4.json')
exe('diff -u expect/planck_grid_5.json  planck_grid_5.json')

# planck (mit)
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/rootiest/keymap.c -o planck_mit.c -l mit')
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/rootiest/keymap.c -o planck_mit_fancy.c -t fancy -l mit')
exe('keymapviz ./qmk_firmware/keyboards/planck/keymaps/rootiest/keymap.c -o planck_mit_{}.json -t json -l mit')

exe('diff -u expect/planck_mit.c       planck_mit.c')
exe('diff -u expect/planck_mit_fancy.c planck_mit_fancy.c')
exe('diff -u expect/planck_mit_0.json  planck_mit_0.json')
exe('diff -u expect/planck_mit_1.json  planck_mit_1.json')
exe('diff -u expect/planck_mit_2.json  planck_mit_2.json')
exe('diff -u expect/planck_mit_3.json  planck_mit_3.json')
exe('diff -u expect/planck_mit_4.json  planck_mit_4.json')
exe('diff -u expect/planck_mit_5.json  planck_mit_5.json')

# id75
exe('keymapviz ./qmk_firmware/keyboards/idobao/id75/keymaps/default/keymap.c -o id75.c')
exe('keymapviz ./qmk_firmware/keyboards/idobao/id75/keymaps/default/keymap.c -o id75_fancy.c -t fancy')
exe('keymapviz ./qmk_firmware/keyboards/idobao/id75/keymaps/default/keymap.c -o id75_{}.json -t json')

exe('diff -u expect/id75.c       id75.c')
exe('diff -u expect/id75_fancy.c id75_fancy.c')
exe('diff -u expect/id75_0.json  id75_0.json')
exe('diff -u expect/id75_1.json  id75_1.json')

if status:
    print('\nAll tests were passed successfully!')
sys.exit(0 if status else 1)
