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

    @commands.command(slash_command=False)
    # @commands.bot_has_permissions(add_reactions=True,embed_links=True)
    async def help(self, ctx, *input):
        """Shows all modules of that bot"""
	
        prefix = "s!"
        version = "v1.0"

        if not input:

            # starting to build embed
            emb = discord.Embed(title='Commands and modules', color=0xf8c7c7,
                                description=f'Use `{prefix}help <module>` to gain more information about that module\n')

            # iterating trough cogs, gathering descriptions
            cogs_desc = ''
            for cog in self.bot.cogs:
                cog.remove('Testing')
                cogs_desc += f'• **{cog}**{self.bot.cogs[cog].__doc__}\n'

            # adding 'list' of cogs to embed
            emb.add_field(name='Modules', value=cogs_desc, inline=False)

            # integrating trough uncategorized commands
            commands_desc = ''
            for command in self.bot.walk_commands():
                # if cog not in a cog
                # listing command if cog name is None and command isn't hidden
                if not command.cog_name and not command.hidden:
                    commands_desc += f'{command.name} - {command.help}\n'

            # adding those commands to embed
            if commands_desc:
                emb.add_field(name='Not belonging to a module', value=commands_desc, inline=False)

            # setting information about author
            emb.add_field(name="About", value=f"This bot is exclusive to Stellaric.")
            emb.set_footer(text=f"TheHa3ker's Product")

        # block called when one cog-name is given
        # trying to find matching cog and it's commands
        elif len(input) == 1:
            # iterating trough cogs
            for cog in self.bot.cogs:
                # check if cog is the matching one
                if cog.lower() == input[0].lower():

                    # making title - getting description from doc-string below class
                    emb = discord.Embed(title=f'{cog} - Commands', description=self.bot.cogs[cog].__doc__,
                                        color=0xf8c7c7)

                    # getting commands from cog
                    for command in self.bot.get_cog(cog).get_commands():
                        # if cog is not hidden
                        if not command.hidden:
                            emb.add_field(name=f"• `{prefix}{command.name}`", value=command.help, inline=False)
                    # found cog - breaking loop
                    break

            # if input not found
            # yes, for-loops have an else statement, it's called when no 'break' was issued
            else:
                emb = discord.Embed(title="What's that?!",
                                    description=f"I've never heard from a module called `{input[0]}`",
                                    color=discord.Color.orange())

        # too many cogs requested - only one at a time allowed
        elif len(input) > 1:
            emb = discord.Embed(title="That's too much.",
                                description="Please request only one module at once",
                                color=discord.Color.orange())

        else:
            emb = discord.Embed(title="It's a magical place.",
                                description="Hello there :p",
                                color=discord.Color.red())

        # sending reply embed using our own function defined above
        await send_embed(ctx, emb)

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