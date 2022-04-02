from tkinter import *
import time

root = Tk()
root.config(background="white")
root.geometry("400x200")
root.resizable(0, 0)
root.title("Clock")
# root.iconbitmap("C:\\Users\\umair\\Downloads\\calculator_jNH_icon.ico")

Clock = Label(root, font=('consolas', 50, 'normal'),
              fg='#737373', bg='#ffffff')
Clock.pack()

Date = Label(root, font=('consolas', 20, 'normal'), fg='#737373', bg='#ffffff')
Date.pack()


def tick():
    Time = time.strftime('%H:%M%p')
    date = (time.strftime('%A'), time.strftime(
        '%d') + "th", time.strftime('%Y'))
    Clock.config(text=Time)
    Date.config(text=date)
    Clock.after(20, tick)


tick()
root.mainloop()
