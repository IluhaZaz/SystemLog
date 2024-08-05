from sqlalchemy import create_engine, MetaData

from config import settings


meta_data = MetaData()

sync_engine = create_engine(
    url=settings.DATABASE_URL_syncpg(),
    echo=True
)