import pickle, time, os
from objects import *


# Loads the accounts and events from the accounts.txt and events.txt files.
if __name__ == "__main__":

    try:
        accounts = pickle.load(open("accounts.txt", "rb"))
        # events = pickle.load(open("events.txt", "rb"))
        print("\n\n\n\n")
        print("_"*50)
        print(">>> Loaded accounts successfully!\n")

        for user in accounts:
            print(user.username)
        # print("accounts:", accounts)
        print("_"*50)
        print("\n\n\n\n")

    except:
        print("Failed. Creating a new accounts list!")
        accounts = [
            User("Isaac Morrow", "Toranian", "dragon"),
            User("Ethan Posner", "Enpro", "bigbad"),
            User("Nick Something", "Tselenium", "bigcool"),
        ]
        pickle.dump(accounts, open("accounts.txt", "wb"))
        print(accounts)

# Initialize the control class which has most of the functions within it.
control = Control(accounts)
command_list = ["login", "signup", "home", "quit", "events", "userstats"]
loop = True

has_account = control.yesno("Do you have an account?\n: ")

if has_account:
    active_user = control.login()

if not has_account:
        name, username, password, age = create_account(accounts)
        new_user = User(name, username, password, age)
        accounts.append(new_user)
        print("created a new account!", new_user.name)
        print(accounts)
        pickle.dump(accounts, open("accounts.txt", "wb"))
        active_user = new_user
        print("NO ERRORS!")



# Main loop of the whole program! Will let the user select what they want.
while loop:
    
    # Get the command from the user
    command = input("\nWhat would you like to do? Type (h)elp for a list of commands.\n: ").lower().strip()

    if command not in command_list:
        print("Command not recognized. Try typing (h)elp for a list of commands.\n")
        clear_screen()
    
    if "q" in command:
        print("Exiting the program!")
        quit()

    if "userstats" in command:
        active_user.print_stats()
    
    if "help" in command:
        for cmd in command_list:
            print(cmd)

    if "createevent" in command:
        


