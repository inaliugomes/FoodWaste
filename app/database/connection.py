from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

#Local where the database will be created
DATABASE_URL = "sqlite:///./foodwaste.db"

#Function that will handle de connection , to operate in database
engine = create_engine(DATABASE_URL,
                       connect_args=
                       {"check_same_thread":False})

#The section that will be open everytime we need to do a operation
# every operation have is on temporary session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine)

#function that allows as to operate that close the session ,
#this hay the  sure that there is not session open .
def get_db():
    with SessionLocal() as session:
        yield session
