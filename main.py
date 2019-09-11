# Author : Yash Mehta <https://github.com/y-mehta/twitter-bot>
# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================

# Main menu
def main_menu():
    os.system('clear')

    print ("Welcome to Twitter-bot")
    print ("Functionality includes, follwoing, retweetm and Like")
    print ("For the #kittens hashtag")
    print ("tweet functionality of pictures and text to come \n")
    menu()
    return

def menu():
    os.system('python3 bot.py')
    os.system('python3 follow-script.py')
    os.system('python retweet-script.py')
    os.system('python like_script.py')
    return

# Exit program
def exit():
    sys.exit()

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
