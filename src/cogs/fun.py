import json
import random

import discord
import pyjokes
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx):
        """Flip a coin and give a result [Heads, Tails]"""
        choices = ("Cara", "Cruz")
        randcoin = random.choice(choices)
        await ctx.send(f"Resultado: `{randcoin}`")

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
    async def joke(self, ctx):
        """Give a joke"""
        await ctx.send(pyjokes.get_joke(language="es", category="all"))


def setup(bot):
    bot.add_cog(Fun(bot))
