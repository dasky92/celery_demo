from app import app
import time


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)


@app.task
def long_task(seconds=None):
    print(f'long_task start')
    if seconds:
        print(f'sleep {seconds}')
        time.sleep(seconds)

    print(f'long_task finish')
    return
