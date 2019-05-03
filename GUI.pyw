import tkinter as tk
import pickle

root = tk.Tk()
root.title("Campbell Rivents")
root.configure(bg = "grey70")
root.geometry("600x400")

main_frame = tk.Frame(root)

eventsLabel = tk.Label(root, text="test", fg="black", bg="grey70")
eventsLabel.place(relx=.5, rely=.6, anchor="center")

main_frame.tkraise()

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