from flask import Flask, send_file, request
app = Flask(__name__)

import uuid
from pathlib import Path   
import os

@app.route('/', methods=['POST'])
def upload_file():
    path = f'./temp/{str(uuid.uuid4())}.epub'
    f = request.files['file']
    f.save(path)
    return path

@app.route('/<filename>', methods=['GET'])
def get_file():
    filename = Path("./temp/{filename}").name
    file = Path(f'./temp/{filename}')
    if (file.is_file()):
        return send_file(f'./temp/{filename}', attachment_filename='file.epub')
    else:
        return 'File does not exist.'