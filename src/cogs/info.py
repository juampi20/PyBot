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
        total_roles = len(guild.roles)
        total_users = len(guild.members)
        total_online = len([x for x in guild.members if x.status != discord.Status.offline])
        online = len([x for x in guild.members if x.status == discord.Status.online])
        offline = len([x for x in guild.members if x.status == discord.Status.offline])
        idle = len([x for x in guild.members if x.status == discord.Status.idle])
        dnd = len([x for x in guild.members if x.status == discord.Status.dnd])
        text_channels = len([x for x in guild.channels if isinstance(x, discord.TextChannel)])
        voice_channels = len([x for x in guild.channels if isinstance(x, discord.VoiceChannel)])
        categories = len(guild.channels) - text_channels - voice_channels

        embed = discord.Embed(color=discord.Color.blue())
        embed.set_thumbnail(url=None or guild.icon_url)
        embed.add_field(name="Server Information", inline=False,
        value=f"Owner: {guild.owner}\nVoice region: {guild.region}\nUsers online: {total_online}/{total_users}")
        embed.add_field(name="Channel counts", inline=False,
        value=f"Category channels: {categories}\nText channels: {text_channels}\nVoice channels: {voice_channels}")
        embed.add_field(name="Member counts", inline=False,
        value=f"Members: {total_users}\nRoles: {total_roles}")
        embed.add_field(name="Member statuses", inline=False,
        value=f"🟢 {online}\n🟡 {idle}\n🔴 {dnd}\n")

        # ⚫ {offline}
        # embed.set_author(name=guild.name, icon_url=None or guild.icon_url)
        await ctx.send(embed=embed)
    
def setup(bot):
    bot.add_cog(Info(bot))