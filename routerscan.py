#!/usr/bin/python3
import os
import sys
import time as t
#####################
#       змінні      #
#####################
_version_ = "0.1 beta"
portsfile = "ports.txt"
hostsfile = "hosts.txt"
#####################
#     функції       #
#####################
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
	print("\n [2] видалити діапазон")
	print("\n [3] показати всі діапазони")
	print("\n [0] вихід \n")
	a = input("rtscan ~$ ")
	if a == "1":
		addd()
	elif a == "2":
		deld()
	elif a == "3":
		showd()
	elif a == "e" or a == "exit" or a == "0":
		os.system("clear")
		title_bar("menu")
		menu()
	else:
		print("неправельна команда")
		t.sleep(3)
		os.system("clear")
		title_bar("menu1")
		menu1()

def menu2():
	
	print("\n [1] додати порт")
	print("\n [2] видалити порт")
	print("\n [3] показати всі порти")
	print("\n [0] вихід \n")
	a = input("rtscan ~$ ")
	if a == "1":
		addp()
	elif a == "2":
		delp()
	elif a == "3":
		showp()
	elif a == "e" or a == "exit" or a == "0":
		os.system("clear")
		title_bar("menu")
		menu()
	else:
		print("неправельна команда")
		t.sleep(3)
		os.system("clear")
		title_bar("menu2")
		menu2()
	
def start():
	print('start')
#####################
#    код програми   #
#####################
start_program()
menu()

