import discord
import datetime
import asyncio
from cogs.utils import checks, config
from discord.ext import commands
from typing import Optional
from discord.utils import get
from setup_bot import StellaricBot
import typing

class EmbedFlags(commands.FlagConverter, prefix='--', delimiter=' '):
  title: str = ""
  description: str = ""
  image: str = ""
  footer: str = ""
  colour: int = 0xf8c7c7

class EmbedFieldConverter(commands.FlagConverter, prefix='--', delimiter=''):
  name: str
  value: str
  inline: typing.Optional[bool] = True

class TestFlags(commands.FlagConverter, prefix='--', delimiter=''):
  title: str = discord.Embed.Empty
  description: str = discord.Embed.Empty
  color: typing.Optional[discord.Color] = 0x000001
  field: typing.List[EmbedFieldConverter] = None
  image: typing.Optional[
    lambda f: re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', f)]

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
      if ctx.message.reference is not None:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
        await message.reply(f"{msg}", allowed_mentions=discord.AllowedMentions().none())
        await ctx.message.delete()
        return
      else:
        await ctx.send(f"{msg}")
        await ctx.message.delete()
        return
    else:
      return

  @commands.has_any_role(
    793679885285326890,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(hidden=True)
  async def timetest(self, ctx, time: int):
    
    if ctx.author.id == 341837496763678731:
      await ctx.send(f"Text start done. Timer: `{time}`")
      await asyncio.sleep(time)
      await ctx.send(f"Text finish done. Timer: `{time}`")
      return
    else:
      return

  @commands.has_any_role(
    793679885285326890,
    822727647087165461
  )
  @commands.guild_only()
  @commands.command(hidden=True)
  async def testembed(self, ctx: commands.Context, channel:Optional[discord.TextChannel], *, message: str):
    if '=' not in message:
      embed_message = discord.Embed(description=message)
    else:
      parser = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

      aliases = {
        'description': ['desc'],
        'colour':['color'],
        'image':['img']
      }
      for x,y in aliases.items():
        if any(alias in message for alias in y):
          for alias in y:
            message = message.replace(alias, x)
      text = f"""
      [DEFAULT]
      {message}
      """
      parser.read_string(text)
      parsed_values = {k:parser['DEFAULT'][k] for k in parser}
      embed_message = discord.Embed(**parsed_values)
    
    if channel:
      await channel.send(embed=embed_message)
      return
    else:
      await ctx.channel.send(embed=embed_message)
      return

  @commands.command()
  async def testembed2(self, ctx, *, flags: EmbedFlags):
          embed = discord.Embed.from_dict({'title': f'{flags.title}',
                                          'description': f'{flags.description}',
                                          'image': {'url': f'{flags.image}'},
                                          'footer': {'text': f'{flags.footer}'},
                                          'color': flags.colour,
                                              })
          await ctx.send(embed=embed)

  @commands.command()
  async def embed(self, ctx: CustomContext, *, flags: TestFlags):
        """
        A test command for trying out the new flags feature in discord.py v2.0
        Flag usage: `--flag [flag string]`
        Note that `--text... [text]` (with ellipsis) can accept a repeated amount of them:
        Like for example, in this case, with the flag `text`:
        `--text hello --text hi how r u --text a third text and so on`
        `--text...(25)` would mean it can have up to 25 different inputs.
        `--text [text*]` would mean that its necessary but not mandatory. AKA if there's multiple of them, you can pass only one and it will work. But you need **at least one of them**

        Flags that have an `=` sign mean that they have a default value.
        for example: `--color [Color=#ffffff]` means the color will be `#ffffff` if it can't find a color in the given input.
        Flags can also be mandatory, for example: `--text <text>`. the `<>` brackets mean it is not optional

        **Available flags:**
        `--title [text*]` Sets the embed title.
        `--description [text*]` Sets the embed body/description.
        `--color [color]` Sets the embed's color.
        `--image [http/https URL*]` Sets the embed's image.
        `--field...(25) [FieldFlags*]` Sets one of the embed's fields using field flags.
        `FieldFlags:`
        > `--name <text>` Sets that field's name
        > `--value <text>` Sets that field's value / body
        > `--inline [yes/no]` If the field should be in-line (displayed alongside other in-line fields if any)
        **For example:** `--field --name hi hello --value more text --inline no`
        _Note: You can have multiple `--field`(s) using `--name` and `--value` (up to 25)_
        """
        embed = discord.Embed(title=flags.title, description=flags.description, colour=flags.color)
        if flags.field and len(flags.field) > 25:
            raise commands.BadArgument('You can only have up to 25 fields!')
        for f in flags.field or []:
            embed.add_field(name=f.name, value=f.value, inline=f.inline)
        if flags.image:
            embed.set_image(url=flags.image[0])
        if any([flags.title, flags.image, flags.description, flags.field]):
            await ctx.send(embed=embed, footer=False, reply=False)
        else:
            raise commands.BadArgument('You must pass at least one of the necessary (`*`) flags!')


def setup(bot: StellaricBot):
  bot.add_cog(TestingQ(bot))