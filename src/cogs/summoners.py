import discord
from discord.ext import commands
from requests import HTTPError
from objects.player import Player
from riotwatcher import LolWatcher
import os, datetime, requests, json

watcher = LolWatcher(os.environ.get("RIOT_API_TOKEN"))
default_region = "LA2"

class Summoners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def get_version(self):
        url = "https://ddragon.leagueoflegends.com/api/versions.json"
        response = requests.get(url).json()
        return response[0]

    @commands.command(name='info')
    async def get_summoner(self, ctx, *, name : str):
        """Display information on a summoner"""
        try:
            summoner = Player(str(name))
        except HTTPError as err:
            await ctx.send('Failed to fetch summoner! Error code {}'.format(err.response.status_code))
            return
        
        #summoner.to_string()
        
        version = self.get_version()
        profile_icon_url = f"http://ddragon.leagueoflegends.com/cdn/{version}/img/profileicon/{summoner.profile_icon_id}.png"
        url = "http://las.op.gg/summoner/userName=" + summoner.name.replace(" ", "+")

        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_author(name=f"{summoner.name.lower().capitalize()}", url=url ,icon_url=f"{profile_icon_url}")
        embed.add_field(name="Level", value=f"`{summoner.level}`", inline=False)
        embed.add_field(name="Solo/Duo", value=f"`{summoner.solo_rank}`", inline=False)
        embed.add_field(name="Flex 5v5", value=f"`{summoner.flex_rank}`", inline=False)
        embed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Summoners(bot))
