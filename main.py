# For day 27 I learned to use the tkinter, and build an application to turn kilometers per hour into miles per hour

from tkinter import *
FONT = ("Arial", 20, "normal")
window = Tk()
window.title("KMH to MPH")
window.minsize(width=500, height=300)


def convert(self):
    pass


button = Button(text="Convert")
button.grid(column=1, row=3)


my_label = Label(text="is equal to", font=FONT)
my_label.grid(column=0, row=2)
my_label.config(padx=25, pady=25)

my_label = Label(text="0", font=FONT)
my_label.grid(column=1, row=2)
my_label.config(padx=25, pady=25)

my_label = Label(text="Miles", font=FONT)
my_label.grid(column=3, row=1)
my_label.config(padx=25, pady=25)

my_label = Label(text="KMH", font=FONT)
my_label.grid(column=3, row=2)
my_label.config(padx=25, pady=25)

window.mainloop()