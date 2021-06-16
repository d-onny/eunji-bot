from discord.ext import commands
import discord
import os
from utils.ReadEnv import ReadEnv
from debug import log  # implicit log run


class Eunji(commands.Bot):

    def __init__(self, *args, **kwargs):
        self.command_prefix = "`"
        self.listOfCogs = []
        self.log = log
        self.COGS_DIR = "cogs"

        self._token = ReadEnv().getToken()
        intents = discord.Intents.default()
        intents.invites = False
        intents.webhooks = False
        intents.integrations = False

        super().__init__(command_prefix=self.command_prefix, intents=intents)
    
    async def on_message(self, msg):
        if msg.author.id == self.user.id:
            return
        elif msg.author.bot:
            return
        await self.process_commands(msg)

    def _run(self):
        if self._token:
            self.run(self._token)

    async def on_ready(self):
        self.loadCogs()
        print("Ready now.")

    # COGS
    def setCogs(self):
        COGS_DIRECTORY = "src/cogs"
        for file in os.listdir(COGS_DIRECTORY):
            if file.endswith(".py"):
                # cogString = os.path.join(COGS_DIRECTORY, file).replace(".py", "")
                cogString = file.replace(".py", "")
                self.listOfCogs.append(cogString)

    def loadCogs(self):
        self.setCogs()
        for cog in self.listOfCogs:
            try:
                self.load_extension(f"{self.COGS_DIR}.{cog}")
            except Exception as e:
                self.log.logger.error(e)
