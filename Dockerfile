FROM python:3.8
ADD ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
ADD ./manage.py .
ADD ./gnujdb gnujdb
ADD ./entrypoint.sh .
CMD ./entrypoint.sh
