import os
from dynaconf import Dynaconf


settings = Dynaconf(
    envvar_prefix="GAME_BOOK_STORE",
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml"],
)
