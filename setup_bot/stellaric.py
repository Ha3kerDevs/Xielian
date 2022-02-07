import discord
import os
import aiohttp
from dotenv import load_dotenv
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
            #allowed_mentions=allowed_mentions,
            #activity=activity,
            intents=intents,
            help_command=None,
            slash_commands=True,
            slash_command_guilds=[793679694057701406]
        )
        self.cogs_extensions = [
            "cogs.event",
            "cogs.help",
            "cogs.utility",
            "cogs.testing",
            "cogs.fun",
            "cogs.info",
            "cogs.moderation",
            "jishaku"
        ]
        self.loop.create_task(self.load_extensions())
        self.session = aiohttp.ClientSession()

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
        bot_token = os.getenv("T0KEN")
        super().run(bot_token, reconnect=True)
        
    async def close(self):
        await self.session.close()
        await super().close()
        print("Closed bot.")
