import os
from os import listdir
from os.path import isfile, join
from discord.ext import commands
from settings import PREFIX, BOT_TOKEN

bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX))

ext_list = [f for f in listdir("src/cogs") if isfile(join("src/cogs", f))]
ext_name_list = [f.split('.')[0] for f in ext_list]

if __name__ == "__main__":
    print("Loading dependencies...")
    for ext in ext_name_list:
        bot.load_extension("cogs." + ext)

bot.run(BOT_TOKEN)
