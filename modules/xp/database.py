class XPDatabase:
    def __init__(self, db):

        self.db = db

    async def create_user(self, guild_id, user_id):

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

    async def get_user(self, guild_id, user_id):

        return await self.db.fetchone(
            """
            SELECT *
            FROM xp_data
            WHERE guild_id = ? AND user_id = ?
            """,
            (guild_id, user_id),
        )

    async def update_user(self, guild_id, user_id, xp, level):

        await self.db.execute(
            """
            UPDATE xp_data
            SET xp = ?, level = ?
            WHERE guild_id = ? AND user_id = ?
            """,
            (xp, level, guild_id, user_id),
        )

    async def fetch_all(self, query, params=()):
        return await self.db.fetchall(query, params)
