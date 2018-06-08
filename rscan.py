#!/usr/bin/python3
import socket
import subprocess
import os
import sys
import random
import time as t
import re
#####################
#       змінні      #
#####################
_version_ = "2.0 release"
portsfile = "ports.txt"
hostsfile = "hosts.txt"
goodip = []
diapazons = []
ports = []
bottocken = 'bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11' # no '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
chatid = '12345679'
#####################
#     функції       #
#####################
def clearx():
	if sys.platform == 'linux':
		a = os.system('clear')
		del a
	elif sys.platform == 'win32':
		a = os.system('cls')
		del a
	else:
		print('\n'*100)
def dload():
	global diapazons
	f = open(hostsfile, 'r')
	for line in f:
		l = line.strip()
		if l != '' and l != '\n':
			diapazons.append(str(l))
			diapazons = list(set(diapazons))
	f.close()
	

def pload():
	global ports
	f = open(portsfile, 'r')
	for line in f:
		l = line.strip()
		if l != '' and l != '\n':
			ports.append(str(l))
			ports = list(set(ports))
	f.close()

def start_program():
	title_bar("title")
	t.sleep(0.7)
	title_bar("menu")

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def title_bar(title):
	clearx()
	if title == "title":          
		print("\t            #####                                                        ")
		print("\t           #     #  ####  #####  #    #  ####   ####  #####   ##   #   # ")
		print("\t           #       #    # #    # ##   # #    # #        #    #  #   # #  ")
		print("\t           #  #### #    # #    # # #  # #    #  ####    #   #    #   #   ")
		print("\t           #     # #    # #####  #  # # #    #      #   #   ######   #   ")
		print("\t           #     # #    # #   #  #   ## #    # #    #   #   #    #   #   ")
		print("\t            #####   ####  #    # #    #  ####   ####    #   #    #   #   ")
	elif title == "menu":
		print('\033[92m'+"\t             MENU  routerscan " + _version_+'\033[0m')
	elif title == "menu1":
		print('\033[92m'+"\t             ДІАПАЗОНИ routerscan " + _version_+'\033[0m')
	elif title == "menu2":
		print('\033[92m'+"\t             ПОРТИ routerscan " + _version_+'\033[0m')
	elif title == "result":
		print('\033[92m'+"\t             РЕЗУЛЬТАТИ routerscan "+_version_+'\033[0m')
def menu():
	title_bar("menu")
	print("\n [1] довідка")
	print("\n [2] діапазони")
	print("\n [3] порти")
	print("\n [4] _почати_ ")
	print("\n [0] \u001b[4m\u001b[31mвихід\u001b[0m \n")
	a = input("rtscan ~$ ")
	if a == "1":
		clearx()
		with open('README.md','r') as f:
			print(f.read())
		t.sleep(10)
		clearx()
		menu()
	elif a == "2":
		clearx()
		menu1()
	elif a == "3":
		clearx()
		title_bar("menu2")
		menu2()
	elif a == "4":
		start()
	elif a == "e" or a == "exit" or a == "0":
		print("До побачення")
		t.sleep(0.5)
		clearx()
		exit()
	else:
		print('\033[91m'+'\033[1m'+"НЕПРАВЕЛЬНА КОМАНДА"+'\033[0m')
		t.sleep(3)
		clearx()
		menu()

def menu1():
	title_bar("menu1")
	
	print("\n [1] додати діапазон")
	print("\n [2] видалити діапазони")
	print("\n [3] показати всі діапазони")
	print("\n [0] \u001b[4m\u001b[31mназад\u001b[0m \n")
	a = input("rtscan ~$ ")
	if a == "1":
		addd()
	elif a == "2":
		f = open(hostsfile, "w")
		f.write("")
		f.close()
		print("діапазони видалено")
		t.sleep(0.6)
		restart_program()
	elif a == "3":
		if diapazons != []:
			for d in diapazons:
				print(str(d.strip()))
			t.sleep(5)
			menu1()
		else:
			print("немає діапазонів")
			t.sleep(3)
			menu1()
	elif a == "e" or a == "exit" or a == "0":
		clearx()
		restart_program()
		
	else:
		print('\033[91m'+'\033[1m'+"НЕПРАВЕЛЬНА КОМАНДА"+'\033[0m')
		t.sleep(3)
		clearx()
		title_bar("menu1")
		menu1()
def addd():
	a = input("ваш діапазон =>")
	f = open(hostsfile, 'a')
	f.write(str(a)+"\n")
	f.close()	
	restart_program()
