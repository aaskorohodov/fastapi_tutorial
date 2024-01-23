from fastapi import FastAPI


app = FastAPI()

my_db = {
    'table_1': {
        1: 'value_1',
        2: 'value_2',
        3: 'value_3',
        4: 'value_4',
        5: 'value_5',
    },
    'table_2': {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
    }

}


@app.get("/items/")
async def read_item(table: str = 'table_1', value: int = 1):
    """Use this: 'http://127.0.0.1:8000/items/?table=table_1&value=2'
    """

    return my_db.get(table, {}).get(value, 'Nothing found')


@app.get("/optional/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    """
    http://127.0.0.1:8000/optional/some_item?q=123 -> {"item_id": "some_item", "q": 123}
    http://127.0.0.1:8000/optional/some_item?not_q=123 -> {"item_id": "some_item"}
    http://127.0.0.1:8000/optional/some_item -> {"item_id": "some_item"}
    """

    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


if __name__ == '__main__':
    import uvicorn

    # Run the FastAPI app at the root level
    uvicorn.run(app, host="127.0.0.1", port=8000)
