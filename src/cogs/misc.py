import discord
from discord.ext import commands
import datetime

class Misc(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def args(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(str(message))

    @commands.command()
    async def ping(self, ctx):
        """Pong!"""
        await ctx.send("Pong!")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello, {ctx.author.name}!")

    @commands.command()
    async def server(self, ctx):
        """Get info for the server"""
        embed = discord.Embed(timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_author(name=f"{ctx.guild.name} - Server Info", icon_url=f"{ctx.guild.icon_url}")
        embed.add_field(name="Server Region:", value=f"`{ctx.guild.region}`", inline=True)
        embed.add_field(name="Server Owner:", value=f"`{ctx.guild.owner}`", inline=True)
        embed.add_field(name="Server ID:", value=f"`{ctx.guild.id}`", inline=False)
        embed.add_field(name="Server created at:", value=f"`{ctx.guild.created_at}`", inline=False)
        embed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        await ctx.send(embed=embed)

    @commands.command()
    async def opgg(self, ctx, *, name):
        """Pull up op.gg for players"""
        if name:
            url = "http://las.op.gg/summoner/userName=" + name.replace(" ", "+")
        else:
            return await ctx.send("Coloque un nickname!")
        
        await ctx.send(url)

def setup(bot):
    bot.add_cog(Misc(bot))