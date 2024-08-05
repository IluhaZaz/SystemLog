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
    def add_user(surname: str, role: Role):
        with sync_session_factory() as session:
            session.add(UsersTable(surname=surname, role=role))
            session.commit()