import requests
from colorama import Fore,init
init()
url = input("enter domain:")
reqe = requests.get("http://"+url)
if reqe.status_code == 200:
    print(Fore.GREEN+url+" is online and valid\n")
    reqe = requests.get("http://"+url+"/robots.txt")
    print(Fore.BLUE+reqe.text)
    print("\n-----------------------------")
    req = requests.get("intodns.com/"+url)
    print(req.text)