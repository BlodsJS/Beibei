import os

from core.bot import MyBot
from core.logger import setup_logger

os_path_bc = os.getcwd()

setup_logger()
# centralized settings

bot = MyBot()
bot.run()
