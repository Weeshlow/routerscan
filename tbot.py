#!/usr/bin/python
import requests
text = 
tocken = 
chatid = 
url = "https://api.telegram.org/{}/sendmessage?chat_id={}&text={}".format(tocken,chatid,text)
def send_message(chat,text):
    params = {'cat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
