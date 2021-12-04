import discord
import datetime
from cogs.utils import checks, config
from discord.ext import commands
from discord.utils import get
from setup_bot import StellaricBot

class TestingQ(commands.Cog, command_attrs=dict(hidden=True), name="Testing"):
  """
  You've managed to find this cog, congrats, now get out.
  """

  def __init__(self, bot: StellaricBot):
    self.bot = bot
  

  @commands.has_any_role(
    793679885285326890,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(hidden=True)
  async def slashdelete(self, ctx, gid: int):
    
    if ctx.author.id == 341837496763678731:
      await self.bot.http.bulk_upsert_guild_commands(self.bot.application_id, gid, [])
      return
    else:
      return
  

  @commands.has_any_role(
    793679885285326890,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(hidden=True)
  async def botmsg(self, ctx, *, msg):
    
    if ctx.author.id == 341837496763678731:
      await ctx.send(f"{msg}")
      await ctx.message.delete()
      return
    else:
      return


  @commands.cooldown(1, 6, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    hidden=True,
    name='tdtest',
    help='TESTING.',
    aliases=['td']
  )
  async def timedif(
      self, ctx, 
      id1: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID1"), 
      id2: Optional[str] = commands.Option(description="PLEASE PRESS TAB WHEN YOU FINISHED PASTING ID2")
    ):
      if ctx.author.id == 341837496763678731:
        continue
      else:
        return

      try:
        if ctx.message.reference is not None:
          if ctx.message.reference.cached_message is None:
            channel = self.bot.get_channel(ctx.message.reference.channel_id)
            id2_a = await channel.fetch_message(ctx.message.reference.message_id)
          else:
            if id2 is not None:
              id2_a = int(id2)
            else:
              return
        id1_a = int(id1)
        #id2_a = int(id2)
          
      except:
          await ctx.send("Check your message ID's! They are incorrect!")
          
      time1 = discord.utils.snowflake_time(int(id1_a))
      time2 = discord.utils.snowflake_time(int(id2_a))
      
      ts_diff = time2 - time1
      secs = abs(ts_diff.total_seconds())
      answer='{} secs'.format(secs)
      
      embed = discord.Embed(title="Time Difference", description=f"Time: {answer}", color=0xf8c7c7)
      await ctx.send(embed=embed)



def setup(bot: StellaricBot):
  bot.add_cog(TestingQ(bot))