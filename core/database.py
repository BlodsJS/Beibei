import logging

import aiosqlite

from . import config

logger = logging.getLogger(__name__)


class DatabaseManager:
    def __init__(self):
        self.connection = None

    async def connect(self):

        self.connection = await aiosqlite.connect(config.DB_PATH)
        self.connection.row_factory = aiosqlite.Row
        await self.connection.execute("PRAGMA foreign_keys = ON")

        logger.info("Database connected")

    async def close(self):

        if self.connection:
            await self.connection.close()
            logger.info("Database closed")

    async def execute(self, query, params=()):

        await self.connection.execute(query, params)
        await self.connection.commit()

    async def fetchone(self, query, params=()):

        async with self.connection.execute(query, params) as cursor:
            return await cursor.fetchone()

    async def fetchall(self, query, params=()):

        async with self.connection.execute(query, params) as cursor:
            return await cursor.fetchall()

    async def create_tables(self):

        await self.execute(
            """
            CREATE TABLE IF NOT EXISTS xp_data (

                guild_id TEXT,
                user_id TEXT,

                level INTEGER DEFAULT 1,
                xp INTEGER DEFAULT 0,

                messages INTEGER DEFAULT 0,
                voice_seconds INTEGER DEFAULT 0,

                PRIMARY KEY (guild_id, user_id)
            )
            """
        )

        await self.execute(
            """
            CREATE TABLE IF NOT EXISTS profile_data (

                user_id TEXT PRIMARY KEY,

                theme TEXT DEFAULT 'standart',
                description TEXT DEFAULT '',
                house TEXT DEFAULT 'cidadao.png',
                badges TEXT DEFAULT '[]'
            )
            """
        )

        logger.info("Tables created")
