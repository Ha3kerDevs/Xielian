import discord, time
import datetime
from discord.ext import commands
from cogs.utils import config
from typing import Optional
from cogs.utils import utils as StellaricUtils
from cogs.utils import checks
from discord.utils import get
from setup_bot import StellaricBot

# 793679885285326890 = Developer (Own Server)
# 797687618007466015 = Moderator (Own Server)
# 822428355554312212 = Founder
# 823814683973779488 = Co-Founder
# 822727647087165461 = Head Admin

# <a:utility:831769452344639498>\u2800
class Utility(commands.Cog, name="Utility"):
  """
  Utility commands idk :p
  """
  
  def __init__(self, bot: StellaricBot):
    self.bot = bot

  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.cooldown(1, 6, commands.BucketType.guild)
  @commands.guild_only()
  @commands.command(help="Nukes a channel. For staff only.")
  async def nuke(self, ctx):
    exe_start = time.time()
    pos = ctx.channel.position
    await ctx.channel.delete(reason=f"{ctx.channel.name} has been nuked")
    channel = await ctx.channel.clone()
    await channel.edit(position=pos)
    await channel.send(f"Nuke successful. [Execution time: {time.time() - exe_start}]", delete_after=11)

  #@commands.has_any_role()
  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name="membercount",
    help="check how many members in Stellaric.",
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
  
  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(
    name='timedif',
    help='For staff only.',
    usage='<id1> <id2>',
    aliases=['td']
  )
  async def timedif(
      self, ctx, 
      id1: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID1"), 
      id2: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID2")
    ):
      try:
        id1 = int(id1)
        id2 = int(id2)
          
      except:
          await ctx.send("Check your message ID's! They are incorrect!")
          
      time1 = discord.utils.snowflake_time(int(id1))
      time2 = discord.utils.snowflake_time(int(id2))
      
      ts_diff = time2 - time1
      secs = abs(ts_diff.total_seconds())
      answer='{} secs'.format(secs)
      
      embed = discord.Embed(title="Time Difference", description=f"Time: {answer}", color=0xf8c7c7)
      await ctx.send(embed=embed)

  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.command(pass_context=True, invoke_without_command=True,
    name="winlog",
    help="logs the winner of a giveaway.",
    usage='<user>, <gtype> and <item>',
  )
  async def _winlog(self, ctx, user: discord.Member, gtype, *, arg):
    channel = user.guild.get_channel(831133427159400468)
    text = arg.upper()
    #thenlog = discord.Embed(
    #  title=f"Win log",
    #  description=f"**Got Logged:** {str(user)} [`{user.id}`]\n"
    #  f"**Giveaway Type | Item:** `{gtype}` | `{text}`\n"
    #  f"**Responsible:** {ctx.author.mention}",
    #  color=0xf8c7c7
    #)
    #auditlog.set_thumbnail(url=user.avatar_url)
    #thenlog.set_footer(text=f"Stellaric Logs | Author ID: {ctx.author.id}")

    await ctx.send(f"[ {user.mention} ] Claimed **{text}** from {gtype}")

    await ctx.message.delete()



def setup(bot: StellaricBot):
  bot.add_cog(Utility(bot))