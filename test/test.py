import sys
import subprocess

status = True


def exe(cmd):
    global status
    print(cmd)
    r = subprocess.run([cmd], shell=True).returncode
    status &= (r == 0)


exe('keymapviz ./qmk_firmware/keyboards/crkbd/keymaps/default/keymap.c -o crkbd.c')
exe('keymapviz ./qmk_firmware/keyboards/crkbd/keymaps/default/keymap.c -o crkbd_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/ergo42/keymaps/default/keymap.c -o ergo42.c')
exe('keymapviz ./qmk_firmware/keyboards/ergo42/keymaps/default/keymap.c -o ergo42_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/ergodash/rev1/keymaps/default/keymap.c -o ergodash.c')
exe('keymapviz ./qmk_firmware/keyboards/ergodash/rev1/keymaps/default/keymap.c -o ergodash_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/ergodox_ez/keymaps/default/keymap.c -o ergodox.c')
exe('keymapviz ./qmk_firmware/keyboards/ergodox_ez/keymaps/default/keymap.c -o ergodox_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/fortitude60/keymaps/default/keymap.c -o fortitude60.c')
exe('keymapviz ./qmk_firmware/keyboards/fortitude60/keymaps/default/keymap.c -o fortitude60_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/helix/rev2/keymaps/default/keymap.c -o helix.c')
exe('keymapviz ./qmk_firmware/keyboards/helix/rev2/keymaps/default/keymap.c -o helix_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/kinesis/keymaps/default/keymap.c -o kinesis.c')
exe('keymapviz ./qmk_firmware/keyboards/kinesis/keymaps/default/keymap.c -o kinesis_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/lets_split/keymaps/default/keymap.c -o lets_split.c')
exe('keymapviz ./qmk_firmware/keyboards/lets_split/keymaps/default/keymap.c -o lets_split_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/mint60/keymaps/default/keymap.c -o mint60.c')
exe('keymapviz ./qmk_firmware/keyboards/mint60/keymaps/default/keymap.c -o mint60_{}.json -t json')
exe('keymapviz ./qmk_firmware/keyboards/kyria/keymaps/default/keymap.c -o kyria.c')
exe('keymapviz ./qmk_firmware/keyboards/kyria/keymaps/default/keymap.c -o kyria_{}.json -t json')

exe('keymapviz -r -k lets_split ./input/replace_lets_split_keymap.c >/dev/null 2>&1')

exe('diff -u expect/crkbd.c      crkbd.c')
exe('diff -u expect/crkbd_0.json crkbd_0.json')
exe('diff -u expect/crkbd_1.json crkbd_1.json')
exe('diff -u expect/crkbd_2.json crkbd_2.json')
exe('diff -u expect/crkbd_3.json crkbd_3.json')

exe('diff -u expect/ergo42.c      ergo42.c')
exe('diff -u expect/ergo42_0.json ergo42_0.json')
exe('diff -u expect/ergo42_1.json ergo42_1.json')
exe('diff -u expect/ergo42_2.json ergo42_2.json')

exe('diff -u expect/ergodash.c      ergodash.c')
exe('diff -u expect/ergodash_0.json ergodash_0.json')
exe('diff -u expect/ergodash_1.json ergodash_1.json')
exe('diff -u expect/ergodash_2.json ergodash_2.json')
exe('diff -u expect/ergodash_3.json ergodash_3.json')

exe('diff -u expect/ergodox.c      ergodox.c')
exe('diff -u expect/ergodox_0.json ergodox_0.json')
exe('diff -u expect/ergodox_1.json ergodox_1.json')
exe('diff -u expect/ergodox_2.json ergodox_2.json')

exe('diff -u expect/fortitude60.c      fortitude60.c')
exe('diff -u expect/fortitude60_0.json fortitude60_0.json')
exe('diff -u expect/fortitude60_1.json fortitude60_1.json')
exe('diff -u expect/fortitude60_2.json fortitude60_2.json')
exe('diff -u expect/fortitude60_3.json fortitude60_3.json')
exe('diff -u expect/fortitude60_4.json fortitude60_4.json')
exe('diff -u expect/fortitude60_5.json fortitude60_5.json')

exe('diff -u expect/helix.c       helix.c')
exe('diff -u expect/helix_0.json  helix_0.json')
exe('diff -u expect/helix_1.json  helix_1.json')
exe('diff -u expect/helix_2.json  helix_2.json')
exe('diff -u expect/helix_3.json  helix_3.json')
exe('diff -u expect/helix_4.json  helix_4.json')
exe('diff -u expect/helix_5.json  helix_5.json')
exe('diff -u expect/helix_6.json  helix_6.json')
exe('diff -u expect/helix_7.json  helix_7.json')
exe('diff -u expect/helix_8.json  helix_8.json')
exe('diff -u expect/helix_9.json  helix_9.json')
exe('diff -u expect/helix_10.json helix_10.json')
exe('diff -u expect/helix_11.json helix_11.json')

exe('diff -u expect/kinesis.c      kinesis.c')
exe('diff -u expect/kinesis_0.json kinesis_0.json')

exe('diff -u expect/lets_split.c      lets_split.c')
exe('diff -u expect/lets_split_0.json lets_split_0.json')
exe('diff -u expect/lets_split_1.json lets_split_1.json')
exe('diff -u expect/lets_split_2.json lets_split_2.json')
exe('diff -u expect/lets_split_3.json lets_split_3.json')
exe('diff -u expect/lets_split_4.json lets_split_4.json')
exe('diff -u expect/lets_split_5.json lets_split_5.json')

exe('diff -u expect/mint60.c      mint60.c')
exe('diff -u expect/mint60_0.json mint60_0.json')
exe('diff -u expect/mint60_1.json mint60_1.json')

exe('diff -u expect/kyria.c      kyria.c')
exe('diff -u expect/kyria_0.json kyria_0.json')
exe('diff -u expect/kyria_1.json kyria_1.json')
exe('diff -u expect/kyria_2.json kyria_2.json')
exe('diff -u expect/kyria_3.json kyria_3.json')

exe('diff -u expect/replace_lets_split_keymap.c input/replace_lets_split_keymap.c')

sys.exit(0 if status else 1)
