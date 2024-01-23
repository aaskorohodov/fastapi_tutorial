from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Describing 2 things, that we expect to get from the body
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


'''Now, FastAPI is expecting to have a json, that should look like so:

{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}

It will parse each key here, and map them with Item and User, making data-validation automatically
'''


@app.put("/items/{item_id}")
async def update_item(
        item_id: int,
        item: Item,
        user: User):

    results = {"item_id": item_id, "item": item, "user": user}
    return results


if __name__ == '__main__':
    import uvicorn

    # Run the FastAPI app at the root level
    uvicorn.run(app, host="127.0.0.1", port=8000)
