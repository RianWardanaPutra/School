from tkinter import *

root = Tk()
root.title("Graff")
mainframe = Frame(root, width=800, height=600)

mainframe.grid()
canvas = Canvas(root, width=800, height=600, background="red")
canvas.grid()
root.mainloop()
