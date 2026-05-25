from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent.parent.parent

MODEL = BASE_PATH / "assets"
THEMES = BASE_PATH / "assets/themes"

HOUSES = BASE_PATH / "assets/houses"
themes_db = {
    "profile": {"standart": "profile_model.png"},
    "stats": {"standart": "stats_model.png"},
    "badges": {"standart": "badges_model.png"},
    "economy": {"standart": "economy_model.png"},
    "theme": {"standart": "theme.png"},
}
