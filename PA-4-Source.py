from tkinter import *
from functools import partial

def main():
    window = Tk()
    window.config(bg='gray90')
    window.title("Staircase Problem")

    ##  User entry field for number of steps
    entry1 = Entry(window, width=30, fg='light grey', relief=FLAT)
    entry1.grid(row=0, column=0, padx=(50,5), pady=(10,5))
    entry1.insert(0, 'Enter number of steps (n ≥ 1)')
    entry1.bind('<FocusIn>', partial(onFocusIn, entry1, None))
    entry1.bind('<FocusOut>', partial(onFocusOut, entry1, None))

    ##  User entry field for set of allowed steps
    entry2 = Entry(window, width=30, fg='light grey', relief=FLAT)
    entry2.grid(row=1, column=0, padx=(50,5), pady=(0,5))
    entry2.insert(0, 'Enter set of allowed steps (Ex: 2,4)')
    entry2.bind('<FocusIn>', partial(onFocusIn, None, entry2))
    entry2.bind('<FocusOut>', partial(onFocusOut, None, entry2))

    ##  Button for submitting input
    Button(window, text='Calculate', command=partial(display, entry1, entry2)).grid(row=0, column=1, padx=(0,50), pady=(10,0))

    ##  Continue to display UI and wait for user input
    window.mainloop()

##  Removes placeholder text in entry box when user focuses in
def onFocusIn(entry1, entry2, e):
    if entry1:
        if entry1.get() == 'Enter number of steps (n ≥ 1)':
            entry1.delete(0, END)
            entry1.config(fg='black')
    else:
        if entry2.get() == 'Enter set of allowed steps (Ex: 2,4)':
            entry2.delete(0, END)
            entry2.config(fg='black')

##  Replaces placeholder text if user focuses out and no input was given
def onFocusOut(entry1, entry2, e):
    if entry1:
        if entry1.get() == '':
            entry1.insert(0, 'Enter number of steps (n ≥ 1)')
            entry1.config(fg='light grey')
    else:
        if entry2.get() == '':
            entry2.insert(0, 'Enter set of allowed steps (Ex: 2,4)')
            entry2.config(fg='light grey')

def display(entry1, entry2):
    print("Hello")

if __name__ == "__main__":
    main()
