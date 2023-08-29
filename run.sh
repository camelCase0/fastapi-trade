
#!/bin/bash
# celery -A src.tasks.tasks:celery worker --loglevel=INFO --pool=solo
# celery -A src.tasks.tasks:celery flower --loglevel=INFO --pool=solo
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

