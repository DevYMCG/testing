from fastapi import FastAPI
from config import setting
from database import engine
from models import Base


Base.metadata.create_all(bind=engine)

tags = [
    {
        "name": "user",
        "description": "This is user route"
    },
    {
        "name": "product",
        "description": "This is product route"
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

@app.get("/user", tags=["user"])
def index():
    return  {"Message": "hello word"}


@app.get("/product", tags=["product"])
def get_product():
    return  {"Message": "hello Product"}

@app.get('/getenvvar', tags=["config"])
def get_envvars():
    return {"database": setting.POSTGRES_URL}

@app.post('/create_user')
def create_user(n: int, ch: str ):
    return "abc"