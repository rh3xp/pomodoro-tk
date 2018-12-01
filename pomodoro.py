#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


main = Tk()
main.title('Pomodoro Clock')
main.geometry("300x200")
main.option_add('*Dialog.msg.width', 20)

#def startPomo():
#    global timeProvided
#    timeProvided = time.get()
    #print("Pomodoro Clock " + timeProvided)
#    lbl.config(text='Time provided: '+ timeProvided)

def popupMessage():
    global totalTime
    totalTime = time.get()
    output = messagebox
    msg = output.showinfo( "Pomodoro Clock", totalTime)

timeLabel = Label(main, text = "Enter time")
timeLabel.pack()
time = Entry(main)
time.pack()

# print in the same window
#submit = Button(main, text = "Submit", command = startPomo)
#submit.place(x = 100, y = 100)
#lbl = Label(main)
#lbl.pack()

# create a new popup
popup = Button(main, text = "Submit", command = popupMessage)
popup.place(x = 100,y = 100)


main.mainloop()
