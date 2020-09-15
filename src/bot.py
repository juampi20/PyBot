import os
import discord
from discord.ext import commands
from settings import PREFIX, BOT_TOKEN

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

extensions = [f.split(".")[0] for f in os.listdir(os.path.join(os.path.dirname(__file__), 'cogs')) if f.endswith('.py')]

def load_extensions(cogs=None, path='cogs.'):
    '''Loads the default set of extensions or a seperate one if given'''
    for extension in cogs or extensions:
        try:
            bot.load_extension(f'{path}{extension}')
            print(f'Loaded extension: {extension}')
        except Exception as e:
            print(f'LoadError: {extension}\n'
                    f'{type(e).__name__}: {e}')

if __name__ == "__main__":
    print("Loading extensions...")
    load_extensions()

bot.run(BOT_TOKEN)
