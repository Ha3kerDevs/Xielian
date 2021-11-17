import discord
from discord.utils import get
from cogs.utils import config
from discord.ext import commands

def is_helper():
  def predicate(ctx):
    if ctx.author.id not in config.devs \
     and discord.utils.get(ctx.guild.roles(id=config.helper_role)) not in ctx.author.roles \
     and discord.utils.get(ctx.guild.roles(id=config.mod_roles)) in ctx.author.roles:
      raise
    else:
      return True
  return commands.check(predicate)

def is_mod():
  def predicate(ctx):
    if ctx.author.id not in config.devs \
     and discord.utils.get(ctx.guild.roles(id=config.mod_roles)) not in ctx.author.roles:
      raise
    else:
      return True
  return commands.check(predicate)

def is_leader():
  def predicate(ctx):
    if ctx.author.id in config.devs \
     and any(role.id in config.leader_roles for role in ctx.author.roles):
      return True
    else:
      return
  return commands.check(predicate)

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