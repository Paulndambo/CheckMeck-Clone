FROM python:3.8-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY ./CheckMechBackend/requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./CheckMechBackend/ /code/

#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "CheckMechBackend.wsgi"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
