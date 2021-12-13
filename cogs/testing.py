import discord
import datetime
import asyncio
from cogs.utils import checks, config
from discord.ext import commands
from typing import Optional
from discord.utils import get
from setup_bot import StellaricBot
import typing


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
      if ctx.message.reference is not None:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await message.reply(f"{msg}", allowed_mentions=discord.AllowedMentions().none())
        await ctx.message.delete()
        return
      else:
        await ctx.send(f"{msg}")
        await ctx.message.delete()
        return
    else:
      return

  @commands.has_any_role(
    793679885285326890,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(hidden=True)
  async def timetest(self, ctx, time: int):
    
    if ctx.author.id == 341837496763678731:
      await ctx.send(f"Text start done. Timer: `{time}`")
      await asyncio.sleep(time)
      await ctx.send(f"Text finish done. Timer: `{time}`")
      return
    else:
      return


def setup(bot: StellaricBot):
  bot.add_cog(TestingQ(bot))