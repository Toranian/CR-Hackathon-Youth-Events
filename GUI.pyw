import gui_objects as objects
import tkinter as tk
import pickle


def changetomainframe():
    main_frame.tkraise()
    main_frame.pack()
    login_frame.pack_forget()
    register_frame.pack_forget()


def changetologinframe():
    login_frame.tkraise()
    login_frame.pack()
    register_frame.pack_forget()
    main_frame.pack_forget()


def changetoregisterframe():
    register_frame.tkraise()
    register_frame.pack()
    login_frame.pack_forget()
    main_frame.pack_forget()


def login():
    print("trying to log you in")
    global active_user

    username = usernamebox.get()
    password = passwordbox.get()
    loginmessagelabel.config(fg="grey25")
    active_user = control.login(username, password)

    if active_user != False:
        changetomainframe()
    else:
        print("login failed")
        loginmessagelabel.config(fg = "white")

def register():

    full_name = fullnamebox.get()
    username = registerusernamebox.get()
    age = ageBox.get()
    password = registerpasswordbox.get()
    confirmpassword = confirmpasswordbox.get()

    changetomainframe()

def showevents():
    for event in events:
        eventslabel.config(text = "{}\u2022{}: {}\n\n".format(eventslabel.cget("text"), event.title, event.description))

active_user = ""

if __name__ == "__main__":

    try:
        accounts = pickle.load(open("accounts.txt", "rb"))
        events = pickle.load(open("events.txt", "rb"))
        for user in accounts:
            print(user.username)
        for event in events:
            print(event.title)


    except:
        print("Failed. Creating a new accounts list!")
        events = []
        pickle.dump(events, open("events.txt", "wb"))

control = objects.Control(accounts)

root = tk.Tk()
root.title("Campbell Rivents")
root.configure(bg = "grey25")
root.geometry("600x400")

#frame for main menu
main_frame = tk.Frame(root, width=600, height=400, bg="grey25")

maintitleLabel = tk.Label(main_frame, text="Campbell Rivents", fg="white", bg="grey25", font = ('consolas', 20, 'bold'))
maintitleLabel.place(relx=.5, rely=.1, anchor="n")

eventslabel = tk.Label(main_frame, fg="white", bg="grey25", font = ('consolas', 15, 'bold'), justify="left", wraplength="400")
eventslabel.place(relx=.1, rely=.5, anchor="w")
showevents()

main_frame.pack()
main_frame.pack_forget()

#frame for login screen
login_frame = tk.Frame(root, bg="grey25", width=600, height=400)
#login_frame.grid_propagate(False)

loginmessagelabel = tk.Label(login_frame, text = "Login Failed", fg = "grey25", bg = "grey25", font = ('consolas', 10, 'bold'))
loginmessagelabel.place(relx=.5, rely=.2, anchor="center")

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

registermessagelabel = tk.Label(register_frame, text="User Already Exists", bg="grey25", fg="grey25")
registermessagelabel.place(relx=.5, rely=.05, anchor="center")

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

root.mainloop()
