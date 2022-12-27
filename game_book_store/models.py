from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class Game(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name = str
    console = str
    category = str
    date: datetime = Field(default_factory=datetime.today)

class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name = str
    password = str
    date: datetime = Field(default_factory=datetime.today)