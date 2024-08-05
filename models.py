from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func

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