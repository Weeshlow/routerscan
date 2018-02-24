#!/usr/bin/python3
import socket
import subprocess as sp
import os
import sys
import time as t
try:
	from netaddr import IPNetwork
	import requests
except ModuleNotFoundError:
	print("будласка встановіть бібліотеки\npip install -r requirements.txt\n")
	exit()
#####################
#       змінні      #
#####################
_version_ = "2.0 release"
portsfile = "ports.txt"
hostsfile = "hosts.txt"
goodip = []
diapazons = []
ports = []
#####################
#     функції       #
#####################

def dload():
	
	f = open(hostsfile, 'r')
	for line in f:
		l = line.strip()
		diapazons.append(str(l))
	f.close()

def pload():
	f = open(portsfile, 'r')
	for line in f:
		l = line.strip()
		ports.append(str(l))
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
	os.system('clear')
	if title == "title":          
		print("\t            #####                                                        ")
		print("\t           #     #  ####  #####  #    #  ####   ####  #####   ##   #   # ")
		print("\t           #       #    # #    # ##   # #    # #        #    #  #   # #  ")
		print("\t           #  #### #    # #    # # #  # #    #  ####    #   #    #   #   ")
		print("\t           #     # #    # #####  #  # # #    #      #   #   ######   #   ")
		print("\t           #     # #    # #   #  #   ## #    # #    #   #   #    #   #   ")
		print("\t            #####   ####  #    # #    #  ####   ####    #   #    #   #   ")
	elif title == "menu":
		print("\t             MENU  routerscan " + _version_)
	elif title == "menu1":
		print("\t             ДІАПАЗОНИ routerscan " + _version_)
	elif title == "menu2":
		print("\t             ПОРТИ routerscan " + _version_)
	elif title == "result":
		print("\t             РЕЗУЛЬТАТИ routerscan "+_version_)
def menu():
	print("\n [1] довідка")
	print("\n [2] діапазони")
	print("\n [3] порти")
	print("\n [4] _почати_ ")
	print("\n [0] вихід \n")
	a = input("rtscan ~$ ")
	if a == "1":
		os.system("apt-get install nano && nano README.md")
		os.system("clear")
		title_bar("menu")
		menu()
	elif a == "2":
		os.system("clear")
		menu1()
	elif a == "3":
		os.system("clear")
		title_bar("menu2")
		menu2()
	elif a == "4":
		start()
	elif a == "e" or a == "exit" or a == "0":
		print("До побачення")
		t.sleep(0.5)
		os.system("clear")
		exit()
	else:
		print("неправельна команда")
		t.sleep(3)
		os.system("clear")
		title_bar("menu")
		menu()

def menu1():
	title_bar("menu1")
	print("\n [1] додати діапазон")
	print("\n [2] видалити діапазони")
	print("\n [3] показати всі діапазони")
	print("\n [0] назад \n")
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
		os.system("clear")
		title_bar("menu")
		dload()
		menu()
	else:
		print("неправельна команда")
		t.sleep(3)
		os.system("clear")
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
	print("\n [1] додати порт")
	print("\n [2] видалити порт")
	print("\n [3] показати всі порти")
	print("\n [0] назад \n")
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
			menu2()
		else:
			print("портів немає!")
			t.sleep(3)
			menu2()
	elif a == "e" or a == "exit" or a == "0":
		os.system("clear")
		title_bar("menu")
		pload()
		menu()
	else:
		print("неправельна команда")
		t.sleep(3)
		os.system("clear")
		title_bar("menu2")
		menu2()
		
#
def servertest(ip,p):
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

def ipcheck(ip,port):
	
	if servertest(ip,port):
		print("[+] "+str(ip)+":"+str(port))
	else:
		print("[-] "+str(ip)+":"+str(port))

def start():
	if diapazons == []:
		print("помилка немає діапазонів")
		t.sleep(0.4)
		restart_program()
	print("")
	if ports == []:
		print("помилка нема портів")
		restart_program()
	for d in diapazons:
		if d == "\n":
			break
		else:
			print("з діапазона " + d)
			for ip in IPNetwork (d):
				for port in ports:
					ipcheck(str(ip),str(port))
	result()



def result():
	title_bar("result")
	print("\n [1] пройтися по адресам (termux)")
	print("\n [2] назад в меню")
	print("\n [3] вивести результати на екран")
	print("\n [0] вихід \n")
	a = input("rtscan ~$ ")
	if a == "1":
		for a in goodip:
			print(a)
			os.system("termux-open-url http://"+a)
			t.sleep(10)
	elif a == "2":
		menu()
	elif a == "3":
		for l in goodip:
			print(l)
	
	elif a == "e" or a == "exit" or a == "0":
		restart_program()
	else:
		print("неправельна команда")
		t.sleep(3)
		os.system("clear")
		title_bar("result")
		result()



#####################
#    код програми   #
#####################
try:
	start_program()
	dload()
	pload()
	menu()
except KeyboardInterrupt:
	exit()
