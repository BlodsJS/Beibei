import textwrap
from pathlib import Path

import discord
from easy_pil import Canvas, Editor, load_image_async
from PIL import ImageDraw

from modules.ui import assets, fonts
from modules.ui.utils import error_image, to_bytesio


class PROFILECard:
    def __init__(self):

        self.WIDTH = 800
        self.HEIGHT = 600

        self.AVATAR_SIZE = (150, 150)

        self.AVATAR_POS = (14, 14)

        self.DESCRIPTION_WIDTH = 31

    async def create_profile_card(
        self,
        user: discord.Member,
        data,
    ):
        theme = data["profile"]["theme"]
        description = data["profile"]["description"]
        house = data["profile"]["house"]
        try:
            theme_path = assets.THEMES / assets.themes_db["theme"][theme]

            bg = Editor(str(theme_path)).resize((self.WIDTH, self.HEIGHT))

            model = Editor(str(assets.MODEL / "bei_model.png")).resize(
                (self.WIDTH, self.HEIGHT)
            )

            bg.paste(model, (0, 0))

            avatar = await load_image_async(user.display_avatar.url)

            avatar = Editor(avatar).resize(self.AVATAR_SIZE).circle_image()

            bg.paste(avatar, self.AVATAR_POS)

            bg.text((170, 19), user.display_name, fonts.TITLE, "white")

            house_path = assets.HOUSES / house

            house_icon = Editor(str(house_path)).resize((40, 41))

            draw = ImageDraw.Draw(bg.image)

            name_width = draw.textlength(user.display_name, font=fonts.TITLE)

            house_pos = (int(name_width) + 180, 13)
            bg.paste(house_icon, house_pos)
            description = description or "..."
            wrapped = textwrap.wrap(description, width=self.DESCRIPTION_WIDTH)

            for index, line in enumerate(wrapped):
                bg.text(
                    (30, 490 + (index * 15)),
                    line,
                    fonts.DESCRIPTION,
                    "white",
                )

            return to_bytesio(bg.image, "profile.webp")
        except Exception as e:
            print(f"[PROFILE CARD ERROR]\n user [{user.id}]\n erro: {e} ")
            return error_image()
