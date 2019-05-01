accounts = {
    "steve": {
        "name": "Steven",
        "username": "steven99",
        "password": "dragon",
    }

}

users = []


width = 50
class User:

    """
    This class handles all the user functions and variables. This class is then stored in the accounts list and saved.
    """

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password



    def print_stats(self):
        print(self.name, self.username, self.password)

    def block_text(self, text, length=50):
        final_text = ""
        while len(self.text) >= length:
            final_text += text[0:length]



    def create_event(self, title, date, description, agemin, agemax):
        self.title = title
        self.date = date
        self.description = description
        self.agemin = agemin
        self.agemax = agemax

    def print_event(self):
        print(self.title.center(width))
        print("_"*width)
        print("\n{0: <30}".format(self.description))
        print("\nRecommended for ages {} - {}.".format(self.agemin, self.agemax))


steve = User("Steve", "steve99", "dragon")
users.append(steve)
steve.create_event("Party at Steve's", "July 12th, 3:30pm", "Come to Steves house for an absolute rager! It's totally wild and will be the night of your life!", 16, 18)
steve.print_event()
