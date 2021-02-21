# apenas outro exemplo do tkinter para informar se um número é primo ou não.

from tkinter import *

root = Tk()

label1 = Label(root, text="Enter Number")
E1 = Entry(root, bd=5)


def isPrime():
    global label1
    entry1 = E1.get()
    entry1 = int(entry1)
    for d in range(2, entry1):
        if entry1 % d == 0:
            label1.config(text="Not prime")
            break
    else:
        label1["text"] = "Prime"


submit = Button(root, text="Submit", command=isPrime)
root.update_idletasks()

label1.pack()
E1.pack()
submit.pack(side=BOTTOM)
root.mainloop()
