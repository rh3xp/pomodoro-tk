#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox


main = Tk()
main.title('Pomodoro Clock')
main.geometry("300x200")
main.option_add('*Dialog.msg.width', 20)

# in the same window
#def startPomo():
#    global timeProvided
#    timeProvided = time.get()
    #print("Pomodoro Clock " + timeProvided)
#    lbl.config(text='Time provided: '+ timeProvided)

# in the same window
#submit = Button(main, text = "Submit", command = startPomo)
#submit.place(x = 100, y = 100)
#lbl = Label(main)
#lbl.pack()


ERROR_DURATION = 3000

def popupMessage():
    global totalTime
    try:
        totalTime = time.get()
        totalTime = int(totalTime)
        msg = messagebox.showinfo( "Pomodoro Clock", totalTime)
    except ValueError:
        top = Toplevel()
        top.title('Error')
        Message(top, text=totalTime+" is not any time.", padx=70, pady=70).pack()
        top.after(ERROR_DURATION, top.destroy)


timeLabel = Label(main, text = "Enter time")
timeLabel.pack()
time = Entry(main)
time.pack()

# create a new popup
popup = Button(main, text = "Submit", command = popupMessage)
popup.place(x = 100,y = 100)

main.mainloop()
