# https://fastapi.tiangolo.com/tutorial/first-steps/

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Broadsword calling DannyBoy, over!"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int=0, limit: int=10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}