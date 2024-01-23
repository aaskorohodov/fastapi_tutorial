from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    overall_price = item.price + item.tax

    return {'Your overall price': overall_price}


if __name__ == '__main__':
    import uvicorn

    # Run the FastAPI app at the root level
    uvicorn.run(app, host="127.0.0.1", port=8000)
