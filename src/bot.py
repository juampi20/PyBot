import os
import discord
from discord.ext import commands
from settings import PREFIX, BOT_TOKEN
from os import listdir
from os.path import isfile, join, dirname
import sys, traceback
# TODO: Create database compatible on Heroku

# # Import sqlalchemy
# from sqlalchemy import engine, create_engine
# from sqlalchemy.orm import sessionmaker
# from utils.models import Base, Member

# engine = create_engine("sqlite:///database.db", echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()

# # If table does not exist, create the database
# if not engine.dialect.has_table(engine, "member"):
#     Base.metadata.create_all(engine)

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX))

if __name__ == '__main__':
    for extension in [f.split(".")[0] for f in listdir(join(dirname(__file__), 'cogs')) if f.endswith('.py')]:
        try:
            bot.load_extension('cogs' + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

bot.run(BOT_TOKEN)