def addp():
	a = input("ваш порт =>")
	f = open(portsfile, 'a')
	f.write(str(a)+"\n")
	f.close()	
	restart_program()


def menu2():
	title_bar('menu2')
	print("\n [1] додати порт")
	print("\n [2] видалити порт")
	print("\n [3] показати всі порти")
	print("\n [0] \u001b[4m\u001b[31mназад\u001b[0m \n")
	a = input("rtscan ~$ ")
	if a == "1":
		addp()
	elif a == "2":
		f = open(portsfile, "w")
		f.write("")
		f.close()
		print("порти видалено")
		t.sleep(0.6)
		restart_program()
	elif a == "3":
		if ports != []:
			for p in ports:
				print(str(p.strip()))
			t.sleep(5)
			clearx()
			menu2()
		else:
			print("портів немає!")
			t.sleep(3)
			menu2()
	elif a == "e" or a == "exit" or a == "0":
		clearx()
		restart_program()
	else:
		print('\033[91m'+'\033[1m'+"НЕПРАВЕЛЬНА КОМАНДА"+'\033[0m')
		t.sleep(3)
		clearx()
		title_bar("menu2")
		menu2()
		

def servertest(ip,p):
	try:
		host = str(ip)
		port = int(p)
		timeout = 5
		args = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
		for family, socktype, proto, canonname, sockaddr in args:
			s = socket.socket(family, socktype, proto)
			socket.setdefaulttimeout(timeout)
			try:
				s.connect(sockaddr)
			except:
				return False
			else:
				s.close()
				return True
	except KeyboardInterrupt:
		s.close()
		exit()
def ipcheck(ip,port):
	global goodip
	try:
		if servertest(ip,port):
			goodip.append(str(ip)+":"+str(port))
			print("[+] "+ str(ip)+":"+str(port))
		else:
			print("[-] "+ str(ip)+":"+str(port))
	except KeyboardInterrupt:
		exit()
def ipnetwork(st,fi):
	try:
		s = re.findall(r'\w+',st)
		f = re.findall(r'\w+',fi)
		start = str(s[0])+'.'+str(s[1])+'.'+str(s[2])+'.{}'
		finish = str(f[0])+'.'+str(f[1])+'.'+str(f[2])+'.{}'
		a = []
		for i in range(int(s[3]),(int(f[3])+1)):
			a.append(str(start.format(i)))
		return a
	except KeyboardInterrupt:
		exit()
def start():
	try:
		global diapazons
		global ports
		if diapazons == []:
			print('\033[91m'+'\033[1m'+"ПОМИЛКА НЕМАЄ ДІАПАЗОНІВ"+'\033[0m')
			t.sleep(2)
			restart_program()
		print("")
		if ports == []:
			print('\033[91m'+'\033[1m'+"ПОМИЛКА НЕМАЄ ПОРТІВ"+'\033[0m')
			t.sleep(2)
			restart_program()
		ip = []

		for d in diapazons:
			if d == "\n":
				break
			else:
	
				r = re.findall(r'\w+.\w+\w+.\w+.\w+',d)
				if r == '':
					print('diapazon error')
					break
				for ip in ipnetwork(r[0],r[1]):
					t.sleep(0.1)
					for p in ports:
						if p == "\n" or p == '' or p == [] or p == None:
							break
						else:
							t.sleep(0.1)

						#print(str(ip)+':'+str(p))
							ipcheck(str(ip),str(p))
		result()
	except KeyboardInterrupt:
		exit()


def result():
	global goodip
	title_bar("result")
	print("\n [1] пройтися по адресам (termux)")
	print("\n [2] \u001b[4m\u001b[31mназад\u001b[0m в меню")
	print("\n [3] вивести результати на екран")
	print("\n [0] \u001b[4m\u001b[31mвихід\u001b[0m \n")
#	print(goodip)
	a = input("rtscan ~$ ")
	if a == "1":
		for a in goodip:
			print(a)
			os.system("termux-open-url http://"+a)
			t.sleep(4)
			clearx()
		result()
	elif a == "2":
		clearx()
		
		menu()
	elif a == "3":
		for gip in goodip:
			print(gip)
			t.sleep(10)
			clearx()
		result()
	
	elif a == "e" or a == "exit" or a == "0":
		exit()
	else:
		print('\033[91m'+'\033[1m'+"НЕПРАВЕЛЬНА КОМАНДА"+'\033[0m')
		t.sleep(3)
		clearx()
		title_bar("result")
		result()



#####################
#    код програми   #
#####################'
try:
	start_program()
	dload()
	pload()
	menu()
except KeyboardInterrupt:
	exit()

