import discord
from discord.ext import commands
import asyncio
import time

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="purge", aliases=["clear", "clean"])
    @commands.is_owner()
    async def _purge(self, ctx, limit=50, member: discord.Member = None):
        """Delete messages"""
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
        
        @commands.command(name='perms', aliases=['perms_for', 'permissions'])
        @commands.guild_only()
        async def check_permissions(self, ctx, *, member: discord.Member=None):
            """A simple command which checks a members Guild Permissions.
            If member is not provided, the author will be checked."""

            if not member:
                member = ctx.author

            # Here we check if the value of each permission is True.
            perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

            # And to make it look nice, we wrap it in an Embed.
            embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
            embed.set_author(icon_url=member.avatar_url, name=str(member))

            # \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
            embed.add_field(name='\uFEFF', value=perms)

            await ctx.send(content=None, embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))