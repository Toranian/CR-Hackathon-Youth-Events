import pickle

try:
    accounts = pickle.load(open("accounts.p", "rb"))
    events = pickle.load(open("events.p", "rb"))
    print("loaded accounts")
    print(accounts)

except:
    # accounts = {
    #     "steve": {
    #         "name": "Steven",
    #         "username": "steven99",
    #         "password": "dragon",
    #     }
    # }
    accounts = []
    print(accounts)
    print()

width = 50


class User:

    """
    This class handles all the user functions and variables. This class is then stored in the accounts list and saved.
    """

    def __init__(self, name=None, username=None, password=None):
        self.name = name
        self.username = username
        self.password = password

    def create_account(self):
        self.name = input("What is your full name?\n:")
        self.username = input("What would you like your username to be?\n:")

        while True:
            self.password = input("Create a password:\n:")
            confirm = input("Confirm your password:\n:")
            if self.password == confirm:
                print("Account Created successfully!")

    def print_stats(self):
        print(self.name, self.username, self.password)

    def create_event(self, title, date, description, agemin, agemax):
        self.title = title
        self.date = date
        self.description = self.block_text(description)
        print(self.description)
        self.agemin = agemin
        self.agemax = agemax

    def print_event(self):
        print(self.title.center(width))
        print("_"*width)
        print("\n" +self.description)
        print("\nRecommended for ages {} - {}.".format(self.agemin, self.agemax))


class Control:

    def __init__(self, accounts, user=None):
        self.user = user
        self.accounts = accounts

    def welcome(self):
        print("Welcome Campbell River Events!")
        print("Would you like to sign in?\n")
        login = self.yesno()
        if login:
            self.login(self.accounts)

    def yesno(self):
        while True:
            answer = input(": ").lower()
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

# steve.create_event("Party at Steve's", "July 12th, 3:30pm", "Come to Steves house for an absolute rager! It's totally wild and will be the night of your life!", 16, 18)

control = Control(accounts)


user = User("John Henry", "johnhenry99", "dragon")
user.print_stats()
accounts.append(user)
print(accounts)
pickle.dump(accounts, open("accounts.p", "wb"))
