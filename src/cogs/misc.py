import random
import time

import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, *, message):
        """The bot repeats what you write to it"""
        await ctx.message.delete()
        await ctx.send(str(message))

    @commands.command()
    async def ping(self, ctx):
        """Pong!"""
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Pong!  `{int(ping)}ms`")

    @commands.command()
    async def hello(self, ctx):
        """The bot will greet you!"""
        await ctx.send(f"Hola, {ctx.author.mention}!")

    @commands.command()
    async def embed(self, ctx, *, message):
        """Quick embed messages"""
        await ctx.message.delete()
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.description = message
        await ctx.send(embed=embed)

    @commands.command()
    async def react(self, ctx):
        """React this message"""
        await ctx.message.add_reaction("✅")


def setup(bot):
    bot.add_cog(Misc(bot))
