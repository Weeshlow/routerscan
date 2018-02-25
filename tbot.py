#!/usr/bin/python
import requests
import sys
def send_message(tocken,chat,text):
    url = "https://api.telegram.org/{}/".format(tocken)
    params = {'cat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response
def main():
    for arg in sys.argv:
        print(arg)



if __name__ == '__main__':
    main()
