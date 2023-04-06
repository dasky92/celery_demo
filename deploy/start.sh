# redis-server start
docker run -itd -p 6379:6379 --name=celery_demo redis

# celery worker
celery -A tasks worker --loglevel=INFO