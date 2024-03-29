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
    help="Mute members lol.",
    usage="<member>, <duration>, [reason]"
  )
  @commands.has_permissions(moderate_members=True)
  @commands.bot_has_permissions(moderate_members=True)
  async def _mute(self, ctx, member: discord.Member, duration: TimeConverter, *, reason = None):
    if duration > 2419200 or duration < 60:
      return await ctx.send("Mute time must be over 1 minute and under 28 days.")
    if member.timed_out:
      return await ctx.send(f"{member} is already muted.")
    dur = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=duration)
    reason_log = reason or f"{ctx.author}: No reason provided."
    await member.edit(timeout_until=dur, reason=reason_log)
    embed = discord.Embed(
      title="Muted",
      description=f"<:checkmark:815484488757805076> {member.mention} Has been muted until {discord.utils.format_dt(dur)}.\nReason: ***{reason_log}***",
      color=0x9b7474
      )
    if "-s" in reason_log:
      return await ctx.message.delete()
    else:
      await ctx.message.delete()
      await ctx.send(embed=embed)
      await member.send(f"You have been muted from Stellaric until {discord.utils.format_dt(dur)}. Reason: **{reason_log}**")
      return

  @commands.command(
    name="unmute",
    help="unmute members lol.",
    usage="<member>"
  )
  @commands.has_permissions(moderate_members=True)
  @commands.bot_has_permissions(moderate_members=True)
  async def _unmute(self, ctx, member: discord.Member, *, reason = None):
    reason = reason or f"{ctx.author}: No reason provided."
    await member.edit(timeout_until=None, reason=reason)
    await ctx.send(f"Unmuted **{member}**.")
  
  @commands.command(
    name="clear",
    aliases=['purge'],
    help="Clears X messages.",
    usage="<amount> [user]"
  )
  @commands.has_permissions(manage_messages=True)
  @commands.bot_has_permissions(manage_messages=True)
  @commands.cooldown(1, 2, commands.BucketType.user)
  async def _clear(self, ctx, num: int, target: discord.Member=None):
    if num > 500 or num < 0:
      return await ctx.send("Invalid amount. Maximum is 500.")
    def msgcheck(amsg):
      if target:
        return amsg.author.id == target.id
      return True
    deleted = await ctx.channel.purge(limit=num, check=msgcheck)
    await ctx.send(f'👍 Deleted **{len(deleted)}/{num}** possible messages for you.', delete_after=10)



def setup(bot: StellaricBot):
  bot.add_cog(Moderation(bot))