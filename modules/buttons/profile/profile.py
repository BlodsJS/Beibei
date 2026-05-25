import discord


class PROFILEView:
    def __init__(self, bot):

        self.bot = bot

    async def process_profile(self, interaction, data):
        custom_id = interaction.data.get("custom_id", "")
        target_id = custom_id.split(":")[-1]

        if custom_id.startswith("profile:profile:open"):
            await self.open_profile(interaction, data, target_id)
        elif custom_id.startswith("profile:profile:close"):
            await self.close_profile(interaction)

    async def open_profile(self, interaction, data, target_id):
        target_user = interaction.guild.get_member(int(target_id))
        file = await self.bot.services.ui.profile.create_profile_card(target_user, data)

        new_view = discord.ui.View(timeout=None)

        new_view.add_item(
            discord.ui.Button(
                label="Stats", custom_id=f"profile:stats:open:{target_id}"
            )
        )

        new_view.add_item(
            discord.ui.Button(
                label="Economy", custom_id=f"profile:economy:open:{target_id}"
            )
        )

        new_view.add_item(
            discord.ui.Button(
                label="Bagdes", custom_id=f"profile:badges:open:{target_id}"
            )
        )

        new_view.add_item(
            discord.ui.Button(
                label="Close", custom_id=f"profile:badges:close:{target_id}"
            )
        )

        await interaction.response.edit_message(attachments=[file], view=new_view)

    async def close_profile(self, interaction):
        await interaction.response.edit_message(
            content="Interface fechada.", attachments=[], view=None
        )
