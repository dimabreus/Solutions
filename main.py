from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, a: Union[str, None] = None, b: Union[str, None] = None):
    return {"item_id": item_id, "a": a, "b": b}


