FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./ ./

EXPOSE 3000 3001
CMD ["sh", "./docker.run.sh"]
