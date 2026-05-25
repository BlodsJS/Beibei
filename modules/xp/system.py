from modules.xp.box import BOXHandler
from modules.xp.database import XPDatabase
from modules.xp.leveling import LevelHandler


class XPSystem:
    def __init__(self, bot):
        self.box = {"target": 0, "xp": 0}
        self.bot = bot
        self.db = XPDatabase(bot.db)
        self.box_handler = BOXHandler()

    async def process_message(self, message, data):

        guild_id = str(message.guild.id)
        user_id = str(message.author.id)

        box = await self.box_handler.check_box(self.box, data)
        print(data)
        print(f" {data['xp']['xp']}\n {data['xp']['level']}")
        await self.add_xp(guild_id, user_id, data["xp"], 17)

    async def add_xp(self, guild_id, user_id, user_data, amount):
        current_xp = user_data["xp"]
        current_level = user_data["level"]
        new_xp = current_xp + amount

        if new_xp < LevelHandler.required_xp(current_level):
            await self.db.update_user(guild_id, user_id, xp=new_xp, level=current_level)
            return

        while True:
            required_xp = LevelHandler.required_xp(current_level)

            if new_xp <= required_xp:
                break

            new_xp -= required_xp
            current_level += 1

        await self.db.update_user(guild_id, user_id, xp=new_xp, level=current_level)
        return

    async def remove_xp(self, guild_id, user_id, user_data, amount):
        current_level = user_data["level"]
        new_xp = user_data["xp"] + amount

        while True:
            required_xp = LevelHandler.required_xp(current_level)

            if new_xp < required_xp:
                break

            new_xp -= required_xp
            current_level += 1

    async def get_rank(self, guild_id: str, user_id: str) -> int:

        query = """
            SELECT user_id
            FROM xp_data
            WHERE guild_id = ?
            ORDER BY xp DESC
        """

        rows = await self.db.fetch_all(query, (guild_id,))

        for index, row in enumerate(rows, start=1):
            if str(row["user_id"]) == str(user_id):
                print("encontrado")
                return index
            print(f"Usario não encontrado: {row['user_id']}")
        return 0

    async def get_user(self, guild_id, user_id):

        row = await self.db.get_user(guild_id, user_id)
        if not row:
            await self.db.create_user(guild_id, user_id)
            row = await self.db.get_user(guild_id, user_id)
        data = dict(row)
        data["required_xp"] = LevelHandler.required_xp(data["level"])
        data["rank"] = await self.get_rank(guild_id, user_id)

        return data
