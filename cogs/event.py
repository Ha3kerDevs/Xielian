import discord
import random
from asyncio import sleep
from discord.ext import commands, tasks

class Event(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.status.start()
  
  @commands.guild_only()
  @commands.Cog.listener()
  async def on_message(self, message):
    #I'm being extra careful so i put 1 whilelist server. (because it didnt work.)
    if message.guild.id != 822390902835904513:
      return
    #if message.channel.id != 798871981637238784:
     #and message.channel.id != 829045954745335818 \
     #and message.channel.id != 829045954745335818 \
     #and message.channel.id != 829204109344505877:
      #return

    if message.author.id == 294882584201003009:
      #GiveawayBot
      if "Congratulations" in message.content: 
        #Detects when Giveawaybot says the word
        await message.channel.send("<a:timer10s:828906900841955378>") #and Tada
        return

    if "<@!828888459070144532>" in message.content:
      #when user mention the bot
      response = [
        "Ayo you called? Type `su!help` for more info.",
        "Help? Type `su!help`.",
        "Prefix is `su!`. For more info, Type `su!help`."
      ]
      await message.channel.send(f"{random.choice(response)}") # Respond

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
      await self.client.wait_until_ready()
      await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(self.client.users)} members"))
      await sleep(140)
      await self.client.change_presence(activity=discord.Game(name="Stay in Stellaric!"))
      await sleep(140)
      await self.client.change_presence(activity=discord.Game(name="Roblox: 4K UHD"))
      await sleep(140)
      await self.client.change_presence(activity=discord.Streaming(name="Nonsense", url="https://www.youtube.com/watch?v=NfSGm9DDQ3o"))
      await sleep(140)
  
  @status.before_loop
  async def before_change_status(self):
    await self.client.wait_until_ready()

def setup(client):
    client.add_cog(Event(client))