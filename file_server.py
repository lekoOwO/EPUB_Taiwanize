from flask import Flask, send_from_directory, request
from epubconv.epubconv import config
settings = config.load()
app = Flask(__name__, static_folder='static')
app.config['MAX_CONTENT_LENGTH'] = settings['maxFileSize'] * 1024 * 1024

import uuid
from pathlib import Path   
import os
from threading import Timer

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file_id = str(uuid.uuid4())
        path = f'./temp/{file_id}.epub'
        f = request.files['file']
        f.save(path)
        Timer(settings['tempTime'], lambda x: os.remove(x) if os.path.isfile(x) else None, [path]).start()
        return file_id
    if request.method == 'GET':
        return app.send_static_file('index.html')

@app.route('/<file_id>', methods=['GET'])
def get_file(file_id):
    return send_from_directory('./temp',f'{file_id}.epub')