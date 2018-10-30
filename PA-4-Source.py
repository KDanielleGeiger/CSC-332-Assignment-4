from tkinter import *
from itertools import product
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

    ##  Display the number of ways to go up the steps
    labelText = StringVar()
    labelText.set('')
    label = Label(window, textvariable=labelText, bg='gray90', fg='blue').grid(row=2, column=0, columnspan=2, pady=(20,0))

    ##  Display each way to go up the steps
    listbox = Listbox(window, width=50, height=6, relief=FLAT)
    scrollbar = Scrollbar(window, orient=VERTICAL)
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    listbox.grid(row=3, column=0, columnspan=2, pady=(0,10))
    scrollbar.grid(row=3, column=0, columnspan=2, padx=(0,24), pady=(0,10), sticky=E+NS)

    ##  Button for submitting input
    Button(window, text='Calculate', command=partial(display, entry1, entry2, labelText, listbox)).grid(row=0, column=1, padx=(0,50), pady=(10,0))

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

##  Call functions to check user input, run the algorithm, and display the results on the UI
def display(entry1, entry2, labelText, listbox):
    try:
        if checkEntry1(entry1) and checkEntry2(entry2):
            n = int(Entry.get(entry1))
            steps = [int(i) for i in Entry.get(entry2).split(',')]
            
            count, paths = countPaths(n, steps)
            displayResults(count, paths, labelText, listbox)
        else:
            displayResults('Invalid Input.', [], labelText, listbox)
    except:
        displayResults('Error.', [], labelText, listbox)

##  Make sure the number of steps is a number >= 1
def checkEntry1(entry):
    try:
        n = int(Entry.get(entry))
        if n >= 1:
            return True
    except:
        return False
    return False

##  Make sure the set of allowed steps is of length >= 2 and each element is a number >= 1
def checkEntry2(entry):
    entry = Entry.get(entry).split(',')
    if len(entry) >= 2:
        try:
            entry = [int(i) for i in entry]
            if all(i >= 1 for i in entry):
                return True
        except:
            return False
    return False

##  Count the number of ways to go up the stairs and find all possible paths
def countPaths(n, steps):
    array = [0] * (n + 1)
    array[0] = 1

    ##  Return if impossible
    if min(steps) > n:
        return 0, []
    
    ##  Remove duplicates in allowed steps if they exist
    duplicateSteps = steps.copy()
    steps = []
    for i in duplicateSteps:
        if i not in steps:
            steps.append(i)

    ##  Calculate number of paths using an array
    array[min(steps)] = 1
    for i in range(min(steps) + 1, n + 1):
        for j in steps:
            if j <= n:
                array[i] += array[i - j]

    ##  Iteratively find each possible path and add each to the results array
    results = []
    for i in range(1, n + 1):
        for tup in list(product(steps, repeat=i)):
            if sum(tup) == n:
                result = list(tup)
                results.append(result)

    return array[n], results

##  Takes n (int or error message) and ways (2D array or empty array) and displays them on the UI
def displayResults(n, ways, labelText, listbox):
    ##  Format n and display in label
    if isinstance(n, str):
        text = n
    elif n == 0:
        text = 'There are no ways to go up the stairs.'
    elif n == 1:
        text = 'There is %s way to go up the stairs.' % n
    elif n < 1000000:
        text = 'There are %s ways to go up the stairs.' % n
    else:
        n = format(n, '.4e')
        text = 'There are %s ways to go up the stairs.' % n
    labelText.set(text)

    ##  Format ways and display in listbox
    listbox.delete(0, END)
    if ways == []:
        return
    else:
        count = 1
        item = ''
        output = []
        for i in ways:
            item += 'Way %s:   ' % count
            for j in i:
                item += '%s -> ' % j

            item = item[:-4]
            output.append(item)
            item = ''
            count += 1

        for i in output:
            listbox.insert(END, i)

if __name__ == "__main__":
    main()
