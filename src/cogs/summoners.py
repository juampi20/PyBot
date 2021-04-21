import datetime

import cassiopeia as cass
import discord
from cassiopeia import Summoner
from discord.ext import commands
from riotwatcher import ApiError, LolWatcher

from src.objects.player import Player
from src.settings import RIOT_API_TOKEN

cass.apply_settings(cass.get_default_config())
cass.set_riot_api_key(RIOT_API_TOKEN)
cass.set_default_region("las")

watcher = LolWatcher(RIOT_API_TOKEN)
default_region = "la2"


class Summoners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, *, name: str):
        """Display information on a summoner"""
        author = ctx.author
        player = None
        try:
            player = Player(name)
        except ApiError as err:
            if err.response.status_code == 429:
                print(
                    f"""We should retry in {err.headers['Retry-After']} seconds
                    this retry-after is handled by default by the RiotWatcher library
                    future requests wait until the retry-after time passes"""
                )
            elif err.response.status_code == 404:
                await ctx.send(
                    f"Failed to fetch summoner! Error code {err.response.status_code}"
                )
                return
            else:
                raise

        ret = f"**Name:** {player.name}\n"
        ret += f"**Level:** {player.summoner_level}\n"

        rank = f"**Solo/Duo:** {player.solo_rank}\n"
        rank += f"**Flex 5v5:** {player.flex_rank}\n"

        url = "https://las.op.gg/summoner/userName=" + name.replace(" ", "+")

        # Generate Embed
        embed = discord.Embed(
            color=discord.Color.blue(), timestamp=datetime.datetime.now()
        )
        embed.set_author(name=player.name, url=url, icon_url=player.icon_url)
        embed.set_footer(text=f"Request by {author.name}", icon_url=author.avatar_url)
        embed.set_thumbnail(url=None or player.icon_url)
        embed.add_field(name="Summoner Info:", value=ret, inline=False)
        embed.add_field(name="Ranked Info:", value=rank, inline=False)
        await ctx.send(embed=embed)

    @commands.command(aliases=["cm", "maestries"])
    async def champ_maestries(self, ctx, *, name: str):
        """Display summoner's champion maestries"""
        author = ctx.author
        s = Summoner(name=name)
        top_champs = ""
        for cm in s.champion_masteries.filter(lambda a: a.level >= 7):
            top_champs += f"{cm.champion.name} ({cm.points} pts)\n"

        embed = discord.Embed(timestamp=datetime.datetime.now())
        embed.set_thumbnail(url=None or s.profile_icon.url)
        embed.set_author(name=s.name, icon_url=s.profile_icon.url)
        embed.set_footer(text=f"Request by {author.name}", icon_url=author.avatar_url)
        embed.add_field(name="Champion Mastery:", value=top_champs, inline=False)
        await ctx.send(embed=embed)

    @commands.command(name="opgg")
    async def get_opgg(self, ctx, *, name):
        """Pull up op.gg for players"""
        if name:
            url = "https://las.op.gg/summoner/userName=" + name.replace(" ", "+")
        else:
            return await ctx.send("Coloque un nickname!")
        await ctx.send(url)


def setup(bot):
    bot.add_cog(Summoners(bot))
