import os
from lib.colors import *

print(f"""
     {bold}Vultest{end}
""")
print("[*] What do you want to test for?")
print(f"    {gray}[#][1]{end} {blue}XSS{end}")
print(f"    {gray}[#][2]{end} {blue}SQL Injection{end}")
print(f"    {gray}[#][3]{end} {red}Exit{end}")
print(" ")
option = input("[+] Select: ")

def scanner(option):
    if (option == "1"):
      print(f"""
--------------------------------------
{green}{bold}Xss scanner{end}
--------------------------------------
""")
      url = input("Enter Url: ")
      os.system('python3 main/anti-xss.py -u' + url)
    elif (option == "2"):
      print(f"""
--------------------------------------
{green}{bold}SQL Injection scanner{end}
--------------------------------------
""")
      url = input("Enter Url: ")
      os.system('python3 main/sqlifinder.py -d' + url)
    elif (option == "3"):
      print(f"""
--------------------------------------
{green}{bold}Goodbye:){end}
--------------------------------------
""")
      sys.exit()
    else:
        print("invalid input")

scanner(option)
