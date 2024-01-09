FROM python:3.9

# 
WORKDIR /fastapi_app

# 
COPY ./requirements.txt .

# 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# 
COPY . .

RUN chmod a+x docker/*.sh

# 
#  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

