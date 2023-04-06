# self module with dependence: same name ?
from celery import Celery
from celeryconfig import CeleryConfig

app = Celery('demo')
app.config_from_object(CeleryConfig)


if __name__ == "__main__":
    app.start()
