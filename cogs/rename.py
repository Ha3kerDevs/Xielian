import discord
from cogs.utils import config
from discord.ext import commands
from cogs.utils import checks
from cogs.utils import utils

#yes the codes is trash and looks like a spaghet

class Rename(commands.Cog, name="<a:giveawaytada:831766696237727745>\u2800Giveaway Config"):

  def __init__(self, client):
    self.client = client
  
  @commands.has_any_role(
    831149093346476062,
    829605227833065472,
    822428355554312212,
    822728446059741218,
    829630416821551196,
    823814683973779488,
    822727647087165461,
    823048526610038796,
    825584517963055174,
    829253527284875304
    )
  @commands.command(
    name="winner",
    description="Announces the winner of a giveaway.",
    usage='<user>'
  )
  async def _winner(self, ctx, user: discord.Member):
    dot = "<:winnerdot:828915794762792990>"
    dot2 = "<:winnerdot2:828915745399242773>"
    line = "<:winnerline:828915722339745794>"
    plus = "<:winnerplus:828915821131989004>"
    info = "<:winnerinfo:828915771198930984>"
    finalline = f"{dot2} {line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line} {dot2}"
    await ctx.send(
    f"╭ {plus} ・ [ {user.mention} ] **won!** Ask them if we're Legit\n"
    f"{finalline}\n "
    f"\u2800{info} ・TIPS :\n"
    f"\u2800{dot} Be fast when coming to giveaways\n"
    f"\u2800{dot} Join the required server\n"
    f"\u2800{dot} Stay in the channel to not get rerolled\n"
    f"{finalline}\n"
    f"╰ {plus} ・Stay in **Stellaric** for more!"
    )
    await ctx.message.delete()
  
  @commands.has_any_role(
    831149093346476062,
    829605227833065472,
    822428355554312212,
    822728446059741218,
    829630416821551196,
    823814683973779488,
    822727647087165461,
    823048526610038796,
    825584517963055174,
    823048690058526730,
    823048862821777438,
    823372056409800724,
    829253527284875304,
    826833464401330177
  )
  @commands.cooldown(1, 2, commands.BucketType.user)
  @commands.group(pass_context=True, invoke_without_command=True,
    name="winlog",
    description="logs the winner of a giveaway.",
    usage="<drop, giveaway or event> <user> <item>"
  )
  async def _winlog(self, ctx):
    await ctx.send(f"Please use the following arguments: <drop, giveaway, or event> <user> then then an item that the user won\nExample: `{ctx.prefix}winlog drop @TheHa3ker 200 robux`")

  @commands.has_any_role(
    831149093346476062,
    829605227833065472,
    822428355554312212,
    822728446059741218,
    829630416821551196,
    823814683973779488,
    822727647087165461,
    823048526610038796,
    825584517963055174,
    823048690058526730,
    823048862821777438,
    823372056409800724,
    829253527284875304,
    826833464401330177
  )
  @_winlog.command()
  async def drop(self, ctx, user: discord.Member, *, arg):
    channel = user.guild.get_channel(831133427159400468)
    text = arg.upper()

    await ctx.send(f"[ {user.mention} ] Claimed **{text}** from drops")
    await utils.post_winlog_log(gtype = "Drop", user=user, text=text, author=ctx.author)
    await ctx.message.delete()
  
  @commands.has_any_role(
    831149093346476062,
    829605227833065472,
    822428355554312212,
    822728446059741218,
    829630416821551196,
    823814683973779488,
    822727647087165461,
    823048526610038796,
    825584517963055174,
    823048690058526730,
    823048862821777438,
    823372056409800724,
    829253527284875304,
    826833464401330177
  )
  @_winlog.command()
  async def giveaway(self, ctx, user: discord.Member, *, arg):
    text = arg.upper()
    
    await ctx.send(f"[ {user.mention} ] Claimed **{text}** from giveaway")
    await utils.post_winlog_log(gtype = "Giveaway", user=user, text=text, author=ctx.author)
    await ctx.message.delete()

  @commands.has_any_role(
    831149093346476062,
    829605227833065472,
    822428355554312212,
    822728446059741218,
    829630416821551196,
    823814683973779488,
    822727647087165461,
    823048526610038796,
    825584517963055174,
    823048690058526730,
    823048862821777438,
    823372056409800724,
    829253527284875304,
    826833464401330177
  )
  @_winlog.command()
  async def event(self, ctx, user: discord.Member, *, arg):
    text = arg.upper()

    await ctx.send(f"[ {user.mention} ] Claimed **{text}** from event")
    await utils.post_winlog_log(gtype = "Event", user=user, text=text, author=ctx.author)
    await ctx.message.delete()


def setup(client):
    client.add_cog(Rename(client))