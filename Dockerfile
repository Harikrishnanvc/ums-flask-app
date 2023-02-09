FROM python:3.10-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /user-management-system

RUN apk add gcc python3-dev postgresql-dev

COPY . /user-management-system
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["./ums_db.sh"]

