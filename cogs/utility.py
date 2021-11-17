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
 
  @commands.has_any_role(
    822428355554312212,
    831149093346476062,
    829605227833065472,
    822728446059741218,
    823814683973779488,
    825584517963055174
  )
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



def setup(client):
  client.add_cog(Utility(client))