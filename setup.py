from setuptools import setup, find_packages
from os import path, chdir
from io import open
from glob import glob

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def search_json_files():
    chdir('keymapviz')
    files = glob('keyboards/*/*.json')
    chdir('..')
    return files

json_files = search_json_files()

setup(
    name='keymapviz',
    version='1.3.0',
    description='keymap.c visualizer',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yskoht/keymapviz',
    author='yskoht',
    author_email='ysk.oht@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='keymapviz keymap.c qmk_firmware',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.5',
    install_requires=['regex'],
    package_data={
        'keymapviz': json_files,
    },
    entry_points={
        'console_scripts': [
            'keymapviz=keymapviz.keymapviz:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/yskoht/keymapviz/issues',
        'Source': 'https://github.com/yskoht/keymapviz',
    },
)
