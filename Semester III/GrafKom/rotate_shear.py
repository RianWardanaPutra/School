#!/usr/bin/env python

import tkinter as tk

class Graff(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Rotate and Shear")
        container = tk.Frame(self, width=1000, height=800)
        canvas = tk.Canvas(container, background="white", width=800, height=600)
        canvas.create_polygon([100,100,200,200,100,200], outline="blue", fill="cyan", width=3)
        container.grid()
        canvas.grid()

if __name__ == "__main__":
    app = Graff()
    app.mainloop()

