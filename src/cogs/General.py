import asyncio
import discord
from discord.ext import commands
from discord import Embed

from Eunji import Eunji


class General(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_message(self, msg):
    #     if msg.author.bot:
    #         return
    #     ctx = await self.bot.get_context(msg)
    #     await ctx.send(msg.content)

    @commands.command(ignore_extra=False,
                      description="Ping!",
                      help="Pong!",
                      brief="ping pong")
    async def ping(self, ctx) -> None:
        message = await ctx.send("pong here")

    @commands.command()
    async def forjeff(self, ctx) -> None:
        await ctx.send("where is oppa jeff")

    @commands.command()
    async def jeffuWu(self,ctx) -> None:
        await ctx.send("Oppa Jeff saranghaeyo~!")

    @commands.command()
    async def test(self, ctx: commands.Context, prefix: str = "`"):
        bot: Eunji = ctx.bot
        bot.command_prefix = prefix
        await ctx.send(f"Prefix set to {prefix} now.")

    @commands.command(aliases=['embed'])
    async def embed_test(self, ctx):
        e = Embed()
        e.title = 'TITLE'
        e.description = 'DESCRIPTION'
        e.set_thumbnail(url=ctx.author.avatar_url)
        e.add_field(name='Field 1', value='Field 1 Value!')
        e.set_footer(icon_url=ctx.author.avatar_url, text='TEXT!')
        e.set_image(url=ctx.author.avatar_url)
        e.description += 'http://img.ifcdn.com/images/8d30a14342f23ed4e473682477039a6e59f14f80597eb9d049ab7a1dc5b08ea1_1.gif'
        await ctx.send(embed=e)
        await ctx.send('http://img.ifcdn.com/images/8d30a14342f23ed4e473682477039a6e59f14f80597eb9d049ab7a1dc5b08ea1_1.gif')


def setup(bot):
    bot.add_cog(General(bot))
