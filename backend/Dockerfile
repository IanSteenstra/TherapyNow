FROM python:3.7.7
ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY "4bih3]<ae<'J_quAQyT2q^2-4'csa="
ENV ALLOWED_HOSTS 127.0.0.1, localhost, api
ENV EMAIL_HOST_PASSWORD "lkdafn83nr2N98h3"

RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/
EXPOSE 8000
RUN pip install -r requirements.txt
COPY . /backend/
RUN python manage.py migrate