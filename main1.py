from random import random
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
import random
import time
import string
import nltk
import json
code = '140401'
main_token = 'd67f83db79197faed7c707a243fa66e7e8b02c7d3de626ff29b83eb816396983cac11adb5b7d6b576a1d6'
vk_session = vk_api.VkApi(token = main_token)
longpoll = VkBotLongPoll(vk_session, '198179927')
vk = vk_session.get_api()
response_1 = 'f'
def sms(id, msg):
	vk.messages.send(peer_id = id, message = msg, random_id = 0)

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
def send_msg(response):
    filename = 'replicas.txt'
    myfile = open(filename, mode='r', encoding='UTF-8')
    json_data = json.load(myfile)
    s1 = -1
    for i in json_data:
        s1 += 1
        for i1 in i:
            for i2 in (mess_view(s1, i1)):
                if i2 in response:
                    msg = mess_view_response(s1, i1)
                    break
                else:
                    continue
    return(msg)

for event in longpoll.listen():
    if (event.type == VkBotEventType.MESSAGE_NEW):
        response = event.object['text']
        response = response.lower()
        sentences = nltk.sent_tokenize(response)
        for sentence in sentences:
            response = nltk.word_tokenize(sentence)
        id = event.obj['peer_id']
        while True:
            try:
                sms(id, random.choice(send_msg(response)))
                break
            except:
                break