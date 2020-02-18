from tkinter import *
from math import *

root = Tk()
root.title("Barnsley Ferns - Rian Wardana")

x, y = 0, 0
xi, yi = 0, 0
items = []

xwmin = -3
xwmax =  3
ywmin =  0
ywmax =  7

xvmin =   0
xvmax = 600
yvmin =   0
yvmax = 700

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

mainframe = Frame(root, width = 1366, height = 768)
mainframe.pack()
canvas = Canvas(mainframe, background="white", width=str(xvmax), height=str(yvmax))
canvas.pack()

def windowToViewport(x, y, xv, yv):
    xv = xvmin + (round(x - xwmin) * xvmax - xvmin) / (xwmax - xwmin)
    yv = yvmax - (round(y - ywmin) * yvmax - yvmin) / (ywmax - ywmin)

def viewportToWindow(x, y, xw, yw):
    xw = xwmin + (x - xvmin) * (xwmax - xwmin) / (xvmax - xvmin)
    yw = ywmin + (yvmax - y) * (ywmax - ywmin) / (yvmax - yvmin)

xv, yv, xw, yw = 0, 0, 0, 0

alpha = 5
beta = -50
gama =  40  # not to be confused with gamma()

a, b, c, d, e, f = [], [], [], [], [], []
a.append(0)
b.append(0)
c.append(0)
d.append(0.37)
e.append(0)
f.append(0)

a.append( 0.65 * cos(alpha * pi / 180))
b.append(-0.65 * sin(alpha * pi / 180))
c.append( 0.65 * sin(alpha * pi / 180))
d.append(-0.65 * cos(alpha * pi / 180))
e.append(0)
f.append(2.5)

a.append( 0.5 * cos(beta * pi / 180))
b.append(-0.5 * sin(beta * pi / 180))
c.append( 0.5 * sin(beta * pi / 180))
d.append(-0.5 * cos(beta * pi / 180))
e.append(0)
f.append(1.5)

a.append( 0.5 * cos(gama * pi / 180))
b.append(-0.5 * sin(gama * pi / 180))
c.append( 0.5 * sin(gama * pi / 180))
d.append(-0.5 * cos(gama * pi / 180))
e.append(0)
f.append(1.7)

def start():
    # canvas.create_oval(100,100,400,500, fill="black")
    iterationNumber = 5
    k = 0
    while k <= iterationNumber:
        # canvas.create_rectangle(0,0, xvmax-xvmin, yvmax-yvmin)
        for i in range(xvmin, xvmax):
            for j in range(yvmin, yvmax):
                """ for item in items:
                    if canvas.coords(item) == (i,j):
                        pass
                    else: """
                viewportToWindow(i,j,x,y)
                xb = a[0] * x + b[0] * y + e[0]
                yb = c[0] * x + d[0] * y + f[0]
                windowToViewport(xb, yb, xi, yi)
                new_item = canvas.create_oval(xi,yi,xi,yi+1, fill="brown")
                # items.append(new_item)
                xb = a[1] * x + b[1] * y + e[1]
                yb = c[1] * x + d[1] * y + f[1]
                windowToViewport(xb, yb, xi, yi)
                # if canvas.option_get
                # print(xb, yb, xi, yi)
                new_item = canvas.create_oval(xi, yi, xi, yi+1, fill="green")
                # items.append(new_item)
                xb = a[2] * x + b[2] * y + e[2]
                yb = c[2] * x + d[2] * y + f[2]
                windowToViewport(xb, yb, xi, yi)
                new_item = canvas.create_oval(xi, yi, xi, yi+1, fill="green")
                # items.append(new_item)
                xb = a[3] * x + b[3] * y + e[3]
                yb = c[3] * x + d[3] * y + f[3]
                windowToViewport(xb, yb, xi, yi)
                new_item = canvas.create_oval(xi, yi, xi, yi+1, fill="green")
                # items.append(new_item)
        k += 1
        root.update_idletasks()
        print(k)
        # print(k, xi, yi)


start()

root.mainloop()