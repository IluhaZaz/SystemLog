from sqlalchemy import select, update, insert, join

from database import sync_engine, meta_data
from models import log_table, users_table


def create_tables():
    sync_engine.echo = False
    meta_data.drop_all(sync_engine)
    meta_data.create_all(sync_engine)
    sync_engine.echo = True

def insert_logs(logs: list[dict]):
    with sync_engine.connect() as conn:
        stmt = insert(table=log_table).values(logs)
        conn.execute(stmt)
        conn.commit()

def show_logs():
    with sync_engine.connect() as conn:
        query = select(log_table.c.id, 
                       log_table.c.user_id, 
                       users_table.c.surname, 
                       users_table.c.role, 
                       log_table.c.action, 
                       log_table.c.at
                       ).select_from(
                            join(users_table, log_table, 
                            users_table.c.id == log_table.c.user_id)
                                    )
        res = conn.execute(query).all()
        for log in res:
            print(*log)

def add_user(surname: str, role: str):
    with sync_engine.connect() as conn:
        stmt = insert(users_table).values([{"surname": surname, "role": role}])
        conn.execute(stmt)
        conn.commit()

def show_users():
    with sync_engine.connect() as conn:
        query = select(users_table)
        res = conn.execute(query)
        for user in res:
            print(*user)

def update_worker_surname(user_id: int, new_surname: str):
    with sync_engine.connect() as conn:
        stmt = update(users_table).values(surname=new_surname).filter_by(id=user_id)
        conn.execute(stmt)
        conn.commit()