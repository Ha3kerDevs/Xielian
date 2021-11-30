import discord
import os
from discord.ext import commands

os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"

intents = discord.Intents(
    bans=True,
    emojis=True,
    guilds=True,
    messages=True,
    members=True,
    reactions=True,
    webhooks=True,
    voice_states=True
    )

async def get_prefix(bot: "Stellaric", message: discord.Message):
    prefixes = ["s!"]
    return prefixes
  
allowed_mentions = discord.AllowedMentions.none()
  
class StellaricBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            command_prefix=get_prefix,
            case_insensitive=True,
            allowed_mentions=allowed_mentions,
            #activity=activity,
            intents=intents,
        )
        self.cogs_extensions = [
            "cogs.event",
            "cogs.help",
            "cogs.utility",
            "cogs.fun",
            "cogs.info"
        ]
        self.loop.create_task(self.load_extensions())

    async def load_extensions(self):
        for ext in self.cogs_extensions:
            try:
                self.load_extension(ext)
            except commands.ExtensionError as error:
                print(error)
        await self.wait_until_ready()
    
    async def on_ready(self):
        print("Bot online.")
    
    def run(self):

        load_dotenv()
        TOKEN = os.getenv("T0KEN")
        super().run(token, reconnect=True)
        
    async def close(self):
        await super().close()
        print("Closed bot.")
