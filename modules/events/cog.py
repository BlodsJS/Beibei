from discord.ext import commands

from modules.events.interaction_events import InteractionEvents
from modules.events.message_events import MessageEvents


class EventCog(commands.Cog):
    def __init__(self, bot):

        self.bot = bot

        self.message_events = MessageEvents(bot)
        self.interaction_events = InteractionEvents(bot)

    @commands.Cog.listener()
    async def on_message(self, message):

        await self.message_events.on_message(message)

    @commands.Cog.listener()
    async def on_interaction(self, interaction):
        await self.interaction_events.on_interaction(interaction)


async def setup(bot):

    await bot.add_cog(EventCog(bot))
