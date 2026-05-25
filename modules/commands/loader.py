# core/services.py ou core/bot.py

import importlib
import os


async def load_commands(bot):
    base = "modules.commands"

    for file in os.listdir("modules/commands"):
        if file.endswith(".py") and file not in ("__init__.py", "loader.py"):
            module_name = f"{base}.{file[:-3]}"
            module = importlib.import_module(module_name)

            if hasattr(module, "setup"):
                await module.setup(bot)
