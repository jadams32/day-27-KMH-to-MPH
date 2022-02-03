# For day 27 I learned to use the tkinter, and build an application to turn kilometers per hour into miles per hour

from tkinter import *
FONT = ("Arial", 20, "normal")
window = Tk()
window.title("KMH to MPH Converter")
window.minsize(width=350, height=350)
window.config(padx=20, pady=20)


def convert():
    user_number = input_field.get()
    mph_value = round(int(user_number) * 0.62137119224)
    conversion_display.config(text=f"{mph_value}")


convert_button = Button(text="Convert", command=convert)
convert_button.grid(column=1, row=2)

input_field = Entry(width=8)
input_field.grid(column=1, row=0)


is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.grid(column=0, row=1)

conversion_display = Label(text="0", font=FONT)
conversion_display.grid(column=1, row=1)

kilometers_per_hour = Label(text="KPH", font=FONT)
kilometers_per_hour.grid(column=3, row=0)

miles_per_hour = Label(text="MPH", font=FONT)
miles_per_hour.grid(column=3, row=1)

window.mainloop()
