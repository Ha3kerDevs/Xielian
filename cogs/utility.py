import discord, time
import datetime
import typing
from discord.ext import commands
from cogs.utils import config
from typing import Optional
from cogs.utils import utils as StellaricUtils
from cogs.utils import checks
from discord.utils import get
from setup_bot import StellaricBot

# 793679885285326890 = Developer (Own Server)
# 797687618007466015 = Moderator (Own Server)
# 822428355554312212 = Founder
# 823814683973779488 = Co-Founder
# 822727647087165461 = Head Admin
# 823048526610038796 = Admin
# 825584517963055174 = Manager
# 823048690058526730 = Head Moderator
# 823048862821777438 = Senior Moderator
# 823372056409800724 = Moderator
# 826833464401330177 = Helper


TIME_DURATION_UNITS = (
  ('month', 2629800),
  ('week', 604800), # 60*60*24*7
  ('day', 86400), # 60*60*24
  ('hour', 3600), # 60*60
  ('min', 60), 
  ('sec', 1)
)

def sec_converter(seconds):
  if seconds == 0:
    return '0'
  parts = []
  for unit, div in TIME_DURATION_UNITS:
    amount, seconds = divmod(int(seconds), div)
    if amount > 0:
      parts.append(f'**{amount}** {unit}{"" if amount == 1 else "s"}')
  return ', '.join(parts)

class EmbedFieldConverter(commands.FlagConverter, prefix='--', delimiter=''):
  name: str
  value: str
  inline: typing.Optional[bool] = True

class TestFlags(commands.FlagConverter, prefix='--', delimiter=''):
  title: str = discord.Embed.Empty
  description: str = discord.Embed.Empty
  color: typing.Optional[discord.Color] = 0xf8c7c7
  field: typing.List[EmbedFieldConverter] = None
  image: str = discord.Embed.Empty


