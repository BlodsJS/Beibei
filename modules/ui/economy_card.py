from easy_pil import Canvas, Editor, Font, load_image_async

from modules.ui import assets, fonts
from modules.ui.utils import error_image, to_bytesio


class ECONOMYCard:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600

    async def create_economy_card(self, user, data):
        try:
            model = "standart"
            model_path = assets.MODEL / assets.themes_db["economy"][model]
            bg = Editor(str(model_path)).resize((self.WIDTH, self.HEIGHT))

            return to_bytesio(bg.image, "economy.webp")
        except Exception as e:
            print(f"[STATS CARD ERROR]\n user [{user.id}]\n erro: {e} ")
            return error_image()
