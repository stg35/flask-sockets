from flask import Flask
from flask import render_template, request
from flask_socketio import SocketIO, emit
import constants
import hashlib
from db import insertUser

app = Flask(__name__)
app.config["SECRET_KEY"] = "key"

socketio = SocketIO(app, cors_allowed_origins="*")

ip = constants.server_ip

users = []

@app.route('/')
def index():
    return render_template('login_page.html')

@app.route('/adm')
def adm():
    # username = 'qqqqq'
    # password = '11123456243'
    # hashed_password = hashlib.sha224(password.encode('utf-8')).hexdigest()
    # print(hashed_password)
    #
    # insertUser(username, hashed_password)

    # collection = db['users']
    # collection.insert_one({'username': username, 'password': hashed_password})

    return render_template('admin.html')

# @app.route('/check')
# def check():




@app.route('/chat')
def chat():
    username = request.args.get('username')
    #password = request.args.get('pass')
    return render_template('index.html', username=username)

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