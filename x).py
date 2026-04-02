from tkinter import *

root = Tk()
root.title("Lenght Converter App")
root.geometry('400x400')

def calculate():
    inp = int(inps.get())
    ans.config(text=f"{inp} inches are {inp*2.54} centimeters")

inp_lbl = Label(text="Amount of inches:", bg="#49eb51")
inp_lbl.pack()
inps = Entry()
inps.pack()

btn = Button(text="Calculate", command=calculate)
btn.pack(pady=10)

ans = Label(text="", font=("Arial", 12))
ans.pack()

root.mainloop()