from discord.ext import commands


class XPCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def xp(self, ctx):

        user_id = str(ctx.author.id)
        guild_id = str(ctx.author.guild.id)
        data_user = await self.bot.services.xp.get_user(guild_id, user_id)
        data_profile = await self.bot.services.profile.get_profile(user_id)
        data = {"profile": data_profile, "xp": data_user}

        file = await self.bot.services.ui.card.create_xp_card(
            user=ctx.author, data=data
        )

        await ctx.send(file=file)


async def setup(bot):
    await bot.add_cog(XPCommands(bot))
