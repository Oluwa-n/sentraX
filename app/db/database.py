   # Creates SQLite engine.
  # Defines Base = declarative_base()
# Creates DB session factory.
  # No models here.
  
  
  #creating the database engine and calling its file 
  
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#sqlite database url 
DATABASE_URL = "sqlite:///./sentrax.db"

#create the engine 

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} 
)


#working on the session 

SessionLocal =  sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)
  
  
#creating the base for the model 

Base = declarative_base()

