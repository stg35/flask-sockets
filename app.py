from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import constants
import hashlib
from db import insertUser, addMessage, findPassword, findUser, lastMessages
from datetime import datetime

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "key"

socketio = SocketIO(app, cors_allowed_origins="*")

ip = constants.server_ip

users = []

counter = []

@app.route('/')
def index():
        registered = False
        errorpass = False
        erroruser = False
        if request.args.get('registered'): registered = True
        if request.args.get('erroruser'): erroruser = True
        if request.args.get('errorpass'): errorpass = True
        return render_template('login_page.html', registered=registered, erroruser=erroruser, errorpass=errorpass)

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

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
        if findUser(username):
            if findPassword(username, hashed_password):
                return render_template('index.html', username=username, messages=lastMessages())
            else:
                return redirect('/?errorpass=True')
        else:
            return redirect('/?erroruser=True')
    return redirect('/')

@socketio.on('message')
def handler_message(msg):

    date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    emit('message_sent', {'message': msg['message'], 'user': msg['user'], 'timestamp': date_time}, broadcast=True)
    addMessage(msg['message'], msg['user'], date_time, len(counter))

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