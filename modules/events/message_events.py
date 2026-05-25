class MessageEvents:
    def __init__(self, bot):

        self.bot = bot

    async def on_message(self, message):

        if message.author.bot:
            return

        guild_id = str(message.guild.id)
        user_id = str(message.author.id)

        data_profile = await self.bot.services.profile.get_profile(user_id)
        data_user = await self.bot.services.xp.get_user(guild_id, user_id)
        if not data_profile:
            await self.bot.services.profile.db.create_profile(user_id)
            data_profile = await self.bot.services.profile.get_profile(user_id)
        if not data_user:
            await self.bot.services.xp.db.create_user(guild_id, user_id)
            data_user = await self.bot.services.xp.get_user(guild_id, user_id)

        data = {"profile": data_profile, "xp": data_user}
        await self.bot.services.xp.process_message(message, data)
