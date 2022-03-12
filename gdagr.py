# refined code for gdagr (formerly gec-yume)

import urllib.request, urllib.error, urllib.parse
from pyfiglet import Figlet
import socket
from googlesearch import search
import requests

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

custom_fig = Figlet(font='graffiti')
print(f"{bcolors.FAIL}{custom_fig.renderText('gdagr')}{bcolors.ENDC}")
print(f"{bcolors.FAIL}by n0v4{bcolors.ENDC}")
print(" ")
print(f"{bcolors.FAIL}1. passwords | 2. card numbers | 3. cameras | 4. servers | 5. ssh keys | 6. government documents{bcolors.ENDC}")
print(" ")
print(" ")
print(f"{bcolors.OKBLUE}LEGAL DISCLAIMER: You shall not exploit any sensitive information you find using this tool. Doing so is highly illegal and will result in serious consequences.{bcolors.ENDC}")

print(" ")

first_input = input(f"{bcolors.FAIL}Type 1,2,3,4,5, or 6\nOr, type gdagr --list_dorks to view more Google Dorking Commands: {bcolors.ENDC}")

print(" ")

dork_list = [('1', 'allintext:password filetype:log after:2020'),  ('2', 'inurl:choosecard.php?catid='), 
			('3', 'intitle:webcamXP 5'), ('4', 'inurl:/proc/self/cwd'), ('5', 'intitle:index.of id_rsa -id_rsa.pub'), 
			('6', 'allintitle: restricted filetype:doc site:gov')]


# fix this by making the result pages longer 

if first_input == "gdagr --list_dorks":
	print(" ")

for i in range(len(dork_list)):
    if dork_list[i][0] == first_input:
    	for j in search(first_input, tld="co.in", num=20, stop=20, pause=2):
    		print(j)
    	print(" ")

print("What would you like to do about the webpage you visited?")

print("gdagr --emb URL: finds all embedded links\ngdagr --c URL: downloads raw content of the webpage\ngdagr --ip URL: url to ip address translation\ngdagr --enum URL: view dns records of webpage")

second_input = input("Enter command first. Then you will be prompted for the URL: ")

if second_input == "gdagr --emb":
	url = input("Enter URL: ")
	requests_ = requests.get(url)
	soup = BeautifulSoup(reqs.text, 'html.parser')
	
	urls = []
	for link in soup.find_all('a'):
		print(link.get('href'))

if second_input == "gdagr --c":
	url = input("Enter URL: ")
	response = urllib.request.urlopen(url)
	webContent = response.read().decode('UTF-8')

	f = open('obo-t17800628-33.html', 'w')
	f.write(webContent)
	f.close
	
if second_input == "gdagr --ip":
	url = input("Enter URL: ")
	print("IP Address:",socket.gethostbyname(url))
	
if second_input == "gdagr --enum":
	url = input("Enter URL: ")
	domain = url
	answers = dns.resolver.resolve(domain, 'NS')
	for server in answers:
		print(server.target)

