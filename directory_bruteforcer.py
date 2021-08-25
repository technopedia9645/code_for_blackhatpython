#this is edited from the subdomain scanner i made 
import requests
import os.path
from os import path
domain = input("enter url to scan : ")
wordlist = input("enter wordlist location : ")
save = str(input(" enter | y |  to save fond directories else enter | n | "))
if path.exists(wordlist):
    file.open(wordlist)
    content = file.read()
    possible_directories = content.splitlines()
    found_directories = []
    url = f"http://{domain}.{possible_directories}"
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("[ + ] found domain : ",url)
        found_directories.append(url)
    if save=='y':
      file_name = str(input("enter file name to save as with extension : "))  
      with open(file_name, "w") as f:
          for possible_directories in found_directories:
              print(possible_directories, file=f)
