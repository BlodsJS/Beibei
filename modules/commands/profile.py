import discord
from discord.ext import commands


class PROFILECommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #
    @commands.command()
    async def profile(self, ctx):
        try:
            user_id = str(ctx.author.id)
            guild_id = str(ctx.author.guild.id)
            data_profile = await self.bot.services.profile.get_profile(user_id)
            data_user = await self.bot.services.xp.get_user(guild_id, user_id)

            data = {"profile": data_profile, "xp": data_user}

            file = await self.bot.services.ui.profile.create_profile_card(
                user=ctx.author,
                data=data,
            )
            view = discord.ui.View(timeout=None)

            view.add_item(
                discord.ui.Button(
                    label="Stats", custom_id=f"profile:stats:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Economy", custom_id=f"profile:economy:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Badges", custom_id=f"profile:badges:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Close", custom_id=f"profile:profile:close:{ctx.author.id}"
                )
            )

            await ctx.send(file=file, view=view)
        except Exception as e:
            print(f"[PROFILE COMMAND ERROR]\n user [{ctx.author.id}]\n erro: {e}")

    @commands.command()
    async def badges(self, ctx):
        try:
            user_id = str(ctx.author.id)
            guild_id = str(ctx.author.guild.id)
            data_profile = await self.bot.services.profile.get_profile(user_id)
            data_user = await self.bot.services.xp.get_user(guild_id, user_id)

            data = {"profile": data_profile, "xp": data_user}

            file = await self.bot.services.ui.badges.create_badges_card(
                user=ctx.author,
                data=data,
            )
            view = discord.ui.View(timeout=None)

            view.add_item(
                discord.ui.Button(
                    label="Profile", custom_id=f"profile:profile:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Stats", custom_id=f"profile:stats:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Economy", custom_id=f"profile:economy:open:{ctx.author.id}"
                )
            )
            view.add_item(
                discord.ui.Button(
                    label="Close", custom_id=f"profile:profile:close:{ctx.author.id}"
                )
            )

            await ctx.send(file=file, view=view)
        except Exception as e:
            print(f"[BADGES COMMAND ERROR]\n user [{ctx.author.id}]\n erro: {e}")

    @commands.command()
    async def stats(self, ctx):
        try:
            user_id = str(ctx.author.id)
            guild_id = str(ctx.author.guild.id)
            data_profile = await self.bot.services.profile.get_profile(user_id)
            data_user = await self.bot.services.xp.get_user(guild_id, user_id)

            data = {"profile": data_profile, "xp": data_user}

            file = await self.bot.services.ui.badges.create_badges_card(
                user=ctx.author,
                data=data,
            )
            view = discord.ui.View(timeout=None)

            view.add_item(
                discord.ui.Button(
                    label="Profile", custom_id=f"profile:profile:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Economy", custom_id=f"profile:economy:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Badges", custom_id=f"profile:badges:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Close", custom_id=f"profile:profile:close:{ctx.author.id}"
                )
            )

            await ctx.send(file=file, view=view)
        except Exception as e:
            print(f"[STATS COMMAND ERROR]\n user [{ctx.author.id}]\n erro: {e}")

    @commands.command()
    async def economy(self, ctx):
        try:
            user_id = str(ctx.author.id)
            guild_id = str(ctx.author.guild.id)
            data_profile = await self.bot.services.profile.get_profile(user_id)
            data_user = await self.bot.services.xp.get_user(guild_id, user_id)

            data = {"profile": data_profile, "xp": data_user}

            file = await self.bot.services.ui.badges.create_badges_card(
                user=ctx.author,
                data=data,
            )
            view = discord.ui.View(timeout=None)

            view.add_item(
                discord.ui.Button(
                    label="Profile", custom_id=f"profile:profile:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Stats", custom_id=f"profile:stats:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Badges", custom_id=f"profile:badges:open:{ctx.author.id}"
                )
            )

            view.add_item(
                discord.ui.Button(
                    label="Close", custom_id=f"profile:profile:close:{ctx.author.id}"
                )
            )

            await ctx.send(file=file, view=view)
        except Exception as e:
            print(f"[ECONOMY COMMAND ERROR]\n user [{ctx.author.id}]\n erro: {e}")


async def setup(bot):

    await bot.add_cog(PROFILECommands(bot))
