from modules.buttons.system import ButtonSystem
from modules.profile.system import PROFILESystem
from modules.ui.ui import UIManager
from modules.xp.system import XPSystem


class ServiceManager:
    def __init__(self, bot):

        self.bot = bot
        self.ui = UIManager()
        self.xp = XPSystem(bot)
        self.profile = PROFILESystem(bot)
        self.buttons = ButtonSystem(bot)
