# Author : Yash Mehta <https://github.com/y-mehta/twitter-bot>
# Import the modules needed to run the script.
import sys, os
import subprocess

# Main definition - constants
menu_actions  = {}

# Main menu
def menu():
    subprocess.run("python3 photo_dict.py & python3 follow-script.py & python3 retweet_script.py & python3 like_script.py", shell=True)
    return

# Exit program
def exit():
    sys.exit()

# Main Program
if __name__ == "__main__":
    # Launch main menu
    menu()
