import logging

from discord.ext import commands

from modules.commands.loader import load_commands

from . import config
from .database import DatabaseManager
from .services import ServiceManager

logger = logging.getLogger(__name__)


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config.PREFIXES, intents=config.INTENTS)
        self.db = DatabaseManager()

    async def setup_hook(self):

        await self.db.connect()
        await self.db.create_tables()

        logger.info("Database initialized")
        self.services = ServiceManager(self)

        await self.load_extension("modules.events.cog")
        await load_commands(self)

    async def on_ready(self):
        logger.info(f"Online como {self.user}")

    def run(self):
        super().run(config.TOKEN)
