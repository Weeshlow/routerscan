#!/usr/bin/python
import requests
import sys
def send_message(tocken,chat,text):
    url = "https://api.telegram.org/{}/".format(tocken)
    params = {'cat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

if __name__ == '__main__':
       send_message(sys.argv[1],sys.argv[2],sys.argv[3])
        
