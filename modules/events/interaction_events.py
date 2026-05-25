class InteractionEvents:
    def __init__(self, bot):

        self.bot = bot

    async def on_interaction(self, interaction):
        if interaction.user.bot:
            return

        guild_id = str(interaction.guild.id)
        user_id = str(interaction.user.id)

        data_profile = await self.bot.services.profile.get_profile(user_id)
        data_user = await self.bot.services.xp.get_user(guild_id, user_id)
        if not data_profile:
            await self.bot.services.profile.db.create_profile(user_id)
            data_profile = await self.bot.services.profile.get_profile(user_id)
        if not data_user:
            await self.bot.services.xp.db.create_user(guild_id, user_id)
            data_user = await self.bot.services.xp.get_user(guild_id, user_id)

        data = {"profile": data_profile, "xp": data_user}

        await self.bot.services.buttons.process_button(interaction)
