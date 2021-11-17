import discord, time
import datetime
from cogs.utils import checks, config
from discord.ext import commands
from discord.utils import get
from typing import Optional


class Info(commands.Cog, name="<:infooo:831769439543623712>\u2800Information"):
  
  def __init__(self, client):
    self.client = client

  @commands.guild_only()
  @commands.command(
    name="whois",
    description="Check your or a person's server information.",
    usage='[user]'
  )
  async def _whois(self, ctx, user: Optional[discord.Member]):
    user = user or ctx.author
    checkmark = "<:checkmark:815484488757805076>"
    crossmark = "<:crossmark:815484561180983336>"
    roles = [role for role in user.roles]
    # _____ Badges _____

    balance = get(self.client.emojis, id=815124115433193492)
    brilliance = get(self.client.emojis, id=815124230701056011)
    bravery = get(self.client.emojis, id=815124160043810846)
    hypesquad = get(self.client.emojis, id=815124571070005258)
    partner = get(self.client.emojis, id=815125503547670529)
    early = get(self.client.emojis, id=815126086585024522)
    staff = get(self.client.emojis, id=815126355725123614)
    verifiedbotdev = get(self.client.emojis, id=815128557066911744)
    bughunterlvl1 = get(self.client.emojis, id=815128921866502165)
    bughunterlvl2 = get(self.client.emojis, id=815128943723937792)
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
    if any(role.id in config.leader_roles for role in user.roles):
      acknow += 'Administrator '

    embed = discord.Embed(title="User information",
                  colour=0x9CDFFF,
                  timestamp=datetime.datetime.utcnow())
    
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text=f"User ID: {user.id}")

    embed.add_field(name="General", value=
    f"• **Name:** {str(user)}\n"
    f"• **Display Name:** {user.display_name or 'None'}\n"
    f"• **Registered At:** {user.created_at.strftime('%B %d, %Y %I:%M %p UTC')}\n"
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
    description="Shows an information about the bot.",
    usage=" "
  )
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def info(self, ctx):
    info = discord.Embed(title="Bot Information", color=0xf8c7c7)
    info.add_field(name="About", value="Stellaric is a multi-purpose bot made in Python. (more bot info soon.)", inline=False)
    info.add_field(name="Developer", value="TheHa3ker#3080", inline=True)
    info.add_field(name="Version", value="1.0", inline=True)
    info.set_footer(text="Powered by H Λ 3 K Ξ Я™ | Stellaric")

    await ctx.send(embed=info)

  @commands.command(
    pass_context=True,
    name="userclaimtime",
    description="Shows an information about the bot.",
    aliases=["uct"],
    usage="[user]"
  )
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def _usertimereq(self, ctx, user: Optional[discord.Member]):
    user = user or ctx.author
    totalreq = 0
    textdescription = ''
    member_add = 10
    voter_add = 2
    voter5_add = 3
    voter10_add = 5
    soldier_add = 3
    captain_add = 5
    baron_add = 8
    supporter_add = 3
    donator_add = 5
    booster_add = 5
    member = discord.utils.get(ctx.guild.roles, id=827443212821069845)
    voter = discord.utils.get(ctx.guild.roles, id=826449210773340190)
    voter5 = discord.utils.get(ctx.guild.roles, id=826450376798240818)
    voter10 = discord.utils.get(ctx.guild.roles, id=826450377649553418)
    supporter = discord.utils.get(ctx.guild.roles, id=822864955308638228)
    soldier = discord.utils.get(ctx.guild.roles, id=825894284153978941)
    captain = discord.utils.get(ctx.guild.roles, id=825894641550229547)
    baron = discord.utils.get(ctx.guild.roles, id=825894302185160726)
    donator = discord.utils.get(ctx.guild.roles, id=824994570281943050)
    booster = discord.utils.get(ctx.guild.roles, id=822445899208196101)
    if member in user.roles:
      totalreq += member_add
      textdescription += "Member (Default) [10]"
    if supporter in user.roles:
      totalreq += supporter_add
      textdescription += "\nAdding our discord link to status! (Supporter) [+3]"
    if donator in user.roles:
      totalreq += donator_add
      textdescription += "\nDonated to Stellaric! [+5]"
    if booster in user.roles:
      totalreq += booster_add
      textdescription += "\nBoosted Stellaric! [+5]"
    if voter in user.roles:
      totalreq += voter_add
      textdescription += "\nVoted 1 time! [+2]"
    if voter5 in user.roles:
      totalreq += voter5_add
      textdescription += "\nVoted 5 times! [+3]"
    if voter10 in user.roles:
      totalreq += voter10_add
      textdescription += "\nVoted 10 times! [+5]"
    if soldier in user.roles:
      totalreq += soldier_add
      textdescription += "\nUser is a Stellaric Soldier! [+3]"
    if captain in user.roles:
      totalreq += captain_add
      textdescription += "\nUser is a Stellaric Captain! [+5]"
    if baron in user.roles:
      totalreq += baron_add
      textdescription += "\nUser is a Stellaric Baron! [+8]"
    
    embed = discord.Embed(title=f"{str(user)}'s Claim Time", description="Warning: This command is still in the works!", color=0xf8c7c7)
    embed.add_field(name="Claim Times", value=f"{textdescription or 'None'}\n", inline=False)
    embed.add_field(name="Total", value=f"{totalreq}", inline=True)
    await ctx.send(embed=embed)

  # , user: Optional[discord.Member]
  @commands.command(hidden=True)
  async def test(self, ctx):
    await ctx.send("testing permission")
    #user = user or ctx.author
    #if set(user.roles).intersection(config.leader_roles):
    #  print("success")
    #  return
    #else:
    #  print("it didnt work.")
    #  return

def setup(client):
  client.add_cog(Info(client))