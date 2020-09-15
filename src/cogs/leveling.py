from discord.ext import commands

class Leveling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def give(self, ctx):
        pass

    @commands.command()
    async def leaderboard(self, ctx):
        pass

    @commands.command()
    async def rank(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Leveling(bot))