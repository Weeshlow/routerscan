#!/usr/bin/python
import requests


url = ""
def send_message(chat,text):
    params = {'cat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
