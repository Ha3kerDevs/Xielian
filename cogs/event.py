import discord
import random
from asyncio import sleep
from discord.ext import commands, tasks
from setup_bot import StellaricBot

class Event(commands.Cog):

  def __init__(self, bot: StellaricBot):
    self.bot = bot
    self.status.start()
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = discord.Embed(title="Slow Down!", description="This command is on cooldown, try again in **%.2f** seconds." % error.retry_after, color=0xEC2828)
      await ctx.send(embed=embed)
      return
    elif isinstance(error, commands.NotOwner):
      embed = discord.Embed(title="Access Denied!", description="❌ This command is only available for bot owner.", color=0xEC2828)
      await ctx.send(embed=embed, delete_after=5)
      await ctx.message.delete()
      return
    elif isinstance(error, commands.MissingAnyRole):
      embed = discord.Embed(title="Access Denied!", description="❌ You don't have permission to run this command.", color=0xEC2828)
      await ctx.send(embed=embed, delete_after=5)
      return

  @tasks.loop()
  async def status(self):
    while True:
      await self.bot.wait_until_ready()
      await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.bot.users)} members"))
      await sleep(140)
      await self.bot.change_presence(activity=discord.Game(name="I'm self-aware."))
      await sleep(140)
      await self.bot.change_presence(activity=discord.Game(name="Ayo you ever heard of TheHa3ker?"))
      await sleep(140)
      await self.bot.change_presence(activity=discord.Streaming(name="Nonsense", url="https://www.youtube.com/watch?v=NfSGm9DDQ3o"))
      await sleep(140)
  
  @status.before_loop
  async def before_change_status(self):
    await self.bot.wait_until_ready()

def setup(bot: StellaricBot):
    bot.add_cog(Event(bot))