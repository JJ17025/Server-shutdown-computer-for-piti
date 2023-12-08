import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'นี้คือ main<br>ไปที่ http://127.0.0.1:5000/shutdown'


@app.route('/shutdown')
def shutdown():
    os.system("shutdown /s /t 1")
    return 'shutdown ok'


if __name__ == '__main__':
    app.run()
#123
