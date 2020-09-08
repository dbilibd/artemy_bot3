from random import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
import time
import string
import nltk
import json
s = -12
s1 = -1
code = '140401'
main_token = 'd67f83db79197faed7c707a243fa66e7e8b02c7d3de626ff29b83eb816396983cac11adb5b7d6b576a1d6'
vk_session = vk_api.VkApi(token = main_token)
longpoll = VkBotLongPoll(vk_session, '198179927')
vk = vk_session.get_api()
response_1 = 'f'
def sms(id, msg):
	vk.messages.send(peer_id = id, message = msg, random_id = 0)

def replic(category, replicas):
    filename = 'replicas.txt'
    myfile = open(filename, mode='r',encoding='UTF-8')
    json_data = json.load(myfile)
    for i in json_data:
        print(i)
        if category in i:
            i[category].append(replicas)
    myfile = open(filename, mode='w',encoding='UTF-8')
    json.dump(json_data, myfile)
    myfile.close()

def replic_res(category, replicas):
    filename = 'response.txt'
    myfile = open(filename, mode='r',encoding='UTF-8')
    json_data = json.load(myfile)
    for i in json_data:
        print(i)
        if category in i:
            i[category].append(replicas)
    myfile = open(filename, mode='w',encoding='UTF-8')
    json.dump(json_data, myfile)
    myfile.close()

def mess():
    filename = 'replicas.txt'
    myfile = open(filename, mode='r', encoding='UTF-8')
    json_data = json.load(myfile)
    mes1 = []
    for i in json_data:
        mes = i.keys()
        mes1.extend(iter(mes))
    return(mes1)

def mess_view(s, response):
    while s > 10:
        s = s - 11
    print('while s = ' + str(s))
    filename = 'replicas.txt'
    myfile = open(filename, mode='r', encoding='UTF-8')
    json_data = json.load(myfile)
    print(json_data[s][response])
    return(json_data[s][response])

def mess_view_response(s, response):
    while s > 10:
        s = s - 11
    print('while s = ' + str(s))
    filename = 'response.txt'
    myfile = open(filename, mode='r', encoding='UTF-8')
    json_data = json.load(myfile)
    print(json_data[s][response])
    return(json_data[s][response])

for event in longpoll.listen():
    if (event.type == VkBotEventType.MESSAGE_NEW):
        response = event.object['text']
        response = response.lower()
        id = event.obj['peer_id']
        while True:
            try:
                if response == code:
                    sms(id, 'Change category:\n')
                    mes = "\n".join(str(x) for x in sorted(mess()))
                    sms(id, mes)
                    response_1 = response
                for i in mess():
                    s += 1
                    print(i)
                    print('s = ' + str(s))
                    if i in mess():
                        if i == response and response_1 == code:
                            print(s)
                            msg = "\n".join(str(x) for x in sorted(mess_view(s, response)))
                            msg_resp = "\n".join(str(x) for x in sorted(mess_view_response(s, response)))
                            sms(id, 'Сообщения:')
                            sms(id, msg)
                            sms(id, 'Ответы:')
                            sms(id, msg_resp)
                            sms(id, 'Введите:\n "фраза" - для добавления фразы\n"ответ" - для добавления ответа\n "back" - для выхода к выбору категории')
                            response_1 = response
                            s = -1
                            break
                    else:
                        s = s - 1
                        s = s + 1
                    if response == 'фраза' and  response_1 in mess():
                        print(response)
                        print(response_1)
                        sms(id, 'Введите фразу:')
                        response_2 = response_1 # yes
                        response_1 = response # фраза
                    elif response != 'back' and response != 'фраза' and response_1 == 'фраза':
                        replic(response_2, response)
                        sms(id, 'Фраза добавлена')
                        response_1 = 'f'
                        break
                    elif response == 'ответ' and  response_1 in mess():
                        print(response)
                        print(response_1)
                        sms(id, 'Введите ответ:')
                        response_2 = response_1
                        response_1 = response
                    elif response != 'back' and response != 'ответ' and response_1 == 'ответ':
                        replic(response_2, response)
                        sms(id, 'Ответ добавлен')
                        response_1 = 'f'
                        break
                    elif response == 'back':
                        response_1 = code
                        s = s - 1
                        break

                filename = 'replicas.txt'
                myfile = open(filename, mode='r', encoding='UTF-8')
                json_data = json.load(myfile)
                for i in json_data:
                    try:
                        s1 += 1
                        for i1 in i:
                            for i2 in (mess_view(s1, i1)):
                                if i2 == response:
                                    msg = mess_view_response(s1, i1)
                                    sms(id, random.choice(msg))
                                    break
                    except:
                        break
                break
            except:
                continue






