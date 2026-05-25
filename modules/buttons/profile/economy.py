import discord


class ECONOMYView:
    def __init__(self, bot):

        self.bot = bot

    async def process_economy(self, interaction, data):
        custom_id = interaction.data.get("custom_id", "")
        target_id = custom_id.split(":")[-1]

        print(custom_id)
        if custom_id.startswith("profile:economy:open"):
            await self.open_economy(interaction, data, target_id)
        elif custom_id.startswith("profile:economy:close"):
            await self.close_economy(interaction, data)

    async def open_economy(self, interaction, data, target_id):

        target_user = interaction.guild.get_member(int(target_id))
        file = await self.bot.services.ui.economy.create_economy_card(target_user, data)

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
                label="Badges", custom_id=f"profile:badges:open:{target_id}"
            )
        )

        new_view.add_item(
            discord.ui.Button(
                label="Close", custom_id=f"profile:economy:close:{target_id}"
            )
        )

        await interaction.response.edit_message(attachments=[file], view=new_view)

    async def close_economy(self, interaction, data):
        await interaction.response.edit_message(
            content="Interface fechada.", attachments=[], view=None
        )
