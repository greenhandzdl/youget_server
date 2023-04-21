from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('submit')
def handle_submit(url):
    command = ['you-get', url]
    output = subprocess.check_output(command)
    socketio.emit('result', output.decode('utf-8'))

if __name__ == '__main__':
    socketio.run(app)