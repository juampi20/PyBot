import json
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

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx):
        """Flip a coin and give a result [Heads, Tails]"""
        choices = ("Cara", "Cruz")
        randcoin = random.choice(choices)
        await ctx.send(f"Resultado: `{randcoin}`")

    @commands.command()
    async def embed(self, ctx, *, message):
        """Quick embed messages"""
        await ctx.message.delete()
        embed = discord.Embed(color=random.randint(0, 0xFFFFFF))
        embed.title = message
        await ctx.send(embed=embed)

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, question=None):
        """Ask questions to the 8ball"""
        await ctx.message.delete()
        if not question:
            return await ctx.send("No hay una pregunta.")
        with open("src/data/answers.json", "r") as f:
            choices = json.load(f)
        author = ctx.message.author
        embed = discord.Embed(color=author.color)
        embed.set_author(name=author.name, icon_url=author.avatar_url)
        embed.add_field(name="Tu pregunta:", value=question, inline=False)
        embed.add_field(
            name="Tu respuesta:", value=random.choice(choices), inline=False
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def react(self, ctx):
        """React this message"""
        await ctx.message.add_reaction("😀")


def setup(bot):
    bot.add_cog(Misc(bot))