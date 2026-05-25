import discord


class BADGESView:
    def __init__(self, bot):

        self.bot = bot

    async def process_badges(self, interaction, data):
        custom_id = interaction.data.get("custom_id", "")
        target_id = custom_id.split(":")[-1]

        if custom_id.startswith("profile:badges:open"):
            await self.open_badges(interaction, data, target_id)
        elif custom_id.startswith("profile:badges:close"):
            await self.close_badges(interaction)

    async def open_badges(self, interaction, data, target_id):
        target_user = interaction.guild.get_member(int(target_id))
        file = await self.bot.services.ui.badges.create_badges_card(target_user, data)
        new_view = discord.ui.View(timeout=None)

        new_view.add_item(
            discord.ui.Button(
                label="Profile", custom_id=f"profile:profile:open:{target_id}"
            )
        )

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
                label="Close", custom_id=f"profile:badges:close:{target_id}"
            )
        )

        await interaction.response.edit_message(attachments=[file], view=new_view)

    async def close_badges(self, interaction):
        await interaction.response.edit_message(
            content="Interface fechada.", attachments=[], view=None
        )
