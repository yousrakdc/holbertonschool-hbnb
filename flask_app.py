#!/usr/bin/python3
from flask import current_app as app
import os

@app.route('/api')
def index():
    cwd = os.getcwd()
    current_file_path = __file__
    root_path = app.root_path
    
    return f'''
        Hello, Flask!<br>
        Current working directory: {cwd}<br>
        Current file path: {current_file_path}<br>
        Application root path: {root_path}
    '''
