from kombu import Queue


class CeleryConfig(object):

    # task_always_eager = True
    # broker
    broker_url = 'redis://localhost:6379/0'

    # backend
    # result_backend = 'db+sqlite:///data/sqlite3.db'
    result_backend = 'redis://localhost:6379/1'

    # formatter
    task_serializer = 'json'
    result_serializer = 'json'
    accept_content = ['json']

    # time
    timezone = 'Asia/Shanghai'

    # utc
    enable_utc = True

    # timeout, unit: second
    # FIXME: 60 for test
    result_expires = 3600

    # tasks
    imports = (
        "tasks",
    )

    # queue
    task_default_queue = "default"
    task_queues = (
        Queue(name="default", routing_key="*"),
    )
    # router
    task_routes = {
        # 'tasks.add': 'low-priority',
    }
