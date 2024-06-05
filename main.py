from tkinter import *
window = Tk()

window.title("MILE TO KM")
window.minsize(width=400, height=200)

def button_click():
    choice = input.get()
    my_label["text"] = (f"Result: {int(choice)*1.6}")

my_label = Label(text=f"{"Put the mile"}", font=("Arial", 24, "bold"))
my_label.pack(side="left")
my_label.place(x=0, y=0)

input = Entry()
input.pack(side="right")
input.place(x=170, y=105)

butao = Button(text="Click Here", command=button_click)
butao.pack()
butao.place(x=100, y=100)





















window.mainloop()