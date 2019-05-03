import tkinter as tk
import pickle

def changetologinframe():
    login_frame.tkraise()
    login_frame.pack()
    register_frame.pack_forget()

def changetoregisterframe():
    print("changing to register frame")
    register_frame.tkraise()
    register_frame.pack()
    login_frame.pack_forget()

def login():
    pass

def register():
    pass

root = tk.Tk()
root.title("Campbell Rivents")
root.configure(bg = "grey25")
root.geometry("600x400")

#frame for main menu
main_frame = tk.Frame(root)

eventsLabel = tk.Label(main_frame, text="test", fg="white", bg="grey25", font = ('consolas', 10, 'bold'))
eventsLabel.place(relx=.5, rely=.6, anchor="center")

#frame for login screen
login_frame = tk.Frame(root, bg="grey25", width=600, height=400)
#login_frame.grid_propagate(False)

login_label = tk.Label(login_frame, text = "LOGIN", fg = "white", bg = "grey25", font = ('consolas', 50, 'bold'))
login_label.place(relx=.5, rely=.4, anchor="center")
usernamelabel = tk.Label(login_frame, text="Username", font = ('consolas', 10, 'bold'), bg="grey25", fg="white")
usernamelabel.place(relx=.5, rely=.55, anchor="center")
usernamebox = tk.Entry(login_frame, width="20")
usernamebox.place(relx=.5, rely=.6, anchor="center")
passwordlabel = tk.Label(login_frame, text="Password", font = ('consolas', 10, 'bold'), bg="grey25", fg="white")
passwordlabel.place(relx=.5, rely=.75, anchor="center")
passwordbox = tk.Entry(login_frame, width="20")
passwordbox.place(relx=.5, rely=.8, anchor="center")
changetoregisterbutton = tk.Button(login_frame, text="register", font = ('consolas', 10, 'bold'), bg="white", fg="black", command=changetoregisterframe)
changetoregisterbutton.place(relx=.45, rely=.9, anchor="center")
loginbutton = tk.Button(login_frame, text="login", font = ('consolas', 10, 'bold'), bg="white", fg="black", command=login)
loginbutton.place(relx=.55, rely=.9, anchor="center")

login_frame.pack()

##
login_frame.pack_forget()
##

register_frame = tk.Frame(root, bg="grey25", width=600, height=400)

register_label = tk.Label(register_frame, text = "REGISTER", fg = "white", bg = "grey25", font = ('consolas', 50, 'bold'))
register_label.place(relx=.5, rely=.2, anchor="center")

fullnamelabel = tk.Label(register_frame, text="Full Name", font = ('consolas', 10, 'bold'), bg="grey25", fg="white")
fullnamelabel.place(relx=.5, rely=.4, anchor="center")
fullnamebox = tk.Entry(register_frame, width="20")
fullnamebox.place(relx=.5, rely=.45, anchor="center")

registerusernamelabel = tk.Label(register_frame, text="Username", font = ('consolas', 10, 'bold'), bg="grey25", fg="white")
registerusernamelabel.place(relx=.5, rely=.5, anchor="center")
registerusernamebox = tk.Entry(register_frame)
registerusernamebox.place(relx=.5, rely=.55, anchor="center")

ageLabel = tk.Label(register_frame, text="Age", font = ('consolas', 10, 'bold'), bg="grey25", fg="white")
ageLabel.place(relx=.5, rely=.6, anchor="center")
ageBox = tk.Entry(register_frame, width="5")
ageBox.place(relx=.5, rely=.65, anchor="center")

registerpasswordlabel = tk.Label(register_frame, text="Password", font = ('consolas', 10, 'bold'), bg="grey25", fg="white")
registerpasswordlabel.place(relx=.5, rely=.7, anchor="center")
registerpasswordbox = tk.Entry(register_frame)
registerpasswordbox.place(relx=.5, rely=.75, anchor="center")
confirmpasswordlabel = tk.Label(register_frame, text="Confirm Password", font = ('consolas', 10, 'bold'), bg="grey25", fg="white")
confirmpasswordlabel.place(relx=.5, rely=.8, anchor="center")
confirmpasswordbox = tk.Entry(register_frame, width="20")
confirmpasswordbox.place(relx=.5, rely=.85, anchor="center")
registerbutton = tk.Button(register_frame, text="register", font = ('consolas', 10, 'bold'), bg="white", fg="black", command=register)
registerbutton.place(relx=.45, rely=.95, anchor="center")
changetologinbutton = tk.Button(register_frame, text="login", font = ('consolas', 10, 'bold'), bg="white", fg="black", command=changetologinframe)
changetologinbutton.place(relx=.55, rely=.95, anchor="center")

register_frame.pack()

register_frame.tkraise()

if __name__ == "__main__":

    try:
        accounts = pickle.load(open("accounts.txt", "rb"))
        events = pickle.load(open("events.txt", "rb"))
        print("\n\n\n\n")
        print("_"*50)
        print(">>> Loaded accounts successfully!\n")
        for user in accounts:
            print(user.username)
        print("\n>>> Loaded events successfully!")
        for event in events:
            print(event.title)
        print("_"*50)
        print("\n\n\n\n")


    except:
        print("Failed. Creating a new accounts list!")
        # accounts = [
        #     User("Isaac Morrow", "Toranian", "dragon"),
        #     User("Ethan Posner", "Enpro", "bigbad"),
        #     User("Nick Hopkins", "Tselenium", "bigcool"),
        # ]
        # pickle.dump(accounts, open("accounts.txt", "wb"))
        # print(accounts)
        events = []
        pickle.dump(events, open("events.txt", "wb"))

root.mainloop()