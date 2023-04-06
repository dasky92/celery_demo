from tasks import add
from celery.result import AsyncResult


task = add.apply_async(args=[2, 2], expires=55)
print(task.task_id)
print(task.get())
print(AsyncResult(task.task_id).result)