from datetime import datetime
from flask import Flask
from flask import request

from validation import is_valid

app = Flask(__name__)

messages = []
users = {'fish': '123'}



@app.route('/ping', methods = ['GET'])
def ping():
    """
    проверка что сервер живой
    :input {}
    :output {"alive": bool, "time": float}
    """
    return {
        'time': datetime.now().timestamp(),
        'alive': True
    }


@app.route('/register', methods = ['POST'])
def register():
    """
    регистрация нового пользователя
    :input {"username": str, "password": str}
    :output {"success": bool}
    """
    user = request.json['username']
    password = request.json['password']

    if users.get(user):
        return {'success': False, 'reason': 'user already exist'}
    if not is_valid(user, password):
        return {'success': False, 'reason': 'invalid username or password'}
    users[user] = password
    return {'success': True}


@app.route('/send', methods = ['POST'])
def send():
    """
    отправка сообщения на сервер
    :input {"username": str, "password": str, "text": str}
    :output {"success": bool} 
    """
    user = request.json['username']
    password = request.json['password']
    text = request.json['text']
    time = datetime.now().timestamp()
    if password == users.get(user):
        messages.append({'user': user, 'time': time, 'text': text})
        return {'success': True}
    return {'success': False, 'reason': 'unknown or unauthorized user'}


@app.route('/load', methods = ['GET'])
def load():
    """
    загрузка сообщений с сервера, начиная с времени time
    если time отсутствует - загрузятся все
    :input {"after": float}
    :output {"messages": []}
    """
    t = float(request.json.get('after') or -1)
    if t > 0:
        filtered = []
        for i in messages:
            if i['time'] > t:
                filtered.append(i)
        return {'messages': filtered}
    return {'messages': messages}


if __name__ == "__main__":
    app.run()
