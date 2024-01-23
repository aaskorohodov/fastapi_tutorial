import asyncio
import time

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    """Async endpoints provide a way to use await inside.

    It can be used in cases, where we need to execute some asynchronous tasks inside an endpoint"""

    start_time = time.perf_counter()

    task1 = asyncio.create_task(operation_1())
    task2 = asyncio.create_task(operation_2())

    r1 = await task1
    r2 = await task2

    end_time = time.perf_counter()
    time_took = end_time - start_time

    result = {
        'Time took': time_took,
        'Result of operation_1': r1,
        'Result of operation_2': r2
    }
    return result


async def operation_1():
    await asyncio.sleep(1)
    return 'Result from operation 1'


async def operation_2():
    await asyncio.sleep(1)
    return 'Result from operation 2'


if __name__ == '__main__':
    import uvicorn

    # Run the FastAPI app at the root level
    uvicorn.run(app, host="127.0.0.1", port=8000)
