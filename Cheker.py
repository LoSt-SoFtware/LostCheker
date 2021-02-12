import requests
import os
os.system('pip install heatshrink && pkg install figlet&&pip install figlet ')
os.system('xdg-open https://t.me/LO1STT')
os.system('clear')
os.system('figlet LOST')
print("=============================================")


t = raw_input(" List File : ")

print("=============================================")

file = open(t, 'r').readlines()
for x in file:
  u = x.strip()
  url = "https://instagram.com/"+u
  ss = requests.get(url)
  chk = ss.status_code
  if chk==200:
    print("\033[92mValid==== USER ====")
    print("User : "+u)
    print("status  : \033[92mValid\033[97m")
    print("=============")
    print(" ")
  elif chk==404:
    print("\033[91m==== USER ====")
    print("User : "+u)
    print("status : \033[91mNot Valid\033[97m")
    print("=============")
    print(" ")
    
os.system('figlet DONE')
