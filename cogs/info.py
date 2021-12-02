import discord, time
import datetime
from cogs.utils import checks, config, utils
from discord.ext import commands
from discord.utils import get
from typing import Optional
from setup_bot import StellaricBot


# <:infooo:831769439543623712>\u2800

class Info(commands.Cog, name="Information"):
  """
  Information about a user, the bot, etc.
  """

  def __init__(self, bot: StellaricBot):
    self.bot = bot


  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name="whois",
    help="Check your or a person's server information.",
    #usage='[user]'
  )
  async def _whois(self, ctx, user: Optional[discord.Member] = commands.Option(description="Enter a username/userid")):
    user = user or ctx.author
    checkmark = "<:checkmark:815484488757805076>"
    crossmark = "<:crossmark:815484561180983336>"
    roles = [role for role in user.roles]
    # _____ Badges _____

    balance = get(self.bot.emojis, id=815124115433193492)
    brilliance = get(self.bot.emojis, id=815124230701056011)
    bravery = get(self.bot.emojis, id=815124160043810846)
    hypesquad = get(self.bot.emojis, id=815124571070005258)
    partner = get(self.bot.emojis, id=815125503547670529)
    early = get(self.bot.emojis, id=815126086585024522)
    staff = get(self.bot.emojis, id=815126355725123614)
    verifiedbotdev = get(self.bot.emojis, id=815128557066911744)
    bughunterlvl1 = get(self.bot.emojis, id=815128921866502165)
    bughunterlvl2 = get(self.bot.emojis, id=815128943723937792)
    badges = ''

    if user.public_flags.verified_bot_developer \
      or user.public_flags.early_verified_bot_developer \
      or user.public_flags.verified_bot:
      badges += f"{verifiedbotdev} "
    if user.public_flags.staff:
      badges += f"{staff} "
    if user.public_flags.partner:
      badges += f"{partner} "
    if user.public_flags.bug_hunter:
      badges += f"{bughunterlvl1} "
    if user.public_flags.bug_hunter_level_2:
      badges += f"{bughunterlvl2} "
    if user.public_flags.early_supporter:
      badges += f"{early} "
    if user.public_flags.hypesquad:
      badges += f"{hypesquad} "
    if user.public_flags.hypesquad_balance:
      badges += f"{balance} "
    elif user.public_flags.hypesquad_brilliance:
      badges += f"{brilliance} "
    elif user.public_flags.hypesquad_bravery:
      badges += f"{bravery} "
    
    # _____ Acknowledgements _____
    acknow = ''
    if user.id in config.devs:
      acknow += 'Bot Developer '

    embed = discord.Embed(title="User information",
                  colour=0x9CDFFF,
                  timestamp=datetime.datetime.utcnow())
    
    #embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text=f"User ID: {user.id}")
    # {user.created_at.strftime('%B %d, %Y %I:%M %p UTC')}
    # {user.joined_at.strftime('%B %d, %Y %I:%M %p UTC')}

    embed.add_field(name="General", value=
    f"• **Name:** {str(user)}\n"
    f"• **Display Name:** {user.display_name or 'None'}\n"
    f"• **Registered At:** {utils.timestamp(user.created_at, 'f')}\n"
    f"• **Joined At:** {user.joined_at.strftime('%B %d, %Y %I:%M %p UTC')}\n"
    f"• **Badges:** {badges or 'None'}", inline=False)

    embed.add_field(name=f"Roles [{len(roles[1:]) or ''}]", value=", ".join([role.mention for role in roles[1:]]) or 'None', inline=False)
    
    embed.add_field(name="Acknowledgements", value=f"{acknow or 'Member'}", inline=False)

    embed.add_field(name="Check", value=
    f"• **Bot?** {checkmark if user.bot else crossmark}\n"
    f"• **Boosted?** {checkmark if bool(user.premium_since) else crossmark}", inline=False)

    await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions().none())
  
  @commands.command(
    pass_context=True,
    name="botinfo",
    help="Shows an information about the bot."
  )
  @commands.cooldown(1, 6, commands.BucketType.user)
  async def info(self, ctx):
    info = discord.Embed(title="Bot Information", color=0xf8c7c7)
    info.add_field(name="About", value="Stellaric is a multi-purpose bot made exclusively on Stellaric", inline=False)
    info.add_field(name="Developer", value="TheHa3ker#3080", inline=True)
    info.add_field(name="Version", value="1.0", inline=True)
    info.set_footer(text="Distributed by H Λ 3 K Ξ Я™ | Stellaric")

    await ctx.send(embed=info)


def setup(bot: StellaricBot):
  bot.add_cog(Info(bot))