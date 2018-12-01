#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


main = Tk()
main.title('Pomodoro Clock')
main.geometry("200x150")

def startPomo():
    global timeProvided
    timeProvided = time.get()
    print("Pomodoro Clock " + timeProvided)
    lbl.config(text='Time provided: '+ timeProvided)

timeLabel = Label(main, text = "Enter time")
timeLabel.pack()
time = Entry(main, bd = 5)
time.pack()

submit = Button(main, text = "Submit", command = startPomo)
submit.place(x = 100, y = 100)

lbl = Label(main)
lbl.pack()


main.mainloop()
