import requests
import os.path
from os import path
domain = input("enter domain to scan : ")
wordlist = input("enter wordlist location : ")
save = str(input(" enter | y |  to save fond subdomains else enter | n | "))
if path.exists(wordlist):
    file.open(wordlist)
    content = file.read()
    possible_domains = content.splitlines()
    found_subdomains = []
    url = f"http://{possible_domains}.{domain}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[ + ] found domain : ",url)
        found_subdomains.append(url)
    if save=='y':
      file_name = str(input("enter file name to save as with extension : "))  
      with open(file_name, "w") as f:
          for possible_domains in found_subdomains:
              print(possible_domains, file=f)
