from .badges import BADGESView
from .economy import ECONOMYView
from .profile import PROFILEView
from .stats import STATSView


class ProfileRouter:
    def __init__(self, bot):

        self.bot = bot
        self.badges = BADGESView(bot)
        self.stats = STATSView(bot)
        self.economy = ECONOMYView(bot)
        self.profile = PROFILEView(bot)

    async def handle(self, interaction):

        custom_id = interaction.data.get("custom_id", "")
        target_id = custom_id.split(":")[-1]

        data_user = await self.bot.services.xp.get_user(
            str(interaction.user.id), target_id
        )
        data_profile = await self.bot.services.profile.get_profile(target_id)
        data = {"profile": data_profile, "user": data_user}

        if custom_id.startswith("profile:badges"):
            await self.badges.process_badges(interaction, data)

        elif custom_id.startswith("profile:stats"):
            await self.stats.process_stats(interaction, data)
        elif custom_id.startswith("profile:economy"):
            await self.economy.process_economy(interaction, data)

        elif custom_id.startswith("profile:profile"):
            await self.profile.process_profile(interaction, data)
