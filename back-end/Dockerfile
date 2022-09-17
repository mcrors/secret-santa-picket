FROM python:3.9-alpine


RUN python -m pip install --upgrade pip \
    && adduser -D santa
USER santa

WORKDIR /secret-santa

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app .

CMD python main.py
