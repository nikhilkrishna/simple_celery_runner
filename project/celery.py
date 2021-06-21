from celery import Celery

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'


app = Celery('tasks', broker=BROKER_URL, backend=BACKEND_URL, include=['project.tasks'])
app.conf.update(
    result_expires=3600,
)
app.conf.task_create_missing_queues = True


if __name__ == '__main__':
    app.start()
    app.autodiscover_tasks(force=True)