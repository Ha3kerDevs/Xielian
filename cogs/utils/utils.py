import discord
from discord.ext import commands

async def post_winlog_log(ctx, gtype, user, text, author):
  #channel = user.guild.get_channel(831133427159400468)
  auditlog = discord.Embed(
      title=f"Audit log | winlog ({gtype})",
      description=f"**Got Logged:** {str(user)} [{user.id}] for {text}\n"
      f"**Responsible:** {author.mention}",
      color=0xf8c7c7
    )
  #auditlog.set_thumbnail(url=user.avatar_url)
  auditlog.set_footer(text=f"Stellaric Logs | Author ID: {author.id}")
  await ctx.send(embed = auditlog)