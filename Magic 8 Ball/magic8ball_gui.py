#!/usr/bin/env python3
"""Recreate magic 8 ball

Usage:

    python3 magic8ball_gui.py
"""

import random
from tkinter import *
from tkinter import messagebox

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)


class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("Magic 8 Ball")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        label = Label(self, text="What is your question?")
        label.pack(side=TOP, fill=X)

        # creating text entry instance
        global entry
        entry = Entry(self)
        entry.pack(fill=X)

        # creating a button instance / # placing the button on my window

        button_ask = Button(self, text="Ask", command=self.askcallback)
        button_ask.pack(side=LEFT, fill=X)

        button_clear = Button(self, text="Clear", command=self.clearcallback)
        button_clear.pack(side=LEFT, fill=X)

        button_quit = Button(self, text="Quit", command=self.quitcallback)
        button_quit.pack(side=LEFT, fill=X)

    def askcallback(self):
        answers = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful"]

        question = entry.get()
        msg = messagebox.showinfo("Ask", "Your question was: " +
                                  question + "\n\n" +
                                  "Magic 8 Ball says: " +
                                  random.choice(answers))
        entry.delete(0, END)

    def clearcallback(self):
        entry.delete(0, END)

    def quitcallback(self):
        exit()


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

#root.geometry("300x100")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
