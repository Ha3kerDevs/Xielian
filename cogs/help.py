from typing import Optional
import discord
from cogs.utils import checks
from discord.ext import commands
from setup_bot import StellaricBot
  
#icon_url=self.bot.user.avatar_url

import discord
from discord.ext import commands
from discord.errors import Forbidden


async def send_embed(ctx, embed):
    try:
        await ctx.send(embed=embed)
    except Forbidden:
        try:
            await ctx.send("Hey, seems like I can't send embeds. Please check my permissions :)")
        except Forbidden:
            await ctx.author.send(
                f"Hey, seems like I can't send any message in {ctx.channel.name} on {ctx.guild.name}\n"
                f"May you inform the server team about this issue?", embed=embed)


class Help(commands.Cog):
    """
    For a single command (help) lol.
    """

    def __init__(self, bot):
        self.bot = bot



    @commands.cooldown(1, 3, commands.BucketType.user)
    @commands.command(hidden=True, name="help2", description="Shows a list of commands.")
    async def help2(self, ctx, *cmd):
        prefix = self.bot.command_prefix
        if not cmd:
            embed = discord.Embed(title="Stellaric Help Center", description=f"Use `{prefix}help <command>` for help.", color=0x84c2fd)
            embed.set_footer(text="Stellaric | Note: This bot is work in progress.")
        for cog in sorted(self.bot.cogs):
            value = ", ".join(
            f"`{str(command)}`" for command in filter(
            lambda x: not x.hidden, sorted(
                self.bot.get_cog(cog).get_commands(),
                key=lambda y: y.name
            ) 
            )
            )
            if value:
                embed.add_field(name=f"{cog} Commands", value=value, inline=False)
        else:
            if self.bot.get_command(cmd[0].replace(prefix, "")):
                command = self.bot.get_command(cmd[0].replace(prefix, ""))
                name = command.name
                usage = command.usage
                brief = command.brief
                aliases = sorted(command.aliases)
                embed = discord.Embed(title=f"Command: {prefix}{name}", description=f"{command.description}", color=0x2e3136)
                embed.set_footer(text="Stellaric • Arg Usage: <> = Required; [] = Optional",
                icon_url=self.bot.user.avatar_url)
                if usage:
                    embed.add_field(name="Usage", value=f"{prefix}{name} {usage}")
                if aliases:
                    embed.add_field(name="Aliases", value=", ".join(f"{alias}" for alias in aliases))
                if brief:
                    embed.add_field(name="Example", value=f"{prefix}{name} {brief}", inline=True)
            else:
                embed = discord.Embed(
                title="Uh oh!",
                description="Unknown Command",
                color=0xe74c3c
            )
        await ctx.reply(embed=embed, allowed_mentions=discord.AllowedMentions().none())


def setup(bot):
    bot.add_cog(Help(bot))