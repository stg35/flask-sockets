from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import constants
import hashlib
from db import insertUser, findUP, addMessage
import requests

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "key"

socketio = SocketIO(app, cors_allowed_origins="*")

ip = constants.server_ip

users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        if findUP(username, hashed_password):
            return redirect(url_for('chat', username=username))
        else:
            return render_template('login_page.html', error=True)
    else:
        registered = False
        error = False
        if request.args.get('registered'): registered = True
        if request.args.get('error'): error = True
        return render_template('login_page.html', registered=registered, error=error)

@app.route('/adm', methods=['GET', 'POST'])
def adm():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        print(hashed_password)
        insertUser(username, hashed_password)
        return redirect('/?registered=True')
    else:
        return render_template('admin.html')

@app.route('/chat')
def chat():
    username = request.args.get('username')
    return render_template('index.html', username=username)

@socketio.on('message')
def handler_message(msg):
    print('User: ' + msg['user'] + ' Message: ' + msg['message'])
    emit('message_sent', {'message': msg['message'], 'user': msg['user']}, broadcast=True)
    addMessage(msg['message'], msg['user'])

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