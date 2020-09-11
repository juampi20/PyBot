import discord
from discord.ext import commands
import random

class AmongUsCog(commands.Cog):
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

    # @commands.is_owner()
    @commands.command(aliases=["m"])
    @commands.has_role("Elite")
    async def mute(self, ctx):
        """ Mute all members of the voice channel """
        await ctx.message.delete()
        connected = ctx.author.voice

        if not connected:
            embed=discord.Embed(title="Debes ingresar un canal de voz!")
            return await ctx.send(embed=embed, delete_after=5)
            
        channel = ctx.author.voice.channel
        members = channel.members

        for member in members:
            await member.edit(mute=True)
        
        embed=discord.Embed(title="VOZ SILENCIADA", description="**Es momento de jugar!**  :mute:")
        await ctx.send(embed=embed, delete_after=5)


    # @commands.is_owner()
    @commands.command(aliases=["um"])
    @commands.has_role("Elite")
    async def unmute(self, ctx):
        """ Unmute all members """
        await ctx.message.delete()

        members = ctx.guild.members
        
        for member in members:
            await member.edit(mute=False)

        embed=discord.Embed(title="VOZ ACTIVADA", description="**Ahora pueden discutir!**  :loud_sound:")
        await ctx.send(embed=embed, delete_after=5)

def setup(bot):
    bot.add_cog(AmongUsCog(bot))