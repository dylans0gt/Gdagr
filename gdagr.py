import urllib.request
import socket
import requests
from bs4 import BeautifulSoup
import dns.resolver
from googlesearch import search
from pyfiglet import Figlet

# Define the color codes
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

# Print the banner
def print_banner(text):
    custom_fig = Figlet(font='graffiti')
    print(f"{bcolors.FAIL}{custom_fig.renderText(text)}{bcolors.ENDC}")

# Print the legal disclaimer
def print_legal_disclaimer():
    print(f"{bcolors.OKBLUE}LEGAL DISCLAIMER: You shall not exploit any sensitive information you find using this tool. Doing so is highly illegal and will result in serious consequences.{bcolors.ENDC}")

# List available dorks
def list_dorks():
    print("Available Dorks:")
    for idx, dork in enumerate(dork_list, start=1):
        print(f"{idx}. {dork[1]}")

# Execute a dork query
def execute_dork_query(dork_index):
    query = dork_list[dork_index - 1][0]
    print(f"Executing query: {query}")
    for j in search(query, tld="co.in", num=20, stop=20, pause=2):
        print(j)

# Process action on webpage
def process_webpage_action(action, url):
    try:
        if action == "--emb":
            print_embedded_links(url)
        elif action == "--c":
            download_webpage_content(url)
        elif action == "--ip":
            print_ip_from_url(url)
        elif action == "--enum":
            enumerate_dns_records(url)
        else:
            print("Invalid action.")
    except Exception as e:
        print("Error:", e)

# Print embedded links in webpage
def print_embedded_links(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = [link.get('href') for link in soup.find_all('a')]
    print("Embedded Links:")
    for url in urls:
        print(url)

# Download webpage content
def download_webpage_content(url):
    response = urllib.request.urlopen(url)
    web_content = response.read().decode('UTF-8')
    with open('web_content.html', 'w') as f:
        f.write(web_content)
    print("Webpage content downloaded.")

# Print IP address from URL
def print_ip_from_url(url):
    ip_address = socket.gethostbyname(url)
    print(f"IP Address of {url}: {ip_address}")

# Enumerate DNS records of webpage
def enumerate_dns_records(url):
    domain = url
    answers = dns.resolver.resolve(domain, 'NS')
    print("DNS Records:")
    for server in answers:
        print(server.target)

if __name__ == "__main__":
    print_banner('gdagr')
    print(f"{bcolors.FAIL}by n0v4{bcolors.ENDC}\n")

    print_legal_disclaimer()
    print("\n1. passwords | 2. card numbers | 3. cameras | 4. servers | 5. ssh keys | 6. government documents\n")

    first_input = input(f"{bcolors.FAIL}Type 1, 2, 3, 4, 5, or 6\nOr, type gdagr --list_dorks to view more Google Dorking Commands: {bcolors.ENDC}\n")

    dork_list = [
        ('allintext:password filetype:log after:2020', 'Passwords'),
        ('inurl:choosecard.php?catid=', 'Card Numbers'),
        ('intitle:webcamXP 5', 'Cameras'),
        ('inurl:/proc/self/cwd', 'Servers'),
        ('intitle:index.of id_rsa -id_rsa.pub', 'SSH Keys'),
        ('allintitle: restricted filetype:doc site:gov', 'Government Documents')
    ]

    if first_input == "gdagr --list_dorks":
        list_dorks()
    elif first_input.isdigit() and int(first_input) in range(1, 7):
        execute_dork_query(int(first_input))
    else:
        print("Invalid input.")
        exit()

    print("\nWhat would you like to do about the webpage you visited?")
    print("gdagr --emb URL: finds all embedded links")
    print("gdagr --c URL: downloads raw content of the webpage")
    print("gdagr --ip URL: url to ip address translation")
    print("gdagr --enum URL: view dns records of webpage\n")

    second_input = input("Enter command first. Then you will be prompted for the URL: ")

    action, url = second_input.split(maxsplit=1)

    process_webpage_action(action, url)
