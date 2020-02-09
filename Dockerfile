FROM python:3.7-alpine
COPY requirements.txt /
RUN pip install -r /requirements.txt
# EXPOSE 5000
COPY . /runtime
WORKDIR /runtime
CMD ["gunicorn", "-w 1", "--bind=0.0.0.0:5000", "--reload", "wsgi:application"]