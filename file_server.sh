host=`python3 -c "import sys, json; print(json.loads(open('config.json').read())['apiHost'])"`
port=`python3 -c "import sys, json; print(json.loads(open('config.json').read())['apiPort'])"`

gunicorn -w 4 -b "$host:$port" file_server:app
