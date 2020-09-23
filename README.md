# PyBot

## Introduction

**PyBot** is a simple Discord bot, made with python, for my personal server.

## Installation with [Pipenv][pipenv-web]

If you dont have pipenv:

`pip3 install --user pipenv`

To install the environment with the necessary packages, run this code:

`pipenv install`

To start the bot, run this code:

`pipenv run start`

Make sure you have pipenv installed, eitherwise, manually install:

- [discord.py[voice]][discord.py-web]
- [python-dotenv][python-dotenv-web]
- [riotwatcher][riotwatcher-web]

`pip install <package>`

You need to load the environment variables in the **.env** file.

Rename the **.env.example** file to **.env** and load the new environment variables.

[pipenv-web]: https://github.com/pypa/pipenv/blob/master/README.md
[discord.py-web]: https://pypi.org/project/discord.py/
[riotwatcher-web]: https://pypi.org/project/riotwatcher/
[python-dotenv-web]: https://pypi.org/project/python-dotenv/
