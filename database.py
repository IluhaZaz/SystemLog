from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from config import settings


meta_data = MetaData()

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg(),
    echo=True
)

class Base(DeclarativeBase):
    pass

sync_session_factory = sessionmaker(sync_engine)