import json


class ProfileDatabase:
    def __init__(self, db):

        self.db = db

    async def create_profile(self, user_id):

        await self.db.execute(
            """
            INSERT INTO profile_data (
                user_id
            )
            VALUES (?)
            """,
            (user_id,),
        )

    async def get_profile(self, user_id):

        return await self.db.fetchone(
            """
            SELECT *
            FROM profile_data
            WHERE user_id = ?
            """,
            (user_id,),
        )

    async def set_theme(self, user_id, theme):

        await self.db.execute(
            """
            UPDATE profile_data
            SET theme = ?
            WHERE user_id = ?
            """,
            (theme, user_id),
        )

    async def set_description(self, user_id, description):

        await self.db.execute(
            """
            UPDATE profile_data
            SET description = ?
            WHERE user_id = ?
            """,
            (description, user_id),
        )

    async def set_house(self, user_id, house):

        await self.db.execute(
            """
            UPDATE profile_data
            SET house = ?
            WHERE user_id = ?
            """,
            (house, user_id),
        )

    async def update_badges(self, user_id, badges):

        await self.db.execute(
            """
            UPDATE profile_data
            SET badges = ?
            WHERE user_id = ?
            """,
            (json.dumps(badges), user_id),
        )

    async def add_badge(self, user_id, badge):

        profile = await self.get_profile(user_id)

        badges = json.loads(profile["badges"])

        if badge not in badges:
            badges.append(badge)

            await self.update_badges(user_id, badges)

    async def remove_badge(self, user_id, badge):

        profile = await self.get_profile(user_id)

        badges = json.loads(profile["badges"])

        if badge in badges:
            badges.remove(badge)

            await self.update_badges(user_id, badges)
