import cassiopeia
import discord
from discord.ext import commands
from objects.player import Player
from riotwatcher import ApiError, LolWatcher
from settings import RIOT_API_TOKEN

watcher = LolWatcher(RIOT_API_TOKEN)
cassiopeia.set_riot_api_key(RIOT_API_TOKEN)
default_region = "la2"


class Summoners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, *, name: str):
        """Display information on a summoner"""
        try:
            player = Player(name)
        except ApiError as err:
            if err.response.status_code == 429:
                print(
                    "We should retry in {} seconds.".format(err.headers["Retry-After"])
                )
                print(
                    "this retry-after is handled by default by the RiotWatcher library"
                )
                print("future requests wait until the retry-after time passes")
            elif err.response.status_code == 404:
                await ctx.send(
                    "Failed to fetch summoner! Error code {}".format(
                        err.response.status_code
                    )
                )
                return
            else:
                raise

        ret = "Name: " + player.name + "\n"
        ret += "Level: " + player.summoner_level
        rank = "Solo/Duo: " + player.solo_rank + "\n"
        rank += "Flex 5v5: " + player.flex_rank

        url = "http://las.op.gg/summoner/userName=" + name.replace(" ", "+")

        # Generate Embed
        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Summoner Info:", value=ret)
        embed.add_field(name="Ranked Info:", value=rank)
        embed.set_author(name=player.name, url=url)
        await ctx.send(embed=embed)

    @commands.command(name="opgg")
    async def get_opgg(self, ctx, *, name):
        """Pull up op.gg for players"""
        if name:
            url = "http://las.op.gg/summoner/userName=" + name.replace(" ", "+")
        else:
            return await ctx.send("Coloque un nickname!")
        await ctx.send(url)


def setup(bot):
    bot.add_cog(Summoners(bot))
