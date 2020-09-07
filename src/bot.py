import os
from discord.ext import commands

bot = commands.Bot(command_prefix="_")

extensions = [
    "misc",
    "events",
    "moderation",
    "summoners",
]

if __name__ == "__main__":
    print("Loading dependencies...")
    for ext in extensions:
        bot.load_extension("cogs." + ext)

bot.run(os.environ.get("BOT_TOKEN"))
