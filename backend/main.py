from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base

def create_tables():
    Base.metadata.create_all(bind = engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE,version=settings.PROJECT_VERSION)
    create_tables()
    return app

app   = start_application()

@app.get('/')
def hello():
    return "Hello  friends!"


def start_application(): # This starts the application.
    app = FastAPI()
    return app

app = start_application() # This instantiates the application

