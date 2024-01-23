from fastapi import FastAPI


app = FastAPI()


@app.get("/items_standard/{item_id}")
async def read_item(item_id):
    """Standard way of catching some parameters"""

    return {"item_id": item_id}


@app.get("/items_specific_int/{item_id}")
async def read_item(item_id: int):
    """In case item_id is not int - 422 status will be returned in response"""

    return {"item_id": item_id}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """This will allow to send paths.

    For example, we can go to 'http://127.0.0.1:8000/files/some/path.txt' and get 'some/path.txt'
    In case we need to have a leading slash:'http://127.0.0.1:8000/files//some/path.txt' -> '/some/path.txt'
    """

    return {"file_path": file_path}


if __name__ == '__main__':
    import uvicorn

    # Run the FastAPI app at the root level
    uvicorn.run(app, host="127.0.0.1", port=8000)
