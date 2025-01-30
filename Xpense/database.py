from sqlalchemy import create_engine
from sqlalchemy.orm import Session


POSTGRES_DATABASE_URL  = "postgresql+psycopg2://postgres:Opeyemi123@localhost/Xpensedb"

engine = create_engine(POSTGRES_DATABASE_URL)

session = Session(engine)