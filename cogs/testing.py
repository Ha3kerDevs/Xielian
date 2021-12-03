import discord
import datetime
from cogs.utils import checks, config
from discord.ext import commands
from discord.utils import get
from setup_bot import StellaricBot

class TestingQ(commands.Cog, command_attrs=dict(hidden=True), name="Testing"):
  """
  You've managed to find this cog, congrats, now get out.
  """

  def __init__(self, bot: StellaricBot):
    self.bot = bot
  

  @commands.has_any_role(
    793679885285326890,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(hidden=True)
  async def slashdelete(self, ctx, gid: int):
    
    if ctx.author.id == 341837496763678731:
      await self.bot.http.bulk_upsert_guild_commands(self.bot.application_id, gid, [])
      return
    else:
      return
  

  @commands.has_any_role(
    793679885285326890,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(hidden=True)
  async def botmsg(self, ctx, *, msg):
    
    if ctx.author.id == 341837496763678731:
      await ctx.send(f"{msg}")
      await ctx.message.delete()
      return
    else:
      return



def setup(bot: StellaricBot):
  bot.add_cog(TestingQ(bot))