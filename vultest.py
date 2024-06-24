import os
import sys
import subprocess
from lib.colors import *


def clear_screen():
    """Clears the terminal screen based on the OS."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')


def display_menu():
    """Displays the main menu for selecting a test."""
    clear_screen()
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
    print(f"    {gray}[#][q]{end} {red}Exit{end}")
    print(" ")


def scanner():
    """Handles the user's choice and runs the appropriate scanner."""
    display_menu()
    while True:
        option = input(f"{purple}=> Select: {end}").strip()
        if option in ["1", "2", "q"]:
            break
        else:
            print(f"{red}[!] Please enter a valid input (1, 2, q).{end}")

    if option == "1":
        print(f"""
--------------------------------------
{green}{bold}XSS Scanner{end}
--------------------------------------
""")
        url = input(f"{purple}=> Enter URL: {end}").strip()
        script_path = os.path.join('main', 'anti-xss.py')
        subprocess.run([sys.executable, script_path, '-u', url])

    elif option == "2":
        print(f"""
--------------------------------------
{green}{bold}SQL Injection Scanner{end}
--------------------------------------
""")
        url = input(f"{purple}=> Enter URL: {end}").strip()
        script_path = os.path.join('main', 'sqlifinder.py')
        subprocess.run([sys.executable, script_path, '-d', url])

    elif option == "q":
        print(f"""
--------------------------------------
{green}{bold}Goodbye :) {end}
--------------------------------------
""")
        sys.exit()


if __name__ == "__main__":
    try:
        scanner()
    except KeyboardInterrupt:
        print(f"\n{yellow}Scan cancelled by user.{end}")
        sys.exit()
    except Exception as e:
        print(f"{red}[!] An error occurred: {e}{end}")
        sys.exit(1)
