from discord.ext import commands
import discord
import datetime

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member=None):
        """Return avatar url"""
        member = member or ctx.author
        avatar = member.avatar_url
        
        embed = discord.Embed(color=discord.Color.blue())
        embed.set_author(name=member, icon_url=avatar, url=str(avatar))
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)

    @commands.command(aliases=['si','serverinfo','svi'])
    @commands.guild_only()
    async def server(self, ctx):
        """Get info for the server"""
        guild = ctx.guild
        total_users = len(guild.members)
        online = len([x for x in guild.members if x.status != discord.Status.offline])
        text_channels = len([x for x in guild.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len([x for x in guild.channels if isinstance(x, discord.VoiceChannel)])
        categories = len(guild.channels) - text_channels - voice_channels

        embed = discord.Embed(color=discord.Color.blue())
        embed.add_field(name="Region", value=guild.region)
        embed.add_field(name="Usuarios", value=f"{online}/{total_users}")
        embed.add_field(name="Canales de Texto", value=text_channels)
        embed.add_field(name="Canales de Voz", value=voice_channels)
        embed.add_field(name="Categorias", value=categories)
        embed.add_field(name="Roles", value=len(guild.roles))
        embed.add_field(name="Dueño", value=guild.owner)
        embed.set_author(name=guild.name, icon_url=None or guild.icon_url)
        embed.set_thumbnail(url=None or guild.icon_url)
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Info(bot))