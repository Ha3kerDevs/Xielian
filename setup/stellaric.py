import discord
import os

os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"






async def get_prefix(bot: "Stellaric", message: discord.Message):
    prefixes = ["s!"]
    return prefixes

  
  
class StellaricBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            command_prefix=get_prefix,
            case_insensitive=True,
            allowed_mentions=allowed_mentions,
            activity=activity,
            intents=intents,
        )
        self.cogs = [
            "cogs.event",
            "cogs.help",
            "cogs.utility",
            "cogs.fun",
            "cogs.info"
        ]
        self.loop.create_task(self.load_extensions())
        
