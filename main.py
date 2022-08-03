from fastapi import FastAPI


description= """
## This is my Application created in FastAPI

It has only one route "index"

"""

tags = [
    {
        "name": "user",
        "description": "These are my user, routes"
    },
    {
        "name": "product",
        "description": "There are product routes"
    }
]

app = FastAPI(title="My Application",
              description=description,
              version="0.0.1",
              contact={
                "name": "Yohana Contreras",
                "email": "yohana.contrerasg@gmail.com"
              },
              openapi_tags=tags,
              openapi_url="/api/v1/openapi.json")

@app.get("/user", tags=["user"])
def index():
    return  {"Message": "hello word"}


@app.get("/product", tags=["product"])
def get_product():
    return  {"Message": "hello Product"}