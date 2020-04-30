from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/list")
def read_list():
    return [
        {
            "id": 1,
            "name": "item one"
        },
        {
            "id": 2,
            "name": "item two"
        },
        {
            "id": "3",
            "name": "item three"
        },
        {
            "id": 4,
            "name": "item four"
        }
    ]