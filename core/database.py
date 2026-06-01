import logging

import aiosqlite

from . import config

logger = logging.getLogger(__name__)


class DatabaseManager:
    def __init__(self):
        self.connection = None

    async def connect(self) -> None:
        """
        Connect to the database and set up the connection.
        """

        self.connection = await aiosqlite.connect(config.DB_PATH)
        self.connection.row_factory = aiosqlite.Row
        await self.connection.execute("PRAGMA foreign_keys = ON")

        logger.info("Database connected")

    async def close(self) -> None:
        """
        Close the database connection.
        """

        if self.connection:
            await self.connection.close()
            logger.info("Database closed")

    async def execute(self, query: str, params: tuple = ()) -> None:
        """
        Execute an SQL query and commit the transaction.

        Args:
            query (str):
                SQL statement to execute.

            params (tuple):
                Parameters used by the SQL statement.
        """

        await self.connection.execute(query, params)
        await self.connection.commit()

    async def fetchone(self, query: str, params: tuple = ()) -> aiosqlite.Row | None:
        """
        Fetch a single row from the result of the query.
        Args:
            query (str):
                SQL statement to execute.
            params (tuple):
                Parameters used by the SQL statement.

        Returns:
            aiosqlite.Row | None:
                The first matching row, or None if no row exists..
        """

        async with self.connection.execute(query, params) as cursor:
            return await cursor.fetchone()

    async def fetchall(self, query: str, params: tuple = ()) -> list[aiosqlite.Row]:
        """
        Fetch all rows from the result of the query.
        Args:
            query (str):
                SQL statement to execute.
            params (tuple):
                Parameters used by the SQL statement.
        Returns:
            list[aiosqlite.Row]:
                A list of all matching rows.
        """

        async with self.connection.execute(query, params) as cursor:
            return await cursor.fetchall()

    async def create_tables(self) -> None:
        """
        Create the necessary tables if they do not exist.
        """

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
