import re
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.pattern = re.compile("^\w{0,10}$")
        self.label = tk.Label(self, text="Enter text")
        vcmd = (self.register(self.validateText), "%i", "%P")
        self.entry = tk.Entry(self, validate="key", validatecommand=vcmd, invalidcommand=self.printError)
        self.label.pack()
        self.entry.pack(anchor=tk.W, padx=10, pady=10)

    def validateText(self, index, text):
        print("Modification at index: " + index)
        return self.pattern.match(text) is not None

    def printError(self):
        print("Invalid text character!")

if __name__ == "__main__":
    app = App()
    app.mainloop()
