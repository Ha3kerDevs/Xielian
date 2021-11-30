import discord, time
import datetime
from discord.ext import commands
from cogs.utils import config
from typing import Optional
from cogs.utils import checks
from discord.utils import get

class Utility(commands.Cog, name="<a:utility:831769452344639498>\u2800Utility"):
  
  def __init__(self, client):
    self.client = client




  #@commands.has_any_role()
  @commands.cooldown(1, 6, commands.BucketType.guild)
  @commands.guild_only()
  @commands.command()
  async def nuke(self, ctx):
    exe_start = time.time()
    pos = ctx.channel.position
    await ctx.channel.delete(reason=f"{ctx.channel.name} has been nuked")
    channel = await ctx.channel.clone()
    await channel.edit(position=pos)
    await channel.send(f"Nuke successful. [Execution time: {time.time() - exe_start}]", delete_after=11)

  #@commands.has_any_role()
  @commands.guild_only()
  @commands.command(
    name="membercount",
    description="check how many members in Stellaric.",
    usage=' ',
    aliases=["mc"]
  )
  async def _membercount(self, ctx):
    member_count = len(ctx.guild.members)
    true_member_count = len([m for m in ctx.guild.members if not m.bot])

    embed = discord.Embed(title="Member Count", description=
      f"Total: {member_count}\n"
      f"True Count: {true_member_count}",
      color=0xf8c7c7
    )
    await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions().none())
  
  def time_dif_func(time=False):
    from datetime import datetime
    now = datetime.now()
    if type(time) is int:
      diff = now - datetime.fromtimestamp(time)
    elif isinstance(time,datetime):
      diff = now - time
    elif not time:
      diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
      return ''

    if day_diff == 0:
      if second_diff < 10:
        return "just now"
      if second_diff < 60:
        return str(second_diff) + " seconds ago"
      if second_diff < 120:
        return "a minute ago"
      if second_diff < 3600:
        return str(second_diff / 60) + " minutes ago"
      if second_diff < 7200:
        return "an hour ago"
      if second_diff < 86400:
        return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
      return "Yesterday"
    if day_diff < 7:
      return str(day_diff) + " days ago"
    if day_diff < 31:
      return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
      return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"

  #@commands.has_any_role()
  @commands.command()
  async def timedif(self, ctx, obj: discord.Object):
    await ctx.send(time_dif_func(obj.created_at))


def setup(client):
  client.add_cog(Utility(client))