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

    @commands.command(name='help',
                      description='Help command',
                      slash_command=False,
                      case_insensitive=True)
    async def help_command(self, ctx, *commands: str):
        """ Shows this message """
        bottom_info = "[ H Λ 3 K Ξ Я™ ] | Stellaric"
        bot = ctx.bot
        prefix = "s!"
        embed = discord.Embed(title="Stellaric Help Center", description="Arguments: <> = Required | () = Optional", color=0xf8c7c7)

        def generate_usage(command_name):
            """ Generates a string of how to use a command """
            temp = f'{prefix}'
            command = bot.get_command(command_name)
            usage = command.usage
            # Aliases
            if len(command.aliases) == 0:
                temp += f'{command_name}'
            elif len(command.aliases) == 1:
                temp += f'[{command.name}|{command.aliases[0]}]'
            else:
                t = '|'.join(command.aliases)
                temp += f'[{command.name}|{t}]'
            # Parameters
            params = f' '
            #for param in command.clean_params:
            #    params += f'<{command.clean_params[param]}> '
            if usage:
                params += f'{usage}'
            temp += f'{params}'
            return temp

        def generate_command_list(cog):
            """ Generates the command list with properly spaced help messages """
            # Determine longest word
            max = 0
            for command in bot.get_cog(cog).get_commands():
                if not command.hidden:
                    if len(f'{command}') > max:
                        max = len(f'{command}')
            # Build list
            temp = ""
            for command in bot.get_cog(cog).get_commands():
                if command.hidden:
                    temp += ''
                elif command.help is None:
                    temp += f'{command}\n'
                else:
                    temp += f' `{command}`'
                    for i in range(0, max - len(f'{command}') + 1):
                        temp += ''
                    #temp += f'{command.help}\n'
            return temp

        # Help by itself just lists our own commands.
        if len(commands) == 0:
            for cog in bot.cogs:
                temp = generate_command_list(cog)
                if temp != "":
                    embed.add_field(name=f'**{cog}**', value=temp, inline=False)
            if bottom_info != "":
                embed.set_footer(text=bottom_info)
        elif len(commands) == 1:
            # Try to see if it is a cog name
            name = commands[0].capitalize()
            command = None

            if name in bot.cogs:
                cog = bot.get_cog(name)
                msg = generate_command_list(name)
                embed.add_field(name=name, value=msg, inline=False)
                msg = f'{cog.description}\n'
                embed.add_field(name="Information", value=msg)
                embed.set_footer(text=bottom_info)

            # Must be a command then
            else:
                command = bot.get_command(name)
                if command is not None:
                    help = f''
                    if command.help is not None:
                        help = command.help
                    embed.add_field(name=f'**{prefix}{command}**',
                                    value=f'{command.description}```{generate_usage(name)}```\n{help}',
                                    inline=False)
                    embed.set_footer(text=bottom_info)
                else:
                    msg = ' '.join(commands)
                    embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')
        else:
            msg = ' '.join(commands)
            embed.add_field(name="Not found", value=f'Command/category `{msg}` not found.')

        await ctx.send(embed=embed)
        return


def setup(bot):
    bot.add_cog(Help(bot))