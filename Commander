'''

@Date	: Sunday, June 22, 2013
@author	: The-Hydra (aka Abdel-Rahman Mohamed Moez)
@Version: 1.0

This script is to execute commands on the proxies you got
from the proxy grabber script.

You have the right to modify the script or use its idea ONLY BY GIVING ME THE CREDIT
'''
import ctypes
from _winreg import *
from colorama import *
import os
import winsound
import urllib2
import re
import time
#
init(autoreset=True)
#
def beep():
	winsound.Beep(1550,650)
def GET_EXTERNAL_IP():
	address = "http://www.ipchicken.com"
	string = urllib2.urlopen(address).read()
	EX_IP = re.search(r'\d+\.\d+\.\d+\.\d+', string).group()    
	return EX_IP
def TEST_PROXY(PROXY, PORT):
	try:
		proxy 	= urllib2.ProxyHandler({'http':PROXY+':'+PORT})
		auth	= urllib2.HTTPBasicAuthHandler()
		opener	= urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
		install = urllib2.install_opener(opener)
		IP		= GET_EXTERNAL_IP()
		return True
	except: 
		pass
		return False
def REFRESH_INTERNET_SETTINGS():
	INTERNET_OPTION_REFRESH = 37
	INTERNET_OPTION_SETTINGS_CHANGED = 39
	internet_set_option = ctypes.windll.Wininet.InternetSetOptionW
	internet_set_option(0, INTERNET_OPTION_REFRESH, 0, 0)
	internet_set_option(0, INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
def STOP_PROXY():
	aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
	aKey = OpenKeyEx(aReg, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, KEY_ALL_ACCESS)
	try:
		DeleteValue(aKey, "ProxyServer")
	except: pass
	SetValueEx(aKey,"ProxyEnable",0, REG_DWORD, 0) 
	CloseKey(aKey)
	REFRESH_INTERNET_SETTINGS()
	print Fore.RED+Style.BRIGHT+"\n\a Using PROXY has been stopped!"
def USE_PROXY(PROXY,IP):
	if TEST_PROXY(PROXY,IP) == True:
		PROXY_IP = str(PROXY+":"+str(IP))
		aReg = ConnectRegistry(None,HKEY_CURRENT_USER)
		aKey = OpenKeyEx(aReg, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, KEY_ALL_ACCESS)
		SetValueEx(aKey,"ProxyEnable",0, REG_DWORD, 1) 
		SetValueEx(aKey,"ProxyServer",0, REG_SZ, PROXY_IP) 
		CloseKey(aKey)
		REFRESH_INTERNET_SETTINGS()
		print Fore.GREEN+Style.BRIGHT+"\n\a \* Now you're using PROXY", PROXY_IP
	else:
		print Fore.RED+Style.BRIGHT+"\n\a \* Invalid PROXY!"
	
def COMMANDER():
	os.system('cls')
	os.system('title Proxy Commander - Coded by: The Hydra')
	print Back.RED+"\n\t\t<Note: This program must be run as Administrator>\t\t"
	print Fore.MAGENTA+Style.BRIGHT+"="*79
	print Fore.WHITE+Style.BRIGHT+" Command \t\t Description\n"
	print " test PROXY:PORT \t Test PROXY given to see if it works."
	print " list \t\t\t List all proxies in file."
	print " use PROXY:PORT \t Use a specific proxy."
	print " stop \t\t\t Stop using PROXY."
	print " del \t\t\t Delete PROXY_LIST.txt."
	print Fore.MAGENTA+Style.BRIGHT+"="*79
	cmd 	= raw_input(Fore.CYAN+'\n>>> PROXY COMMANDER: '+Style.BRIGHT)
	CMD 	= cmd.split(" ")
	try:
		PROXY	= CMD[1].split(":")[0]
		PORT	= CMD[1].split(":")[1]
	except: pass
	if CMD[0] == 'use':
		USE_PROXY(PROXY, PORT)
	elif CMD[0] == 'list':
		print "\n"+'-'*80
		if os.path.exists('PROXY_LIST.txt'):
			for line in open('PROXY_LIST.txt').readlines():
				print Fore.YELLOW+line
			print '-'*79
		else:
			print Fore.RED+"\n\a \* PROXY_LIST.txt files does not EXIST!"
			beep()
	elif CMD[0] == 'test':
		try:
			if TEST_PROXY(PROXY, PORT) == True:
				print Fore.GREEN+Style.BRIGHT+"\n\a \* Proxy is \x18 UP"
			else: 
				print Fore.RED+Style.BRIGHT+"\n\a \* Proxy is \x19 DOWN"
		except:
			print Fore.RED+Style.BRIGHT+"\n\a \* Proxy is \x19 DOWN"
		
	elif CMD[0] == 'stop':
		STOP_PROXY()
	elif CMD[0] == 'del':
		try:
			os.remove('PROXY_LIST.txt')
		except: pass
	else:
		print Fore.RED+Style.BRIGHT+"\n  Unkown Command!"
		beep()
	
	raw_input()

#
while 1: COMMANDER()
