from discord.ext import commands
from discord.ext.commands import CommandNotFound

class Events(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot has logged in.")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            await ctx.send("Comando no encontrado!")
            print(error)

    @commands.Cog.listener()
    async def on_message(self, message): 
	    #this line handles the case for the bot itself 
        if message.author == self.bot.user:
            return

    @commands.Cog.listener()
    async def on_voice_state_update(self, ctx, before, after):
        # await ctx.send("Howdy")
        pass

def setup(bot):
    bot.add_cog(Events(bot))