from app import app
from app.settings import *
from app import message_hendler
from flask import Flask, request, json
import vk

# @app.route('/')
# @app.route('/index')
# def index():
#     return ('hello from flask!')

    
@app.route('/group-app')
def group_app():
    return '2+2=5 =/'
    
    
@app.route('/', methods=['POST'])
def processing():
    #Распаковываем json из пришедшего POST-запроса
    data = json.loads(request.data)
    #Вконтакте в своих запросах всегда отправляет поле типа
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        session = vk.Session()
        api = vk.API(session, v=5.0)
        user_id = data['object']['user_id']
        mess = message_hendler.parse_command(data['object']['body'])
        api.messages.send(access_token=token, user_id=str(user_id), message=mess)
        # Сообщение о том, что обработка прошла успешно
        return 'ok'
        
        
