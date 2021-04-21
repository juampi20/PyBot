import json
import random

import discord
from discord.ext import commands

toggle = True


class AmongUs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["choice", "ch"])
    async def choose(self, ctx, *members: str):
        """ Chooses between multiple choices """
        with open("src/data/amongus.json", "r") as f:
            choices = json.load(f)
        author = ctx.message.author
        embed = discord.Embed(color=author.color)
        embed.set_author(name=author.name, icon_url=author.avatar_url)
        embed.add_field(name="Opciones:", value=(", ".join(members)), inline=False)
        embed.add_field(
            name="Respuesta:",
            value=f"{random.choice(choices)} {random.choice(members)}.",
            inline=False,
        )
        await ctx.send(embed=embed)

    @commands.command(aliases=["m"])
    @commands.has_role("Elite")
    async def mute(self, ctx):
        """Mute and Unmute all in voice channel"""
        global toggle
        if toggle:
            voice_channel = ctx.author.voice.channel
            for user in voice_channel.members:
                if not user.bot:
                    await user.edit(mute=True)
                    toggle = False
            await ctx.message.add_reaction("👌")
        else:
            voice_channel = ctx.author.voice.channel
            for user in voice_channel.members:
                await user.edit(mute=False)
                toggle = True
            await ctx.message.add_reaction("👌")


def setup(bot):
    bot.add_cog(AmongUs(bot))
