import tkinter as tk
import math as mt


alpha = 5
beta = 50
gama = -40

xwmin = -100; xwmax = 100
ywmin =  0; ywmax = 300

xvmin = 0; xvmax = 600
yvmin = 0; yvmax = 700

x, y, xi, yi = 0, 0, 0, 0


def windowToView(xw, yw):
    xv = xvmin + round((xw - xwmin) / (xwmax - xwmin) * (xvmax - xvmin))
    yv = yvmax - round((yw - ywmin) / (ywmax - ywmin) * (yvmax - yvmin))
    return (xv, yv)

def viewToWindow(xv, yv):
    xw = xwmin + (xv - xwmin) * (xwmax - xwmin) / (xvmax - xvmin)
    yw = ywmin + (yvmax - yv) * (ywmax - ywmin) / (yvmax - yvmin)
    return (xw, yw)


class FractalTree(tk.Tk):
                
    def __init__(self):
        super().__init__()

        self.a = [0] * 4
        self.b = [0] * 4
        self.c = [0] * 4
        self.d = [0] * 4
        self.e = [0] * 4
        self.f = [0] * 4

        self.a[0] = 0
        self.b[0] = 0
        self.c[0] = 0
        self.d[0] = 0.2
        self.e[0] = 0
        self.f[0] = 0

        self.a[1] =  0.85 * mt.cos(alpha * mt.pi / 180)
        self.b[1] = -0.85 * mt.sin(alpha * mt.pi / 180)
        self.c[1] =  0.85 * mt.sin(alpha * mt.pi / 180)
        self.d[1] =  0.85 * mt.cos(alpha * mt.pi / 180)
        self.e[1] =  0
        self.f[1] =  1.9

        self.a[2] =  0.3  * mt.cos(beta * mt.pi / 180)
        self.b[2] = -0.34 * mt.sin(beta * mt.pi / 180)
        self.c[2] =  0.3  * mt.sin(beta * mt.pi / 180)
        self.d[2] =  0.34 * mt.cos(beta * mt.pi / 180)
        self.e[2] =  0 
        self.f[2] =  1.5 

        self.a[3] =  0.3  * mt.cos(gama * mt.pi / 180)
        self.b[3] = -0.34 * mt.sin(gama * mt.pi / 180)
        self.c[3] =  0.3  * mt.sin(gama * mt.pi / 180)
        self.d[3] =  0.34 * mt.cos(gama * mt.pi / 180)
        self.e[3] =  0
        self.f[3] =  1.2

        self.title = "Tugas 5 Rian Wardana"
        self.canvas = tk.Canvas(self, bg="white", width=800, height=800)
        self.elipse = self.canvas.create_oval(100,100,600,700)
        self.canvas.pack()
        self.treeDraw()

    def treeDraw(self):
        iteration = 500
        k = 0
        while k <= iteration:
            for i in range(xvmax):
                for j in range(yvmax):
                    p = checkPointInCircle(i, j, 350, 400, 250, 300)
                    if p <= 1:
                        x, y = viewToWindow(i,j)
                        xb = self.a[0] * x + self.b[0] * y + self.e[0]
                        yb = self.c[0] * x + self.d[0] * y + self.f[0]
                        xi, yi = windowToView(xb, yb)
                        self.canvas.create_oval(xi,yi,xi+1,yi+1, fill="brown", outline="brown", width=4)
                        
                        xb = self.a[1] * x + self.b[1] * y + self.e[1]
                        yb = self.c[1] * x + self.d[1] * y + self.f[1]
                        xi, yi = windowToView(xb, yb)
                        self.canvas.create_oval(xi, yi, xi, yi+1, fill="green", outline="green")
                        
                        xb = self.a[2] * x + self.b[2] * y + self.e[2]
                        yb = self.c[2] * x + self.d[2] * y + self.f[2]
                        xi, yi = windowToView(xb, yb)
                        self.canvas.create_oval(xi, yi, xi, yi+1, fill="green", outline="green")
                        
                        xb = self.a[3] * x + self.b[3] * y + self.e[3]
                        yb = self.c[3] * x + self.d[3] * y + self.f[3]
                        xi, yi = windowToView(xb, yb)
                        self.canvas.create_oval(xi, yi, xi, yi+1, fill="green", outline="green")
                        self.canvas.update()
            k += 1

def checkPointInCircle(x, y, h, k, a, b):
    
    p = ((((x - h) ** 2) // (a ** 2)) + 
         (((y - k) ** 2) // (b ** 2)))
    
    return p

if __name__ == "__main__":
    app = FractalTree()
    app.mainloop()