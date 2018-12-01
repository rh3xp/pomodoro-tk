#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


main = Tk()
main.title('Pomodoro Clock')
main.geometry("300x200")

#def startPomo():
#    global timeProvided
#    timeProvided = time.get()
    #print("Pomodoro Clock " + timeProvided)
#    lbl.config(text='Time provided: '+ timeProvided)


#main.option_add('*Dialog.msg.width', 20)
#def popupMessage():
#    global totalTime
#    totalTime = time.get()
#    output = messagebox
#    msg = output.showinfo( "Pomodoro Clock", totalTime)


WELCOME_DURATION = 5000
def popupMessage():
    global totalTime
    totalTime = time.get()
    top = Toplevel()
    top.title('Pomodoro Clock')
    Message(top, text=totalTime, padx=70, pady=70).pack()
    top.after(WELCOME_DURATION, top.destroy)


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
