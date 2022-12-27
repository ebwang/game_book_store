from sqlmodel import create_engine, Session
from game_book_store import models
from game_book_store.config import settings

# Ao inves de passar a string passamos o a conf que esta no settings.toml

# Para usar esse parametro tem que importar o config.py onde possui uma implementacao usando o Dynaconf
engine = create_engine(settings.database.url, echo=False)  # NEW

# Ou pode passar a url direto
# engine = create_engine("sqlite:///car.db", echo=False)
models.SQLModel.metadata.create_all(engine)

# NEW
def get_session():
    return Session(engine)
