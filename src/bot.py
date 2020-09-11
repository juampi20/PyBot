import os
from os import listdir
from os.path import isfile, join
from discord.ext import commands

bot = commands.Bot(command_prefix=commands.when_mentioned_or("_"))

extensions = [f for f in listdir("src/cogs") if isfile(join("src/cogs", f))]
extensions = [f.split('.')[0] for f in extensions]

if __name__ == "__main__":
    print("Loading dependencies...")
    for ext in extensions:
        bot.load_extension("cogs." + ext)

bot.run(os.environ.get("BOT_TOKEN"))
