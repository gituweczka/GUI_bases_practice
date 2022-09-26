from tkinter import *


def button_clicked():
    my_label["text"] = input.get()


window = Tk()
window.title("Gucia GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="Hey there bud", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click me too")
new_button.grid(column=2, row=0)

input = Entry(width=10)
input.grid(column=3, row=2)


window.mainloop()
