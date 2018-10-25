#!/usr/bin/env python3
"""Checks if sides of triangles make a Pythagorean Triple.

Usage:

    python3 pythagoreantriplechecker.py
"""

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
        self.master.title("Pythagorean Triple Checker")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        label = Label(self, text="Input the sides of your triangle below.")
        label.grid(columnspan=2, padx=5, pady=10, sticky=W)

        label = Label(self, text="Side A : ")
        label.grid(column=0, row=1)

        label = Label(self, text="Side B : ")
        label.grid(column=0, row=2)

        label = Label(self, text="Side C : ")
        label.grid(column=0, row=3)

        # creating text entry instance
        global entry_a
        entry_a = Entry(self)
        entry_a.grid(column=1, row=1)
        entry_a.focus_set()
        entry_a.bind('<Return>', Window.go_to_entry_b)

        global entry_b
        entry_b = Entry(self)
        entry_b.grid(column=1, row=2)
        entry_b.bind('<Return>', Window.go_to_entry_c)

        global entry_c
        entry_c = Entry(self)
        entry_c.grid(column=1, row=3)
        entry_c.bind('<Return>', lambda event: Window.submitcallback(self))

        # creating a button instance / # placing the button on my window

        button_submit = Button(self, text="Submit", command=self.submitcallback)
        button_submit.grid(column=2, row=4, padx=10, pady=10, sticky=W)

        button_clear = Button(self, text="Clear", command=self.clearcallback)
        button_clear.grid(column=1, row=4, pady=10, sticky=W)

        button_quit = Button(self, text="Quit", command=self.quitcallback)
        button_quit.grid(column=2, row=0, padx=10, pady=10, sticky=E)

    def go_to_entry_b(self):
        entry_b.focus_set()

    def go_to_entry_c(self):
        entry_c.focus_set()

    def submitcallback(self):

        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())

        if a and b <= c:
            if a*a + b*b == c*c:
                answer = "Yes, this is a Pathagorean Triple"
            else:
                answer = "No, this is not a Pathagorean Triple"
        else:
            answer = "ERROR: The hypotenuse (c) is always the longest side. " \
                     "Please re-enter the sides, " \
                     "entering the longest side into 'Side C'"

        msg = messagebox.showinfo("Submit", answer)
        
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_c.delete(0, END)
        entry_a.focus_set()

    def clearcallback(self):
        entry_a.delete(0, END)
        entry_b.delete(0, END)
        entry_c.delete(0, END)
        entry_a.focus_set()

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
