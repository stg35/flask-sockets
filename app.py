from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"

socketio = SocketIO(app, cors_allowed_origins="*")
socketio.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handler_message(msg):
    print('User: ' + msg['user'] + ' Message: ' + msg['message'])
    emit('message_sent', {'message': msg['message'], 'user': msg['user']}, broadcast=True)

if __name__ == '__main__': 
    socketio.run(app, host='0.0.0.0')