# <a:utility:831769452344639498>\u2800
class Utility(commands.Cog, name="Utility"):
  """
  Utility commands idk :p
  """

  def __init__(self, bot: StellaricBot):
    self.bot = bot

  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.cooldown(1, 6, commands.BucketType.guild)
  @commands.guild_only()
  @commands.command(help="Nukes (Mass purge) a channel. For staff only.")
  async def nuke(self, ctx):
    exe_start = time.time()
    pos = ctx.channel.position
    await ctx.channel.delete(reason=f"{ctx.channel.name} has been nuked")
    channel = await ctx.channel.clone()
    await channel.edit(position=pos)
    await channel.send(f"Nuke successful. [Execution time: {time.time() - exe_start}]", delete_after=5)

  #@commands.has_any_role()
  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name="membercount",
    help="check how many members in Stellaric.",
    aliases=["mc"]
  )
  async def _membercount(self, ctx):
    member_count = len(ctx.guild.members)
    true_member_count = len([m for m in ctx.guild.members if not m.bot])

    embed = discord.Embed(title="Member Count", description=
      f"Total: {member_count}\n"
      f"True Count: {true_member_count}",
      color=0xf8c7c7
    )
    await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions().none())
  
  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name='timedif',
    help="Check the message id's time difference.",
    usage='<id1> <id2>',
    aliases=['td']
  )
  async def _timedif(
      self, ctx, 
      id1: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID1"), 
      id2: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID2")
    ):

      try:
        if ctx.message.reference is not None:
          #channel = self.bot.get_channel(ctx.message.reference.channel_id)
          id2 = ctx.message.reference.message_id
        else:
          if id2 is not None:
            id2 = int(id2)
          else:
            return
        id1 = int(id1)
        #id2_a = int(id2)
          
      except:
          await ctx.send("Check your message ID's! They are incorrect!")
          
      time1 = discord.utils.snowflake_time(int(id1))
      time2 = discord.utils.snowflake_time(int(id2))
      
      ts_diff = time2 - time1
      secs = abs(ts_diff.total_seconds())
      then_send = sec_converter(secs)
      answer='**{}** secs'.format(secs)
      
      embed = discord.Embed(title="Time Difference", description=f"Time: {answer} \nHuman Readable: {then_send or 'I Dunno'}", color=0xf8c7c7)
      await ctx.send(embed=embed)

  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461,
    823048526610038796,
    825584517963055174,
    823048690058526730,
    823048862821777438,
    823372056409800724,
    826833464401330177
  )
  @commands.cooldown(1, 3, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(pass_context=True,
    name="winlog",
    help='logs the winner of a giveaway.',
    usage='<user>, <giveaway type> and <item>',
  )
  async def _winlog(self, ctx, user: discord.Member, gtype, *, item):
    channel = user.guild.get_channel(831133427159400468)
    text = item.upper()
    #thenlog = discord.Embed(
    #  title=f"Win log",
    #  description=f"**Got Logged:** {str(user)} [`{user.id}`]\n"
    #  f"**Giveaway Type | Item:** `{gtype}` | `{text}`\n"
    #  f"**Responsible:** {ctx.author.mention}",
    #  color=0xf8c7c7
    #)
    #auditlog.set_thumbnail(url=user.avatar_url)
    #thenlog.set_footer(text=f"Stellaric Logs | Author ID: {ctx.author.id}")

    await ctx.send(f"[ {user.mention} ] Claimed **{text}** from {gtype}")

    await ctx.message.delete()
  
  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(
    name="noreq",
    help="Announces the 'no requirement' message."
  )
  async def _noreq(self, ctx):
    
    line = "<:sl_blueline:915258046660354078>"
    dot2 = "<:s_dots:915257866468868146>"
    horn = "<:s_horn:915257645848473650>"
    gift = "<:s_gift:915257902145617981>"

    finalline = f"{dot2} {line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line} {dot2}"
    await ctx.send(
    f"╭ {gift} **NO REQUIREMENTS, ENJOY!**\n"
    f"{finalline}\n "
    f"{horn} **TIPS:**\n"
    f"{dot2} Putting **Stellaric** at the top of your server list will help you see our pings easily!\n"
    f"{dot2} Make sure to **prioritize our pings** so you won't miss any giveaways!\n"
    f"{dot2} Be active in Stellaric for more!\n"
    f"{finalline}\n"
    f"╰ {gift} **Stay in Stellaric for more giveaways like this!**"
    )
    await ctx.message.delete()


  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(
    name="winner",
    help="Announces the winner of a giveaway.",
    usage="<user> <item>"
  )
  async def _winner(self, ctx, user: discord.Member, *, item):
    text_upper = item.upper()
    
    line = "<:sl_blueline:915258046660354078>"
    dot2 = "<:s_dots:915257866468868146>"
    guide = "<:s_guide:915257977005539418>"
    gift = "<:s_gift:915257902145617981>"
    vouch_channel = "<#823515781341642802>"

    finalline = f"{dot2} {line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line}{line} {dot2}"
    
    await ctx.send(
    f"╭ {gift} [ {user.mention} ] won **{text_upper}**! You may ask them if we're legit\n"
    f"{finalline}\n "
    f"{guide} Never want to miss a giveaway? If so follow all **TIPS:** listed below:\n"
    f"{dot2} Drag us above all other servers to help see our pings much more easier.\n"
    f"{dot2} Make sure to prioritize pings from **Stellaric** so you won't miss any giveaways!\n"
    f"{dot2} Make **Stellaric** as your main server if you want tons of Events and Giveaways\n"
    f"{finalline}\n"
    f"╰ {gift} We are Legit! You can check {vouch_channel} for our Legitimacy!"
    )
    await ctx.message.delete()

  @commands.has_any_role(
    793679885285326890,
    797687618007466015,
    822428355554312212,
    823814683973779488,
    822727647087165461
  )
  @commands.command(
    slash_command=False,
    name="embed",
    help="Type `s!embed` (no args) for the actual instructions."
  )
  async def embed(self, ctx: commands.Context, *, flags: TestFlags):
    embed = discord.Embed(title=flags.title, description=flags.description, colour=flags.color)
    if flags.field and len(flags.field) > 25:
      raise commands.BadArgument('You can only have up to 25 fields!')
    for f in flags.field or []:
      embed.add_field(name=f.name, value=f.value, inline=f.inline)
    if flags.image:
      embed.set_image(url=flags.image)
    if any([flags.title, flags.image, flags.description, flags.field]):
      await ctx.send(embed=embed)
    else:
      text_damn = """
      **Available flags:**
      `--title [text*]` Sets the embed title.
      `--description [text*]` Sets the embed body/description.
      `--color [color]` Sets the embed's color.
      `--image [http/https URL*]` Sets the embed's image.
      `--field...(25) [FieldFlags*]` Sets one of the embed's fields using field flags.
      **FieldFlags:**
      > `--name <text>` Sets that field's name
      > `--value <text>` Sets that field's value / body
      > `--inline [yes/no]` If the field should be in-line (displayed alongside other in-line fields if any)
      **For example:** `--field --name hi hello --value more text --inline no`
      _Note: You can have multiple `--field`(s) using `--name` and `--value` (up to 25)_
      """
      await ctx.send(text_damn)
      # raise commands.BadArgument('You must pass at least one of the necessary (`*`) flags!')


def setup(bot: StellaricBot):
  bot.add_cog(Utility(bot))