import requests
from colorama import Fore,init

init()
search = ["/login/",
"/admin/",
"/download/",
"/vip/",
"/search/",
"/python/",
"/hack/"]
page = input("Enter Domain name: ")


for website in search:
    req = requests.get("https://"+page+website)
    if req.status_code == 200:
        print(Fore.GREEN+"https://"+page+website+" URL Available")
    else:
        print(Fore.LIGHTRED_EX+"https://"+page+website+" Denied ")
