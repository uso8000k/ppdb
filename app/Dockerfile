FROM python:3.7
MAINTAINER https://github.com/uso8000k

WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python","app/app.py"]
