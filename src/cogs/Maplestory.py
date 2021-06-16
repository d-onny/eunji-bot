import asyncio
import discord
from discord.ext import commands
from discord import Embed

from Eunji import Eunji


class Maplestory(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Maplestory(bot))