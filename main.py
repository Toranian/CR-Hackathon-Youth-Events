import pickle, time, os
from objects import *

# Hey! You there! If you are to edit this code, make sure you are using the pep 8
# style guide!  https://www.python.org/dev/peps/pep-0008/


# Loads the accounts and events from the accounts.txt and events.txt files.
if __name__ == "__main__":

    try:
        accounts = pickle.load(open("accounts.txt", "rb"))
        events = pickle.load(open("events.txt", "rb"))
        print("\n\n\n\n")
        print("_"*50)
        print(">>> Loaded accounts successfully!\n")
        print(accounts)
        for user in accounts:
            print(user)
        print(">>> Loaded events successfully!")
        for event in events:
            print(event.title)
        print("_"*50)
        print("\n\n\n\n")

    except:
        print("Failed. Creating a new accounts list!")
        accounts = [
            User("Isaac Morrow", "Toranian", "dragon"),
            User("Ethan Posner", "Enpro", "bigbad"),
            User("Nick Hopkins", "Tselenium", "bigcool"),
        ]
        pickle.dump(accounts, open("accounts.txt", "wb"))
        print(accounts)
        events = []
        pickle.dump(events, open("events.txt", "wb"))


# Initialize the control class which has most of the functions within it.
control = Control(accounts)
command_list = ["login", "signup", "home", "quit", "events", "userstats", "createevent"]


# Asks if the user has any account
has_account = control.yesno("Do you have an account?"); control.clear_screen(0)

# If the user has an account, they will be signed in
if has_account:
    active_user = control.login()

# creates a new account and makes the active_user live
if not has_account:
        try:
            name, username, password, age = control.create_account()
            new_user = User(name, username, password, age)
            accounts.append(new_user)
            pickle.dump(accounts, open("accounts.txt", "wb"))
            active_user = new_user
            control.output_message("Account '{}' created successfully.".format(active_user.username))

        except Exception as e:
            control.output_message("Account was not created successfully.\n{}".format(e))

# Main loop of the whole program! Will let the user select what they want.
loop = True
while loop:

    # Let's the user continue the program by hitting enter on the keyboard.
    control.continue_loop()
    control.clear_screen(0)

    # Get the command from the user
    control.output_message("What would you like to do? Type (h)elp for a list of commands.")
    command = control.input_message(" ").lower().replace(" ", "")

    if command == "":
        continue

    if command not in command_list:
        print("Command not recognized. Try typing (h)elp for a list of commands.\n")
        control.clear_screen()

    if "q" in command:
        print("Exiting the program!")
        quit()

    # Create a new account
    if "signup" in command:
        control.output_message("Creating a new user")
        try:
            name, username, password, age = control.create_account()
            new_user = User(name, username, password, age)
            accounts.append(new_user)
            pickle.dump(accounts, open("accounts.txt", "wb"))
            active_user = new_user
            control.output_message("Account '{}' created successfully.".format(active_user.username))

        except Exception as e:
            control.output_message("Account was not created successfully.\n{}".format(e))

    # Print the active users stats
    if "userstats" in command:
        control.clear_screen()
        active_user.get_stats()

    # Show all the available commands
    if "help" in command:
        for cmd in command_list:
            print(cmd)

    if "createevent" in command:
         title, description, time, location, created_by = control.create_event(active_user)
         new_event = Event(title, description, time, location, created_by)
         events.append(new_event)
         print(events)
         pickle.dump(events, open("events.txt", "wb"))
