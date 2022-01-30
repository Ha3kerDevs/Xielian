import discord
import datetime
import asyncio
import typing
from cogs.utils import checks, config, utils
from discord.ext import commands
from typing import Optional, Union
from discord.utils import get
from setup_bot import StellaricBot


class TestingQ(commands.Cog, command_attrs=dict(hidden=True), name="Testing"):
  """
  You've managed to find this cog, congrats, now get out.
  """

  def __init__(self, bot: StellaricBot):
    self.bot = bot
  

  @commands.is_owner()
  @commands.guild_only()
  @commands.command(hidden=True)
  async def slashdelete(self, ctx, gid: int):
    await self.bot.http.bulk_upsert_guild_commands(self.bot.application_id, gid, [])

  
  @commands.is_owner()
  @commands.guild_only()
  @commands.command(hidden=True)
  async def botmsg(self, ctx, *, msg):

    if ctx.message.reference is not None:
      message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
      await message.reply(f"{msg}", allowed_mentions=discord.AllowedMentions().none())
      await ctx.message.delete()
      return
    else:
      await ctx.send(f"{msg}")
      await ctx.message.delete()
      return

  @commands.is_owner()
  @commands.guild_only()
  @commands.command(hidden=True)
  async def timetest(self, ctx, time: int):
    
    await ctx.send(f"Text start done. Timer: `{time}`")
    await asyncio.sleep(time)
    await ctx.send(f"Text finish done. Timer: `{time}`")

  @commands.is_owner()
  @commands.guild_only()
  @commands.command(hidden=True)
  async def outuserinfo(self, ctx, *, user: Union[discord.Member, discord.User] = None):
    userfetch = user or ctx.author
    e = discord.Embed(title="User info", color=0x9b7474)

    user = await self.bot.fetch_user(userfetch.id)

    e.add_field(name='ID', value=userfetch.id, inline=False)
    e.add_field(name='Joined', value=f"{utils.timestamp(user.joined_at, 'f')}", inline=False)
    e.add_field(name='Created', value=f"{utils.timestamp(user.created_at, 'f')}", inline=False)
    e.set_thumbnail(url=user.display_avatar.url)

    await ctx.send(embed=e)

def setup(bot: StellaricBot):
  bot.add_cog(TestingQ(bot))