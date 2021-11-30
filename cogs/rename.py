import discord
from cogs.utils import config
from discord.ext import commands
from cogs.utils import checks
from cogs.utils import utils
from setup_bot import StellaricBot

#yes the codes is trash and looks like a spaghet
# <a:giveawaytada:831766696237727745>\u2800

class Rename(commands.Cog, name="Giveaway Config"):

  def __init__(self, bot: StellaricBot):
    self.bot = bot
  
  #@commands.has_any_role()
  #@commands.command(
  #  name="winner",
  #  description="Announces the winner of a giveaway.",
  #  usage='<user>'
  #)
  #async def _winner(self, ctx, user: discord.Member):
  #  dot = "<:winnerdot:828915794762792990>"
  #  dot2 = "<:winnerdot2:828915745399242773>"
  #  line = "<:winnerline:828915722339745794>"
  #  plus = "<:winnerplus:828915821131989004>"
  #  info = "<:winnerinfo:828915771198930984>"
  #  finalline = f"{dot2} {line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line} {dot2}"
  #  await ctx.send(
  #  f"╭ {plus} ・ [ {user.mention} ] **won!** Ask them if we're Legit\n"
  #  f"{finalline}\n "
  #  f"\u2800{info} ・TIPS :\n"
  #  f"\u2800{dot} Be fast when coming to giveaways\n"
  #  f"\u2800{dot} Join the required server\n"
  #  f"\u2800{dot} Stay in the channel to not get rerolled\n"
  #  f"{finalline}\n"
  #  f"╰ {plus} ・Stay in **Stellaric** for more!"
  #  )
  #  await ctx.message.delete()
  
 #@commands.has_any_role()
  @commands.cooldown(1, 2, commands.BucketType.user)
  @commands.group(pass_context=True, invoke_without_command=True,
    name="winlog",
    description="logs the winner of a giveaway.",
    usage="<drop, giveaway or event> <user> <item>"
  )
  async def _winlog(self, ctx, user: discord.Member, gtype, *, arg):
    #channel = user.guild.get_channel(831133427159400468)
    text = arg.upper()

    await ctx.send(f"[ {user.mention} ] Claimed **{text}** from {gtype}")
    await utils.post_winlog_log(gtype = gtype, user=user, text=text, author=ctx.author)
    await ctx.message.delete()


def setup(bot: StellaricBot):
    bot.add_cog(Rename(bot))