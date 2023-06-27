from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL='postgresql://igor_render:5lGQuN1kIVPqR4x6GD7a7Z7EpW9ja2GQ@dpg-ci8rn3h8g3nfuca2vvc0-a.frankfurt-postgres.render.com/shop_wapi_render'

# equivalent à un "connect"
database_engine = create_engine(DATABASE_URL)
# equivalent à un "cursor"
SessionTemplate = sessionmaker(bind=database_engine, autocommit=False, autoflush=False)

def get_cusor():
    db= SessionTemplate()
    try:
        yield db
    finally:
        db.close()