import tkinter
from tkinter import *
from tkinter import ttk
#setup
window = Tk()
window.geometry("370x90")
window.title("tk")

#button
def run():
    principal = eprinc.get()
    interest = eint.get()
    years = eyears.get()

    principal = int(principal)
    interest = int(interest)
    years = int(years)

    
    answer.config(text=str(principal*interest*years))
    return

lprinc = Label(window,text="Principal")
lint = Label(window,text="Interest Rate")
lyears = Label(window,text="Years")
lamount = Label(window,text="Amount")
l1 = Label(window,text="-")
answer = Label(window,text="-",background="grey",width=8)
eprinc = Entry(window)
eint = Entry(window)
eyears = Entry(window)

lprinc.grid(row=1,column=1)
lint.grid(row=1,column=2)
lyears.grid(row=1,column=3)
lamount.grid(row=4,column=1)
l1.grid(row=3,column=1)

eprinc.grid(row=2,column=1)
eint.grid(row=2,column=2)
eyears.grid(row=2,column=3)

answer.grid(row=4,column=2)
button = Button(window, text="run-", command=run )
button.grid(row=4,column=3)


window.mainloop()