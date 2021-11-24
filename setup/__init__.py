import os
import discord
import datetime
from dotenv import load_dotenv
from discord.ext.commands import Bot as client

prefix = "su!"

cogs = [
  "cogs.rename",
  "cogs.event",
  "cogs.help",
  "cogs.utility",
  "cogs.fun",
  "cogs.info"
]

class Client(client):
  def __init__(self):
    self.launch_time = datetime.datetime.now()
    self.prefix = prefix
    super().__init__(command_prefix=prefix, intents=discord.Intents.all())

  def run(self, verison):
    self.version = verison

    load_dotenv()
    TOKEN = os.getenv("T0KEN")
    super().run(TOKEN, reconnect=True)

  async def on_ready(self):
    print("ready")
    for cog in cogs:
      try:
        client.load_extension(cog)
        print(f"{cog} loaded.")
      except Exception as e:
        print(e)


client = Client()
client.remove_command('help')
client.load_extension('jishaku')
