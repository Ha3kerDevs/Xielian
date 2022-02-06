import discord
import datetime
from cogs.utils import checks, config
from discord.ext import commands
from discord.utils import get
from setup_bot import StellaricBot

class Moderation(commands.Cog, name="Moderation", hidden=True):
  
  def __init__(self, bot: StellaricBot):
    self.bot = bot


def setup(bot: StellaricBot):
  bot.add_cog(Moderation(bot))