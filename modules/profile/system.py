from modules.profile.database import ProfileDatabase


class PROFILESystem:
    def __init__(self, bot):
        self.bot = bot
        self.db = ProfileDatabase(bot.db)

    async def get_profile(self, user_id):

        row = await self.db.get_profile(user_id)

        if not row:
            await self.db.create_profile(user_id)

            row = await self.db.get_profile(user_id)

        return dict(row)
