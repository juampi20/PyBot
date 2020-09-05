import os
from dotenv import load_dotenv
load_dotenv()

from discord.ext import commands

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print("Bot has logged in.")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("BOT_TOKEN"))
