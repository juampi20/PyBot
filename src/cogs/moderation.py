import discord
from discord.ext import commands
import asyncio
import time

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.is_owner()
    async def purge(self, ctx, limit=50, member: discord.Member = None):
        # Delete message purge
        await ctx.message.delete()

        # Detect pinned messages
        def not_pinned(msg):
            return not msg.pinned

        msg = []
        
        # Verificate if number is integer
        try:
            limit = int(limit)
        except:
            embed = discord.Embed(title="Porfavor, coloque un numero de tipo entero!")
            return await ctx.send(embed=embed, delete_after=5)
        
        # Purge messages if not member
        if not member:
            await ctx.channel.purge(limit=limit, check=not_pinned)
            embed= discord.Embed(title=f"Se eliminaron {limit} mensajes")
            return await ctx.send(embed=embed, delete_after=5)
        
        # If member exists, recollect member's messages
        async for m in ctx.channel.history():
            if len(msg) == limit:
                break
            if m.author == member:
                msg.append(m)
        
        # Purge member's messages
        await ctx.channel.delete_messages(msg)
        embed = discord.Embed(title=f"Se eliminaron {limit} mensajes de {member.mention}")
        await ctx.send(embed=embed, delete_after=5)


    @commands.command()
    @commands.is_owner()
    async def mute(self, ctx):
        await ctx.message.delete()
        connected = ctx.author.voice

        if not connected:
            embed=discord.Embed(title="Debes ingresar un canal de voz!")
            return await ctx.send(embed=embed)
            
        channel = ctx.author.voice.channel
        members = channel.members

        for member in members:
            await member.edit(mute=True)
        
        embed=discord.Embed(title="VOZ SILENCIADA", description="**Es momento de jugar!**  :mute:")
        await ctx.send(embed=embed, delete_after=5)
        
        await asyncio.sleep(300)
        for member in members:
            await member.edit(mute=False)


    @commands.command()
    @commands.is_owner()
    async def unmute(self, ctx):
        await ctx.message.delete()
        connected = ctx.author.voice

        if not connected:
            embed=discord.Embed(title="Debes ingresar un canal de voz!")
            return await ctx.send(embed=embed)
            
        channel = ctx.author.voice.channel
        members = channel.members
        
        for member in members:
            await member.edit(mute=False)
            
        embed=discord.Embed(title="VOZ ACTIVADA", description="**Ahora pueden discutir!**  :loud_sound:")
        await ctx.send(embed=embed, delete_after=5)

def setup(bot):
    bot.add_cog(Moderation(bot))