# Arquivo utilizado para a regra de negocio, logica e demais

from typing import Optional, List
from sqlmodel import select
from game_book_store.db import get_session
from game_book_store.models import Game


def get_games_from_database() -> List[Game]:
    with get_session() as session:
        sql = select(Game)
    return list(session.exec(sql))

def add_game_to_database(
    name: str, category: str, console: str
) -> bool:
    with get_session() as session:
        game = Game(name=name, category=category, console=console)
        session.add(game)
        session.commit()
    return True


#def get_cars_from_database(model: Optional[str] = None) -> List[Car]:
#    with get_session() as session:
#        sql = select(Car)
#        if model:
#            sql = sql.where(Car.model == model)
#        return list(session.exec(sql))
#
#def search_car_from_database(name: str) -> List[Car]:
#    with get_session() as session:
#        sql = select(Car).where(Car.name == name)
#    return list(session.exec(sql))
#
#def remove_car_from_database(name: str) -> bool:
#    with get_session() as session:
#        sql = select(Car).where(Car.name == name)
#        results = session.exec(sql)
#        if results:
#            car_result = results.first()
#            session.delete(car_result)
#            session.commit()
#            return True
#        else:
#            return False
#