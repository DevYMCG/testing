from fastapi import FastAPI
from config import setting
from database import engine
from models import Base
from router import items, users, login
from webapps.routers import items as web_items
from webapps.routers import users as web_users
from webapps.routers import auth as web_auth
from fastapi.staticfiles import StaticFiles

# we are alembic migrations
# Base.metadata.create_all(bind=engine)

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

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(users.router)
app.include_router(items.router)
app.include_router(login.router)
app.include_router(web_items.router)
app.include_router(web_users.router)
app.include_router(web_auth.router)
