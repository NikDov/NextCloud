from cgi import test
import tkinter as tk
from Connector import Connector
from User import User
import credentials
from File import File

connector = Connector(credentials.NEXTCLOUD_URL, credentials.NEXTCLOUD_USERNAME, credentials.NEXTCLOUD_PASSWORD).nextcloud_connect()
user = User()

def create_user():
    username_in = username.get()
    password_in = password.get()
    print(username_in)
    user.create_user(connector, username_in, password_in)

    


adm_window = tk.Tk()
adm_window.title("Admin Window")
adm_window.geometry("500x400")
adm_window.resizable(False, False)

tk.Label(adm_window, text="Username").grid(row=0, column=0)
username = tk.Entry(adm_window)
username.grid(row=0, column=1)

tk.Label(adm_window, text="Password").grid(row=1, column=0)
password = tk.Entry(adm_window, show="*")
password.grid(row=1, column=1)

adm_window.grid_columnconfigure(0, minsize=100)


create_user_button = tk.Button(adm_window, text="Create user", command=create_user).grid(row=2, column=0)

adm_window.mainloop()

