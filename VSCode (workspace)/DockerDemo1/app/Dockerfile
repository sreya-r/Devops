FROM python:3.9-slim
WORKDIR /app
copy . /app
run pip install flask

env flask_app=app.python
env flask_run_host=0.0.0.0
env flask_run_port=5000

expose 5000

cmd ["flask", "run"]