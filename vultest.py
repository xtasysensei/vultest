import os
import sys
import subprocess
from lib.colors import *


def display_menu():
    print(f"""
    {yellow}{bold}
 #     #                                        
 #     # #    # #      ##### ######  ####  #####
 #     # #    # #        #   #      #        #  
 #     # #    # #        #   #####   ####    #  
  #   #  #    # #        #   #           #   #  
   # #   #    # #        #   #      #    #   #  
    #     ####  ######   #   ######  ####    # 
    {end}
    """)
    print("[*] What do you want to test for?")
    print(f"    {gray}[#][1]{end} {blue}XSS{end}")
    print(f"    {gray}[#][2]{end} {blue}SQL Injection{end}")
    print(f"    {gray}[#][3]{end} {red}Exit{end}")
    print(" ")


def scanner(option):
    if option == "1":
        print(f"""
--------------------------------------
{green}{bold}XSS Scanner{end}
--------------------------------------
""")
        url = input("Enter URL: ")
        script_path = os.path.join('main', 'anti-xss.py')
        subprocess.run(['python', script_path, '-u', url])
    elif option == "2":
        print(f"""
--------------------------------------
{green}{bold}SQL Injection Scanner{end}
--------------------------------------
""")
        url = input("Enter URL: ")
        script_path = os.path.join('main', 'sqlifinder.py')
        subprocess.run(['python', script_path, '-d', url])
    elif option == "3":
        print(f"""
--------------------------------------
{green}{bold}Goodbye :) {end}
--------------------------------------
""")
        sys.exit()
    else:
        print("Invalid input")


if __name__ == "__main__":
    display_menu()
    option = input("[+] Select: ").strip()
    scanner(option)
