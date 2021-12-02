import discord
import datetime
from cogs.utils import config
from discord.ext import commands
from setup_bot import StellaricBot


class Testing(commands.Cog, name="Testing", hidden=True):
    """
    this is for test purposes
    """
  
    def __init__(self, bot: StellaricBot):
        self.bot = bot

    @commands.has_any_role(793679885285326890)
    @commands.command(slash_command=False)
    async def deleteslash(self, ctx, gid: int):
        if author.id == 341837496763678731:
            await self.bot.http.bulk_upsert_guild_commands(self.bot.application_id, gid, [])
            await ctx.message.delete()
            return
        else:
            return
        #await self.bot.http.bulk_upsert_global_commands(self.bot.application_id, [])

def setup(bot: StellaricBot):
  bot.add_cog(Testing(bot))