from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    """Describing some data, that we expect to get in a body af a request"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    """Using described model as we want"""

    '''Use this as a request's body:
    {
    "name": "Some name",
    "description": "Some description",
    "price": 100.0,
    "tax": 10.15
    }
    '''
    overall_price = item.price + item.tax

    return {'Your overall price': overall_price}


if __name__ == '__main__':
    import uvicorn

    # Run the FastAPI app at the root level
    uvicorn.run(app, host="127.0.0.1", port=8000)
