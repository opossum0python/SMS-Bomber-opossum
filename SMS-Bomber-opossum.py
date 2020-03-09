from tkinter import *
from tkinter import messagebox
from Attack_Services import start
from loggin import Loggin
import threading


def spamm(code_country, phone):
    Loggin(code_country.get(), phone.get()).loggin()
    t = threading.Thread(target=start, args=(code_country.get(), phone.get()))
    t.start()


root = Tk()
root.title("SMS-Bomber-opossum")

code_country = StringVar()
phone = StringVar()

code_country_label = Label(text="Введите Код страны:")
phone_label = Label(text="Введите номер без кода страны:")

code_country_label.grid(row=0, column=0, sticky="w")
phone_label.grid(row=1, column=0, sticky="w")

code_country_entry = Entry(textvariable=code_country)
phone_entry = Entry(textvariable=phone)

code_country_entry.grid(row=0,column=1, padx=5, pady=5)
phone_entry.grid(row=1,column=1, padx=5, pady=5)


message_button = Button(text="Click Me", command=lambda: spamm(code_country, phone))
message_button.grid(row=2,column=1, padx=5, pady=5, sticky="e")

root.mainloop()
