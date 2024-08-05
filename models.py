from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey, text
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated
from enum import Enum
from datetime import datetime


#decrarative style
from database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]

class Action(Enum):
    enter = "enter"
    quit = "quit"


class LogTable(Base):
    __tablename__ = "log"
    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    action: Mapped[Action]
    at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))


class Role(Enum):
    boss = "chief"
    deputy_chief = "deputy_chief"
    worker = "worker"
    user = "user"
    fired = "fired"


class UsersTable(Base):
    __tablename__ = "users"
    id: Mapped[intpk]
    surname: Mapped[str]
    role: Mapped[Role]


#imperative style
from database import meta_data


log_table = Table(
    "log",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id"), nullable=False,),
    Column("action", String, nullable=False),
    Column("at", DateTime(timezone=True), server_default=func.now())
)

users_table = Table(
    "users",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("surname", String),
    Column("role", String, nullable=False)
)