import os, time, pickle

# clears the screen after a certain amount of time. Default value is 0.5 seconds.
def clear_screen(wait=0.5):
    time.sleep(wait)
    os.system("cls")

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

    def print_stats(self):
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
    
    def save_account(self, user, accounts):
        pickle.dump
class Control:

    """
    Contains many of the most critical functions in the program.
    """

    def __init__(self, accounts, user=None):
        self.user = user
        self.accounts = accounts
        self.width = 50

    def welcome(self):
        message = "Welcome to Campbell River Events!".center(self.width); print(message)
        print("_"*self.width)
        print("Would you like to sign in?\n")
        login = self.yesno()
        return login

    def yesno(self, message):
        while True:
            answer = input("{}".format(message)).lower()
            if "y" in answer:
                return True
                break

            if "n" in answer:
                return False
                break

            else:
                print("Incorrect format entered. Try typing 'yes' or 'no'. Or, 'y' or 'n' for short.")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        for user in self.accounts:
            if username == user.username:
                if password == user.password:
                    print("signed in successfully")
                    return user
            else:
                print("That username is not recorded in our database. If you would like to create an account, type: signup.")
    

# returns the name, username and password after the user creates an account.
def create_account(accounts):

    name = input("\nWhat is your full name?\n: ")
    
    # create the username. Repeat if it is already in the database!
    while True:
        username = input("\nWhat would you like your username to be?\n: ")
        for user in accounts:
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
            return (name, username, password, age)



