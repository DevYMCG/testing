from fastapi import FastAPI
from config import setting

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