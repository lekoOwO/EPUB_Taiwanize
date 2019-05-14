host=`python3 -c "import sys, json; print(json.loads(open('config.json').read())['wsHost'])"`
port=`python3 -c "import sys, json; print(json.loads(open('config.json').read())['wsPort'])"`

gunicorn -w 4 -b "$host:$port" file_server:app