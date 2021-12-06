import discord
import datetime
import time
import typing
from cogs.utils import config
from discord.ext import commands
from setup_bot import StellaricBot


#async def post_winlog_log(gtype, user, text, author):
#  #channel = user.guild.get_channel(831133427159400468)
#  auditlog = discord.Embed(
#      title=f"Audit log | winlog ({gtype})",
#      description=f"**Got Logged:** {str(user)} [{user.id}] for {text}\n"
#      f"**Responsible:** {author.mention}",
#      color=0xf8c7c7
#    )
#  #auditlog.set_thumbnail(url=user.avatar_url)
#  auditlog.set_footer(text=f"Stellaric Logs | Author ID: {author.id}")
#  await ctx.send(embed = auditlog)

def get_user_badges(user: discord.Member, fetched_user: discord.User = None):
    flags = dict(user.public_flags)

    user_flags = []
    for flag, text in config.USER_FLAGS.items():
        try:
            if flags[flag]:
                user_flags.append(text)
        except KeyError:
            continue
    return ' '.join(user_flags) if user_flags else None

def timestamp(times: datetime.datetime, format: typing.Optional[str] = None):
    if format:
        return f'<t:{int(times.replace(tzinfo=datetime.timezone.utc).timestamp())}:{format}>'
    return f'<t:{int(times.replace(tzinfo=datetime.timezone.utc).timestamp())}>'