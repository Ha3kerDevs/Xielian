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
  
  @commands.command(name='timedif', help='', aliases=['snowflake', 'timediff'])
  async def timedif(self, ctx, id1: int, id2: int):
      try:
        time1 = discord.utils.snowflake_time(int(id1))
        time2 = discord.utils.snowflake_time(int(id2))
          
      except:
          await ctx.send("Check your message ID's! They are incorrect!")
          
      time1 = msg1.created_at
      time2 = msg2.created_at
      
      ts_diff = time2 - time1
      secs = abs(ts_diff.total_seconds())
      days,secs=divmod(secs,secs_per_day:=60*60*24)
      hrs,secs=divmod(secs,secs_per_hr:=60*60)
      mins,secs=divmod(secs,secs_per_min:=60)
      secs=round(secs, 2)
      answer='{} secs'.format(secs)
      
      if secs > 60:
          answer='{} mins and {} secs'.format(int(mins),secs)
          if mins > 60:
              answer='{} hrs, {} mins and {} secs'.format(int(hrs),int(mins),secs)
              if hrs > 24:
                  answer='{} days, {} hrs, {} mins and {} secs'.format(int(days),int(hrs),int(mins),secs)
      
      embed = discord.Embed(title="**Time Difference**", description=f"""IDs: {id1}, {id2}
      Time difference between the 2 IDs: 
      {answer}""")
      await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Utility(client))