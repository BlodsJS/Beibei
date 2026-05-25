from .profile.router import ProfileRouter


class ButtonSystem:
    def __init__(self, bot):

        self.bot = bot

        self.routes = {
            "profile": ProfileRouter(bot),
        }

    async def process_button(self, interaction):

        custom_id = interaction.data.get("custom_id", "")

        route = custom_id.split(":")[0]

        handler = self.routes.get(route)

        if handler:
            await handler.handle(interaction)
