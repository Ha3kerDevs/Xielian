import discord
from discord.utils import get
from cogs.utils import config
from discord.ext import commands

def in_right_channel():
  async def predicate(ctx):
    if ctx.channel.id in config.channel_ids \
     and any(role.id in config.leader_roles for role in ctx.author.roles):
      return await ctx.send("Uh oh! Looks like you runned the command on the wrong channel")
    else:
      return True
  return commands.check(predicate)

#def in_giveaway_channel():
#  async def predicate(ctx):
#    if ctx.channel.id not in config.giveaway_channel_ids \
#     and ctx.author.id not in config.devs \
#     and ctx.author.id not in config.leader_roles:
#      raise await ctx.send("Uh oh! Looks like you runned the command on the wrong channel")
#    else:
#      return True
#  return commands.check(predicate)