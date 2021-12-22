from flask import Flask
from flask import render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY']= 'secret'
sio = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')


@sio.on('message')
def server_pesan(psn):
	print('PESAN : ' + psn)
	send(psn, broadcast=True)

if __name__ == '__main__':
    sio.run(app)

