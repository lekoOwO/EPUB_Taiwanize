FROM python:alpine

COPY . /usr/src/app/
WORKDIR /usr/src/app

EXPOSE 3000 3001

RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["nohup", "python", "./api.py"]
CMD ["sh", "./file_server.sh"]
