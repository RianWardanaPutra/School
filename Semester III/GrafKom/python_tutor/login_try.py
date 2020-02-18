import tkinter as tk

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        self.loginButton = tk.Button(self, text="Log in", 
                                    command=self.printLogin)
        self.clearButton = tk.Button(self, text="Clear",
                                    command=self.clearForm)
        self.username.pack()
        self.password.pack()
        self.loginButton.pack(fill=tk.BOTH)
        self.clearButton.pack(fill=tk.BOTH)

    def printLogin(self):
        print(f"Username: {self.username.get()}")
        print("Password: {}".format(self.password.get()))

    def clearForm(self):
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        self.username.focus_set()

if __name__=="__main__":
    app = LoginApp()
    app.mainloop()