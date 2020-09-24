import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member = None):
        """Return avatar url"""
        member = member or ctx.author
        avatar = member.avatar_url

        embed = discord.Embed(color=discord.Color.blue())
        embed.set_author(name=member, icon_url=avatar, url=str(avatar))
        embed.set_image(url=avatar)
        await ctx.send(embed=embed)

    @commands.command(aliases=["si", "serverinfo", "svi"])
    @commands.guild_only()
    async def server(self, ctx):
        """Get info for the server"""
        guild = ctx.guild
        total_roles = len(guild.roles)
        total_users = len(guild.members)
        total_online = len(
            [x for x in guild.members if x.status != discord.Status.offline]
        )
        online = len([x for x in guild.members if x.status == discord.Status.online])
        offline = len([x for x in guild.members if x.status == discord.Status.offline])
        idle = len([x for x in guild.members if x.status == discord.Status.idle])
        dnd = len([x for x in guild.members if x.status == discord.Status.dnd])
        text_channels = len(
            [x for x in guild.channels if isinstance(x, discord.TextChannel)]
        )
        voice_channels = len(
            [x for x in guild.channels if isinstance(x, discord.VoiceChannel)]
        )
        categories = len(guild.channels) - text_channels - voice_channels

        embed = discord.Embed(color=discord.Color.blue())
        embed.set_thumbnail(url=None or guild.icon_url)

        ret = f"Owner: {guild.owner}\n"
        ret += f"Voice region: {guild.region}\n"
        ret += f"Users online: {total_online}/{total_users}\n"

        embed.add_field(name="Server Information", inline=False, value=ret)

        ret = f"Category channels: {categories}\n"
        ret += f"Text channels: {text_channels}\n"
        ret += f"Voice channels: {voice_channels}\n"

        embed.add_field(name="Channel counts", inline=False, value=ret)

        ret = f"Members: {total_users}\n"
        ret += f"Roles: {total_roles}\n"

        embed.add_field(name="Member counts", inline=False, value=ret)

        ret = f"🟢 {online}\n"
        ret += f"🟡 {idle}\n"
        ret += f"🔴 {dnd}\n"

        embed.add_field(name="Member statuses", inline=False, value=ret)
        # embed.set_author(name=guild.name, icon_url=None or guild.icon_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))