#!/usr/bin/python3
import setuptools

from os import path
dirname = path.abspath(path.dirname(__file__))

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()


setuptools.setup(
    name = 'newton-code-challenge',
    version = '0.9.3',
    author = 'artu-hnrq',
    author_email = "Arthur Henrique Della Fraga <Arthur.Henrique.Della.Fraga@gmail.com>",
    url = "https://github.com/artu-hnrq/newton-code-challenge",
    description = "A simple serialized data API using gRPC",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    license = "MIT License",

    install_requires = install_requires,
    extras_require = {
        'dev': [
            'setuptools',
            'wheel',
            'twine',
        ]
    },

    python_requires = '>=3.8.2',

    packages = setuptools.find_packages(where = 'src'),
    package_dir = {'': 'src'},

    entry_points={
        "console_scripts": [
            "newton = newton:main",
        ],
    }
)
