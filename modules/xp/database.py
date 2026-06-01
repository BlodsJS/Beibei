import aiosqlite


class XPDatabase:
    def __init__(self, db):

        self.db = db

    async def create_user(self, guild_id: str, user_id: str) -> None:
        """
        Create a new user in the database.
        Args:
            guild_id (str): The Discord ID of the guild.
            user_id (str): The Discord ID of the user.
        """

        await self.db.execute(
            """
            INSERT INTO xp_data (
                guild_id,
                user_id
            )
            VALUES (?, ?)
            """,
            (guild_id, user_id),
        )

    async def get_user(self, guild_id: str, user_id: str) -> aiosqlite.Row | None:
        """
        Get a user from the database.
        Args:
            guild_id (str): The Discord ID of the guild.
            user_id (str): The Discord ID of the user.
        Returns:
            aiosqlite.Row | None: The user data, or None if not found.
        """

        return await self.db.fetchone(
            """
            SELECT *
            FROM xp_data
            WHERE guild_id = ? AND user_id = ?
            """,
            (guild_id, user_id),
        )

    async def update_user(
        self, guild_id: str, user_id: str, xp: int, level: int
    ) -> None:
        """
        Update a user's XP and level in the database.
        Args:
            guild_id (str): The Discord ID of the guild.
            user_id (str): The Discord ID of the user.
            xp (int): The user's XP.
            level (int): The user's level.
        """

        await self.db.execute(
            """
            UPDATE xp_data
            SET xp = ?, level = ?
            WHERE guild_id = ? AND user_id = ?
            """,
            (xp, level, guild_id, user_id),
        )

    async def fetch_all(self, query: str, params: tuple = ()) -> list[aiosqlite.Row]:
        """
        Fetch all rows from the database.
        Args:
            query (str): The SQL query to execute.
            params (tuple): The parameters for the query.
        Returns:
            list[aiosqlite.Row]: The list of rows returned by the query.
        """
        return await self.db.fetchall(query, params)
