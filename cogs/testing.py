import discord
import datetime
from cogs.utils import config
from discord.ext import commands
from setup_bot import StellaricBot


class Testing(commands.Cog, name="Testing"):
    """
    this is for test purposes
    """
  
    def __init__(self, bot: StellaricBot):
        self.bot = bot
    
    @commands.has_any_role(793679885285326890)
    @commands.command()
    async def pingslash(
        self, 
        ctx: commands.Context, 
        emoji: bool = commands.Option(description="Slash command testing")):

        if emoji:
            await ctx.send("\U0001f3d3")
        else:
            await ctx.send("Pong!")


def setup(bot: StellaricBot):
  bot.add_cog(Testing(bot))