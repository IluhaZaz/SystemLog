from sqlalchemy import select, update, insert

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

def show_logs():
    with sync_engine.connect() as conn:
        query = select(log_table)
        res = conn.execute(query).all()
        for log in res:
            print(*log)

def update_worker_name_in_logs(user_id: int, new_surname: str):
    with sync_engine.connect() as conn:
        stmt = update(log_table).values(surname=new_surname).filter_by(user_id=user_id)
        conn.execute(stmt)
        conn.commit()
