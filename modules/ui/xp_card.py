import discord
from easy_pil import Canvas, Editor, Font, load_image_async

from modules.ui import assets, fonts
from modules.ui.utils import error_image, to_bytesio


class XPCard:
    def __init__(self):

        # Tudo visual fica centralizado aqui
        self.WIDTH = 500
        self.HEIGHT = 140

        self.AVATAR_SIZE = (70, 70)

        self.PROGRESS_BAR_WIDTH = 250
        self.PROGRESS_BAR_HEIGHT = 18

        # fontes (simples e reutilizáveis)
        self.font_name = Font.poppins(size=22, variant="bold")
        self.font_body = Font.poppins(size=14)
        self.font_rank = Font.poppins(size=26, variant="bold")

    # ---------------------------
    # util interno
    # ---------------------------

    # ---------------------------
    # XP CARD
    # ---------------------------
    async def create_xp_card(self, user: discord.Member, data) -> discord.File:

        xp = data["xp"]["xp"]
        required_xp = data["xp"]["required_xp"]
        level = data["xp"]["level"]
        rank = data["xp"]["rank"]

        try:
            # canvas base
            # theme_path = assets.THEMES / assets.themes_db["profile"][theme]
            bg = Canvas((self.WIDTH, self.HEIGHT), color="#131515")
            editor = Editor(bg)

            # avatar
            avatar = await load_image_async(user.display_avatar.url)

            avatar = Editor(avatar).resize(self.AVATAR_SIZE).circle_image()

            editor.paste(avatar, (80, 35))

            # textos principais
            editor.text(
                (158, 40), user.display_name, color="white", font=self.font_name
            )

            editor.text(
                (170, 100), f"Level {level}", color="white", font=self.font_body
            )

            editor.text((20, 45), f"#{rank}", color="white", font=self.font_rank)

            editor.text(
                (320, 98),
                f"{xp:,}/{required_xp:,} XP",
                color="white",
                font=self.font_body,
            )

            # barra de progresso
            progress = (xp / required_xp) * 100 if required_xp > 0 else 0

            editor.rectangle(
                (158, 70),
                width=self.PROGRESS_BAR_WIDTH,
                height=self.PROGRESS_BAR_HEIGHT,
                radius=10,
                outline="black",
                stroke_width=2,
            )

            editor.bar(
                (163, 73),
                self.PROGRESS_BAR_WIDTH - 10,
                self.PROGRESS_BAR_HEIGHT - 6,
                progress,
                fill="white",
                radius=10,
            )

            return to_bytesio(editor.image, "xp_card.png")

        except Exception as e:
            print(f"[XP CARD ERROR]\n user [{user.id}]\n erro: {e} ")
            return error_image()
