host=$(python3 -c "import sys, json; print(json.load('config.json')['wsHost'])")
port=$(python3 -c "import sys, json; print(json.load('config.json')['wsPort'])")

gunicorn -w 4 -b $(host):$(port) file_server:app