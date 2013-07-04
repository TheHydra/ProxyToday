'''

@Date	: Sunday, June 22, 2013
@author	: The-Hydra (aka Abdel-Rahman Mohamed Moez)
@Version: 1.0

This script is for grabbing proxies IPs:PORTS and listing them
in well formatted way and exporting them into a text file.

You have the right to modify the script or use its idea ONLY BY GIVING ME THE CREDIT

'''
#############################################
from BeautifulSoup import BeautifulSoup as BS
import urllib
import urllib2
import re
from colorama import *
import os
import sys
import time
#############################################
os.system('cls')
os.system('title Proxy Grabber - Coded by: The Hydra')
init(autoreset=True)
#############################################
def GET_EXTERNAL_IP():
	address = "http://www.ipchicken.com"
	string = urllib2.urlopen(address).read()
	EX_IP = re.search(r'\d+\.\d+\.\d+\.\d+', string).group()    
	return EX_IP
def LIST_PROXY_LIST():
	proxyURL	= 'http://gatherproxy.com'
	soup		= BS(urllib2.urlopen(proxyURL))
	print Fore.CYAN+"="*79
	print Style.BRIGHT+Fore.RED+"IP "+Fore.GREEN+"\t\tPORT"+Fore.YELLOW+" \tType"+Fore.WHITE+"\t\tCountry, City"
	print Fore.CYAN+"="*79
	for tag in soup.findAll('script'):
		try:
			PROXY_IP		= re.search(r'"PROXY_IP":"\d*.\d*.\d*.\d*"',str(tag)).group()[12:-1]
			PROXY_PORT		= re.search(r'"PROXY_PORT":"\d*"',str(tag)).group()[14:-1]
			PROXY_TYPE		= re.search(r'"PROXY_TYPE":"[a-zA-Z0-9-_]*"',str(tag)).group()[14:-1]
			PROXY_COUNTRY	= re.search(r'"PROXY_COUNTRY":"[a-zA-Z0-9-_]*"',str(tag)).group()[17:-1]
			if PROXY_TYPE == 'Elite': PROXY_COUNTRY = '\t'+PROXY_COUNTRY
			PROXY_CITY		= re.search(r'"PROXY_CITY":"[a-zA-Z0-9-_ ]*"',str(tag)).group()[14:-1]
			if TEST_PROXY(PROXY_IP, PROXY_PORT) == True:

				OUTPUT = str(Style.BRIGHT+Fore.RED+PROXY_IP+"\t"+str(Fore.GREEN+PROXY_PORT)+"\t"+str(Fore.YELLOW+PROXY_TYPE)+"\t"+str(Fore.WHITE+PROXY_COUNTRY)+", "+str(Fore.WHITE+PROXY_CITY))
				print OUTPUT
		except: pass

def TEST_PROXY(PROXY, PORT):
	proxy 	= urllib2.ProxyHandler({'http':PROXY+':'+PORT})
	auth	= urllib2.HTTPBasicAuthHandler()
	opener	= urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
	install = urllib2.install_opener(opener)
	IP		= GET_EXTERNAL_IP()
	if REAL_IP == IP:
		return False
	else:
		PROXY_FILE = open('PROXY_LIST.txt','a')
		PROXY_FILE.write(PROXY+":"+PORT+"\n")
		PROXY_FILE.close()
		return True
##############################################
global REAL_IP
REAL_IP = GET_EXTERNAL_IP()
print Fore.CYAN+"="*79
print Fore.GREEN+Style.BRIGHT+"[+] Your REAL IP: "+Fore.WHITE+REAL_IP
#
while 1: LIST_PROXY_LIST()
