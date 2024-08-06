from sqlalchemy import select
from tabulate import tabulate

from database import sync_engine, sync_session_factory, Base
from models import LogTable, Role, UsersTable


class SystemORMSync:

    @staticmethod
    def create_tables():
        sync_engine.echo = False
        Base.metadata.drop_all(sync_engine)
        Base.metadata.create_all(sync_engine)
        sync_engine.echo = True

    @staticmethod
    def insert_logs(logs: list[LogTable]):
        with sync_session_factory() as session:
            session.add_all(logs)
            session.commit()
    
    @staticmethod
    def show_logs():
        with sync_session_factory() as session:
            query = select(LogTable.id, 
                        LogTable.user_id, 
                        UsersTable.surname, 
                        UsersTable.role, 
                        LogTable.action, 
                        LogTable.at).join(UsersTable, UsersTable.id == LogTable.user_id)
            res = session.execute(query).all()
            print(tabulate(res, headers=("id", "user_id", "surname", "role", "action", "at"), tablefmt="double_grid"))
    
    @staticmethod
    def add_user(surname: str, role: Role):
        with sync_session_factory() as session:
            session.add(UsersTable(surname=surname, role=role))
            session.commit()

    @staticmethod
    def show_users():
        with sync_session_factory() as session:
            query = select(UsersTable)
            res = session.execute(query).scalars().all()
            print(res)
            res = [repr(user).split("|") for user in res]
            print(tabulate(res, headers=("id", "surname", "role"), tablefmt="double_grid"))
    
    @staticmethod
    def update_worker_data(user_id: int, new_surname: str = None, new_role: str = None):
        with sync_session_factory() as session:
            user = session.get(UsersTable, user_id)
            if new_surname:
                user.surname = new_surname
            if new_role:
                user.role = new_role
            session.commit()