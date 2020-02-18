#########################
### Fransiskus Rian Wardana Putra ###
##### 18/427592/PA/18552 #######
#########################

from graphics import GraphWin, Point, Line, Text, update

# from TEXT import *


# Rumus transformasi x
def transformX(Xw):
    return int((Xw - Xwmin) / (Xwmax - Xwmin) * (Xvmax - Xvmin) + Xvmin)


# Rumus transformasi y
def transformY(Yw):
    return int(Yvmax - ((Yw - Ywmin) / (Ywmax - Ywmin) * (Yvmax - Yvmin)))


Xwmin = -4
Xwmax = 4
Ywmax = 6
Ywmin = -2

Xvmin = 0
Xvmax = int(input("Masukkan lebar layar : "))
Yvmax = int(input("Masukkan tinggi layar : "))
Yvmin = 0

# window with title and size
win = GraphWin("Rian Wardana - 18/427592/PA/18552",
               Xvmax,
               Yvmax,
               autoflush=False)

#garis koordinat
p1 = Point(transformX(-3), transformY(0))
p2 = Point(transformX(3), transformY(0))
line = Line(p1, p2)
line.draw(win)
p1 = Point(transformX(0), transformY(5))
p2 = Point(transformX(0), transformY(-1))
line = Line(p1, p2)
line.draw(win)

#angka di koordinat
i = -3
while i <= 3:
    if i != 0:
        p1 = Point(transformX(i), transformY(-0.1))
        teks = Text(p1, i)
        teks.draw(win)
    i = i + 1

i = -1
while i <= 5:
    if i != 0:
        p1 = Point(transformX(0.05), transformY(i))
        teks = Text(p1, i)
        teks.draw(win)
    i = i + 1

#grafik
x = float(-2)
while x <= 2:
    nx = x
    ny = x**2
    point = Point(transformX(nx), transformY(ny))
    point.draw(win)
    update(2000)
    x = x + 0.001

win.getMouse()
win.close()
