import os
from lib.colors import *
print(f"""
     {bold}Vultest{end}
""")
print("[*] What do you want to test for?")
print(f"    {gray}[#][1]{end} {blue}XSS{end}")
print(f"    {gray}[#][2]{end} {blue}SQL Injection{end}")
print(" ")
option = input("[+] Select: ")

def scanner(option):
    if (option == "1"):
      print(f"""
----------------
{green}{bold}Xss scanner{end}
----------------
""")
      url = input("Enter Url: ")
      os.system('python3 anti-xss.py -u' + url)
    elif (option == "2"):
      print(f"""
----------------
{green}{bold}SQL Injection scanner{end}
----------------
""")
      url = input("Enter Url: ")
      os.system('python3 sqlifinder.py -d' + url)
    else:
        print("invalid input")

scanner(option)
