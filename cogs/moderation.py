import discord
import datetime
from cogs.utils import checks, config
from discord.ext import commands
from discord.utils import get
from setup_bot import StellaricBot, TimeConverter

class Moderation(commands.Cog, name="Moderation"):
  
  def __init__(self, bot: StellaricBot):
    self.bot = bot


  @commands.command(
    name="mute",
    help="Check your or a person's server information.",
    usage="<member>, <duration>, [reason]"
  )
  @commands.has_permissions(moderate_members=True)
  @commands.bot_has_permissions(moderate_members=True)
  async def _mute(self, ctx, member: discord.Member, duration: TimeConverter, reason = None):
    pass

def setup(bot: StellaricBot):
  bot.add_cog(Moderation(bot))