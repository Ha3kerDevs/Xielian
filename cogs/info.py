import discord, time, typing
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

    if user == self.bot.user:
      about = self.bot.get_command("botinfo")
      return await about(ctx)

    checkmark = "<:checkmark:815484488757805076>"
    crossmark = "<:crossmark:815484561180983336>"
    roles = [role for role in user.roles]

    sort = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    pos = f"{sort.index(user) + 1:,}/{len(ctx.guild.members):,}"

    acknow = ''
    if user.id in config.devs:
      acknow += 'Bot Developer'

    embed = discord.Embed(
      title="User information",
      colour=0x9b7474,
      timestamp=datetime.datetime.utcnow()
    )

    embed.set_thumbnail(url=user.display_avatar.url)
    embed.set_footer(text=f"User ID: {user.id}")

    embed.add_field(name="General", value=
    f"• **Name:** {str(user)}\n"
    f"• **Display Name:** {user.display_name or 'None'}\n"
    f"• **Registered At:** {utils.timestamp(user.created_at, 'f')} ({utils.timestamp(user.created_at, 'R')})\n"
    f"• **Joined At:** {utils.timestamp(user.joined_at, 'f')} ({utils.timestamp(user.created_at, 'R')})\n"
    f"• **Position:** {pos}\n"
    f"• **Badges:** {utils.get_user_badges(user) or 'No Badges'}", inline=False)

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
    dev = self.bot.get_user(341837496763678731)
    info = discord.Embed(title="Bot Information", color=0x9b7474)
    info.add_field(name="About", value="Stellaric is a multi-purpose bot made exclusively on Stellaric", inline=False)
    info.add_field(name="Developer", value=f"{dev.mention}", inline=True)
    info.add_field(name="Version", value="1.5", inline=True)
    info.set_footer(text="[ H Λ 3 K Ξ Я™ ] x Stellaric")

    await ctx.send(embed=info)


def setup(bot: StellaricBot):
  bot.add_cog(Info(bot))