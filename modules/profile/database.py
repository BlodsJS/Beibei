import json


class ProfileDatabase:
    def __init__(self, db):

        self.db = db

    async def create_profile(self, user_id: str) -> None:
        """
        Create a new profile for the given user ID.
        Args:
            user_id (str): The Discord user ID to create a profile for.
        """

        await self.db.execute(
            """
            INSERT INTO profile_data (
                user_id
            )
            VALUES (?)
            """,
            (user_id,),
        )

    async def get_profile(self, user_id: str) -> dict | None:
        """
        Retrieves the profile for the given user ID.
        Args:
            user_id (str): The Discord user ID to retrieve the profile for.
        Returns:
            Row | None:
                The profile data for the given user ID,
                or None if no profile exists.
        """

        return await self.db.fetchone(
            """
            SELECT *
            FROM profile_data
            WHERE user_id = ?
            """,
            (user_id,),
        )

    async def set_theme(self, user_id: str, theme: str) -> None:
        """
        Sets the theme for the given user ID.
        Args:
            user_id (str): The Discord user ID to set the theme for.
            theme (str): The theme to set for the user.
        """

        await self.db.execute(
            """
            UPDATE profile_data
            SET theme = ?
            WHERE user_id = ?
            """,
            (theme, user_id),
        )

    async def set_description(self, user_id: str, description: str) -> None:
        """
        Sets the description for the given user ID.
        Args:
            user_id (str): The Discord user ID to set the description for.
            description (str): The description to set for the user.
        """

        await self.db.execute(
            """
            UPDATE profile_data
            SET description = ?
            WHERE user_id = ?
            """,
            (description, user_id),
        )

    async def set_house(self, user_id: str, house: str) -> None:
        """
        Sets the house for the given user ID.
        Args:
            user_id (str): The Discord user ID to set the house for.
            house (str): The house to set for the user.
        """

        await self.db.execute(
            """
            UPDATE profile_data
            SET house = ?
            WHERE user_id = ?
            """,
            (house, user_id),
        )

    async def update_badges(self, user_id: str, badges: list) -> None:
        """
        Updates the badges for the given user ID.
        Args:
            user_id (str): The Discord user ID to update the badges for.
            badges (list): The list of badges to set for the user.
        """

        await self.db.execute(
            """
            UPDATE profile_data
            SET badges = ?
            WHERE user_id = ?
            """,
            (json.dumps(badges), user_id),
        )

    async def add_badge(self, user_id: str, badge: str) -> None:
        """
        Adds a badge to the user's profile.
        Args:
            user_id (str): The Discord user ID to add the badge to.
            badge (str): The badge to add to the user's profile.
        """

        profile = await self.get_profile(user_id)
        if not profile:
            return

        badges = json.loads(profile["badges"])

        if badge not in badges:
            badges.append(badge)

            await self.update_badges(user_id, badges)

    async def remove_badge(self, user_id: str, badge: str) -> None:
        """
        Removes a badge from the user's profile.
        Args:
            user_id (str): The Discord user ID to remove the badge from.
            badge (str): The badge to remove from the user's profile.
        """

        profile = await self.get_profile(user_id)
        if not profile:
            return

        badges = json.loads(profile["badges"])

        if badge in badges:
            badges.remove(badge)

            await self.update_badges(user_id, badges)
