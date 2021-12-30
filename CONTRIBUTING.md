# Contributing

Your any contributions are welcome! Adding keyboard, fixing bug, updating document, adding test and creating new feature, etc.

- Getting code
- Creating feature branch from develop
- If you want to add a new keyboard
  - Adding keymapviz/keyboards/_keyboard_name_/\_\_init\_\_.py
  - Adding keymapviz/keyboards/_keyboard_name_/layout_editor/default.json
  - Fixing keymapviz/\_\_init\_\_.py
  - Fixing keymapviz/README.md
- Run
- Committing & push your code and
- Create pull request

---

## Getting code

```sh
$ git clone https://github.com/yskoht/keymapviz.git
$ cd keymapviz
```

## Creating feature branch from develop

```sh
$ git switch -c feature/nice-branch-name origin/develop # please replace :)
Branch 'feature/nice-branch-name' set up to track remote branch 'develop' from 'origin'.
Switched to a new branch 'feature/nice-branch-name'

$ git branch
* feature/nice-branch-name
  master
```

## If you want to add a new keyboard

You need to add two new files. (Replace _keyboard_name_ with the name of the keyboard you want to add.)

- keymapviz/keyboards/_keyboard_name_/\_\_init\_\_.py
- keymapviz/keyboards/_keyboard_name_/layout_editor/default.json

And fix two files.

- keymapviz/\_\_init\_\_.py
- keymapviz/README.md

### Adding keymapviz/keyboards/_keyboard_name_/\_\_init\_\_.py

Define three variables in this file. `keymap_keyword`, `layout_editor_json` and `ascii_art`.
(`fancy_ascii_art` is optional.)

- `keymap_keyword`: The regular expression for the macro keywords used to define the keymap in `keymap.c` of qmk.
- `layout_editor_json`: The path to `layout_editor.json` file.
- `ascii_art`: ASCII art. `{}` is replaced by a key legend. If you want to place the key legend in a desired location, you need to write the key index in the bracket. Please refer to these files.
  - [keymapviz/keyboards/lets_split/\_\_init\_\_.py](https://github.com/yskoht/keymapviz/blob/develop/keymapviz/keyboards/lets_split/__init__.py)
  - [keymapviz/keyboards/ergodox/\_\_init\_\_.py](https://github.com/yskoht/keymapviz/blob/develop/keymapviz/keyboards/ergodox/__init__.py)

### Adding keymapviz/keyboards/_keyboard_name_/layout_editor/default.json

Download json of your keyboard from [http://www.keyboard-layout-editor.com/](http://www.keyboard-layout-editor.com/) and replace legend with `{number}`. Please refer to the file.

- [keymapviz/keyboards/lets_split/layout_editor/default.json](https://github.com/yskoht/keymapviz/blob/develop/keymapviz/keyboards/lets_split/layout_editor/default.json)

### Fixing keymapviz/\_\_init\_\_.py

Add keyboard.

```diff
 ...
 import keymapviz.keyboards.kinesis
 import keymapviz.keyboards.helix
 import keymapviz.keyboards.mint60
+import keymapviz.keyboards.keyboard_name # Here

 ...
 KEYBOARDS = {
    ...
+   'mint60': keymapviz.keyboards.mint60, # Add comma
+   'keyboard_name': keymapviz.keyboards.keyboard_name # Here
}
```

### Fixing keymapviz/README.md

Add keyboard.

```diff
 ...
 - [kinesis](https://github.com/qmk/qmk_firmware/tree/master/keyboards/kinesis)
 - [lets_split](https://github.com/qmk/qmk_firmware/tree/master/keyboards/lets_split)
 - [mint60](https://github.com/qmk/qmk_firmware/tree/master/keyboards/mint60)
+- [keyboard_name](https://github.com/qmk/qmk_firmware/tree/master/keyboards/keyboard_name) # Here
```

## Run

Install `keymapviz` on your PC and make sure it works properly.

```sh
$ pip install setuptools
$ python setup.py sdist # build
$ pip install dist/*.tar.gz # install
$ keymapviz -v # You can use your own keymapviz.
```

## Committing & push your code and

```sh
$ git add -A
$ git commit -m 'nice commit message' # please replace :)
$ git push -u origin feature/nice-branch-name # please replace :)
```

## Create pull request

Create the pull request on github for `yskoht/keymapviz` `develop` branch.
