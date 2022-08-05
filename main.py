from fastapi import FastAPI
from config import setting
from database import engine
from models import Base
from router import items, users

Base.metadata.create_all(bind=engine)

tags = [
    {
        "name": "user",
        "description": "This is user route"
    },
    {
        "name": "items",
        "description": "This is items route"
    }
]

app = FastAPI(
              title=setting.TITLE,
              description=setting.DESCRIPTION,
              version=setting.VERSION,
              contact={
                "name": setting.NAME,
                "email": setting.EMAIL
              },
              openapi_tags=tags)

app.include_router(users.router)
app.include_router(items.router)
