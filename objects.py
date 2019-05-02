import os, time, pickle

# Hey! You there! If you are to edit this code, make sure you are using the pep 8
# style guide!  https://www.python.org/dev/peps/pep-0008/


# User accounts
class User:

    """
    This class handles all the user functions and variables. This class is then stored in the accounts list and saved.
    """

    def __init__(self, name=None, username=None, password=None, age=None):

        self.width = 50
        self.name = name
        self.username = username
        self.password = password
        self.age = age

    def get_stats(self):
        print("Stats:\n{}\nName: {}\nUsername: {}\nPassword: {}\nAge: {}\n{}".format("_"*50, self.name, self.username, self.password, self.age, "_"*50))

    def create_event(self, title, date, description, agemin, agemax):
        self.title = title
        self.date = date
        self.description = self.block_text(description)
        print(self.description)
        self.agemin = agemin
        self.agemax = agemax

    def print_event(self):
        print(self.title.center(self.width))
        print("_"*self.width)
        print("\n" +self.description)
        print("\nRecommended for ages {} - {}.".format(self.agemin, self.agemax))


# Event objects.
class Event:

    def __init__(self, title, description, time, location, created_by):
        self.title = title
        self.description = description
        self.time = time
        self.location = location
        self.created_by = created_by

    def display(self):
        print("Event display")


# The main control handler class of the program
class Control:

    """
    Contains many of the most critical functions in the program.
    """

    def __init__(self, accounts, user=None):
        self.user = user
        self.accounts = accounts
        self.width = 50

    # returns a true or false value based on the user input
    def yesno(self, message):
        while True:
            answer = self.input_message(message).lower()
            # answer = input("{}".format(message)).lower()
            if "y" in answer:
                return True
                break

            if "n" in answer:
                return False
                break

            else:
                print("Incorrect format entered. Try typing 'yes' or 'no'. Or, 'y' or 'n' for short.")

    # Logs the user in. Checks the database to see if the username and password match the records.
    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        for user in self.accounts:
            if username == user.username:
                if password == user.password:
                    self.clear_screen(0)
                    self.output_message("Signed in successfully")
                    return user
            else:
                print("That username is not recorded in our database. If you would like to create an account, type: signup.")

    # returns the name, username and password after the user creates an account.
    def create_account(self):

        name = input("\nWhat is your full name?\n: ")

        # create the username. Repeat if it is already in the database!
        while True:
            username = input("\nWhat would you like your username to be?\n: ")
            for user in self.accounts:
                if user.username == username:
                    print("That username already exists in our database. Please try again!")
            break

        age = input("\nHow old are you?:\n: ")

        # make sure the passwords match!
        while True:
            password = input("Create a password:\n:")
            confirm = input("Confirm your password:\n:")
            if password == confirm:
                print("Account Created successfully!")
                clear_screen()
                return name, username, password, age

    # clears the screen after a certain amount of time. Default value is 0.5 seconds.
    def clear_screen(self, wait=0.5):
        time.sleep(wait)

        os.system("cls")

        os.system("clear")

    # Output message
    def output_message(self, message):
        print("\n")
        print("_"*len(message))
        print("{}".format(message))
        print("_"*len(message))
        print("\n")

    def input_message(self, message):
        return input("{}\n-> ".format(message))

    # creates the event
    def create_event(self, active_user):
        # title = input("What would you like the title of your event to be?\n: ")
        # description = input("What would you like the description of your event to be?\n: ")
        title = self.input_message("What would you like the title of your event to be?")
        description = self.input_message("What would you like the description of your event to be?")
        time = self.input_message("What time would you like the event to be at?")
        location = self.input_message("Where is this event being held (location)?")
        created_by = active_user.username

        return title, description, time, location, created_by

    # Continue the loop after a user returns
    def continue_loop(self):
        input("\nPress enter to contine.\n")
