import re
import discord
from discord.ext import commands

time_regex = re.compile(r"(?:(\d{1,5})\s?(h|s|m|d|w|y))+?")
time_dict = {
    "h": 3600,
    "hours": 3600,
    "hour": 3600,
    "s": 1,
    "sec": 1,
    "secs": 1,
    "seconds": 1,
    "m": 60,
    "mins": 60,
    "minutes": 60,
    "min": 60,
    "d": 86400,
    "day": 86400,
    "days": 86400,
    "w": 604800,
    "week": 604800,
    "weeks": 604800,
    "y": 31557600,
    "year": 31557600,
    "years": 31557600,
}

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(f"{value} is an invalid time-key!")
            except ValueError:
                raise commands.BadArgument(f"{key} is not a number!")
        if time < 0:
            raise commands.BadArgument("Time can not be under 1 second")
        return time