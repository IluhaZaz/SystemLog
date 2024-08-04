from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from database import meta_data

log_table = Table(
    "log",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("surname", String),
    Column("at", DateTime(timezone=True), server_default=func.now())
)