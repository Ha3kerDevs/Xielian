import discord
import aiohttp
import asyncio
import random
from typing import Optional
from cogs.utils import checks
from discord.ext import commands
from setup_bot import StellaricBot
  
# <:banaa:831766861615333387>\u2800

class Fun(commands.Cog, name="Fun"):
  
  def __init__(self, bot: StellaricBot):
    self.bot = bot

  #@checks.in_right_channel()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name='slap',
    help="Slap someone or yourself!",
    usage='(user)'
  )
  async def _slap(self, ctx, user: Optional[discord.Member]):
    async with aiohttp.ClientSession() as cs:
      async with cs.get("https://purrbot.site/api/img/sfw/slap/gif") as r:
        res = await r.json()
    img = res['link']
    if user is None:
      embed = discord.Embed(title="Slap", description=f"**{ctx.author.name}** slapped **Themselves**!", color=0xf8c7c7)
    else:
      embed = discord.Embed(title="Slap", description=f"**{ctx.author.name}** slapped **{user.name}**!", color=0xf8c7c7)
    embed.set_footer(text="Stellaric | If the image/gif is not loading, try again.")
    embed.set_image(url=img)
    await ctx.send(embed=embed)

  #@checks.in_right_channel()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name='hug',
    help="Hug someone or yourself!",
    usage='(user)'
  )
  async def _hug(self, ctx, user: Optional[discord.Member]):
    async with aiohttp.ClientSession() as cs:
      async with cs.get("https://purrbot.site/api/img/sfw/hug/gif") as r:
        res = await r.json()
    img = res['link']
    if user is None:
      embed = discord.Embed(title="Hug", description=f"**{ctx.author.name}** hugs **Themselves**!", color=0xf8c7c7)
    else:
      embed = discord.Embed(title="Hug", description=f"**{ctx.author.name}** hugs **{user.name}**!", color=0xf8c7c7)
    embed.set_footer(text="Stellaric | If the image/gif is not loading, try again.")
    embed.set_image(url=img)
    await ctx.send(embed=embed)

  #@checks.in_right_channel()
  @commands.cooldown(1, 5, commands.BucketType.user)
  @commands.guild_only()
  @commands.command(
    name='rps',
    help="Play rock, paper, scissors with the bot.",
    usage='<rock, paper or scissors>'
  )
  async def _rps(self, ctx, user_choice):
    rps = ['rock', 'paper', 'scissors']
    if user_choice.lower() in rps:
      embed = discord.Embed(title="Rock, Paper, Scissors", description=f"**User's Choice:** {user_choice}\n**Bot's Choice:** {random.choice(rps)}", color=0xf8c7c7)
      await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions().none())
    elif user_choice.lower() not in rps:
      await ctx.reply('This command only works with rock, paper, or scissors.', delete_after=6, allowed_mentions=discord.AllowedMentions().none())

  #@checks.in_right_channel()
  @commands.guild_only()
  @commands.command(
    name='coinflip',
    help="Flip a coin!"
  )
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def _coinflip(self, ctx):
    coin = ["Heads", "Tails"]
    a_coin = "<a:Coin:812201969040359454>"
    embed = discord.Embed(title=f"{a_coin} Coinflip", description="Flipping..", color=0xF77733)
    message = await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions().none())
    embed = discord.Embed(title=f"{a_coin} Coinflip", description=f"It land on **{random.choice(coin)}**!", color=0xf8c7c7)

    await asyncio.sleep(3)
    await message.edit(embed=embed)

def setup(bot: StellaricBot):
  bot.add_cog(Fun(bot))