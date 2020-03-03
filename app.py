from flask import Flask
from flask import render_template, request
from flask_socketio import SocketIO, emit
import constants

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"

socketio = SocketIO(app, cors_allowed_origins="*")

ip = constants.server_ip

users = []

@app.route('/')
def index():
    return render_template('login_page.html')

@app.route('/chat')
def chat():
    username = request.args.get('username')
    password = request.args.get('pass')
    return render_template('index.html', username=username, password=password)

@socketio.on('message')
def handler_message(msg):
    print('User: ' + msg['user'] + ' Message: ' + msg['message'])
    emit('message_sent', {'message': msg['message'], 'user': msg['user']}, broadcast=True)

@socketio.on('connect')
def handler_connection():
    users.append(1)
    print('Users: ', len(users))

@socketio.on('disconnect')
def handler_disconnection():
    del users[-1]
    print('Users: ', len(users))

if __name__ == '__main__':
	socketio.run(app, host=ip, debug=True)