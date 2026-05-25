import discord


class STATSView:
    def __init__(self, bot):

        self.bot = bot

    async def process_stats(self, interaction, data):
        custom_id = interaction.data.get("custom_id", "")
        target_id = custom_id.split(":")[-1]
        print(custom_id)
        if custom_id.startswith("profile:stats:open"):
            await self.open_stats(interaction, data, target_id)
        elif custom_id.startswith("profile:stats:close"):
            await self.close_stats(interaction)

    async def open_stats(self, interaction, data, target_id):
        target_user = interaction.guild.get_member(int(target_id))
        file = await self.bot.services.ui.stats.create_stats_card(target_user, data)
        new_view = discord.ui.View(timeout=None)

        new_view.add_item(
            discord.ui.Button(
                label="Profile", custom_id=f"profile:profile:open:{target_id}"
            )
        )

        new_view.add_item(
            discord.ui.Button(
                label="Economy", custom_id=f"profile:economy:open:{target_id}"
            )
        )

        new_view.add_item(
            discord.ui.Button(
                label="Badges", custom_id=f"profile:badges:open:{target_id}"
            )
        )
        new_view.add_item(
            discord.ui.Button(
                label="Close", custom_id=f"profile:stats:close:{target_id}"
            )
        )
        await interaction.response.edit_message(attachments=[file], view=new_view)

    async def close_stats(self, interaction):
        await interaction.response.edit_message(
            content="Interface fechada.", attachments=[], view=None
        )
