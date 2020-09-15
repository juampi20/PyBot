import discord
from discord.ext import commands
import random

toggle = True

class AmongUs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["choice","ch"])
    async def choose(self, ctx, *choices: str):
        """ Chooses between multiple choices """
        msg = [
            "El impostor debe ser",
            "Sospecho de",
            "No creo que sea",
            "Quizas sea",
            "Estoy seguro que es",
            "Lo vi meterse en las alcantarillas a",
            "Lo vi escanearse a",
            "Lo vi tirar la basura a",
            "Vi que no esta haciendo tareas",
            "Me parece que es",
            "Porque yo lo digo! Es"
        ]
        
        embed = discord.Embed(title=f"{random.choice(msg)} {random.choice(choices)}.")
        await ctx.send(embed=embed)


    @commands.command(aliases=["m"])
    @commands.has_role("Elite")
    async def mute(self, ctx):
        """Mute and Unmute all in voice channel"""
        global toggle
        if toggle == True:
            voice_channel = ctx.author.voice.channel
            for user in voice_channel.members:
                if user.bot != True:
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