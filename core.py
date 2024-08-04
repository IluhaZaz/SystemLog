from sqlalchemy import select, delete, update, insert

from database import sync_engine, meta_data
from models import log_table


def create_tables():
    meta_data.drop_all(sync_engine)
    meta_data.create_all(sync_engine)

def insert_logs(logs: list[dict]):
    with sync_engine.connect() as conn:
        stmt = insert(table=log_table).values(logs)
        conn.execute(stmt)
        conn.commit()