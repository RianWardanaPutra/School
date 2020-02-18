from tkinter import *
from tkinter import ttk

# function to calculate feet to meters
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Main window
root = Tk()
root.title("Feet to Meter")

# Main frame in window
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

# placing widget on frame
feetEntry = ttk.Entry(mainframe, width=7, textvariable=feet)
feetEntry.grid(column=2, row=1, sticky=(W,E))
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equal to: ").grid(column=1, row = 2, sticky=E)
ttk.Label(mainframe, text=" meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feetEntry.focus()
root.bind('<Return>', calculate)

root.mainloop()