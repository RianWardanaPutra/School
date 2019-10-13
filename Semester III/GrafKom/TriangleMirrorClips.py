from graphics import *

win = GraphWin("TriangleMirror", 1200, 800)
GraphWin.setBackground(win, 'white')

instruction = Text(Point(350, 15), "")
instruction.setText(
    "Instruction: Click 3 times anywhere to make triangle, then click 2 times anywhere to make mirror line"
)
instruction.setFace("arial")
instruction.setSize(11)
instruction.setTextColor("black")
instruction.draw(win)

clips = Rectangle(Point(250, 150), Point(950, 550))
clips.draw(win)


#1=top,2=left,3=bottom,4=right
def checkPosition(x, y):
    if x < 250:
        return 2
    elif x > 950:
        return 4
    elif y < 150:
        return 1
    elif y > 550:
        return 3
    else:
        return 0


def clipPositionX(xIn, yIn, xOut, yOut, pos):
    if pos == 1:
        x = xIn + (xOut - xIn) * (150 - yIn) / (yOut - yIn)
        return x
    elif pos == 3:
        x = xIn + (xOut - xIn) * (550 - yIn) / (yOut - yIn)
        return x
    elif pos == 2:
        return 250
    elif pos == 4:
        return 950
    else:
        return xOut


def clipPositionY(xIn, yIn, xOut, yOut, pos):
    if pos == 2:
        y = yIn + (yOut - yIn) * (250 - xIn) / (xOut - xIn)
        return y
    elif pos == 4:
        y = yIn + (yOut - yIn) * (950 - xIn) / (xOut - xIn)
        return y
    elif pos == 1:
        return 150
    elif pos == 3:
        return 550
    else:
        return yOut


pointOut = 0
click1 = win.getMouse()
click1.draw(win)
x1 = int(click1.getX())
y1 = int(click1.getY())
if checkPosition(x1, y1) == 0:
    pointOut += 1

click2 = win.getMouse()
click2.draw(win)
x2 = int(click2.getX())
y2 = int(click2.getY())
if checkPosition(x2, y2) == 0:
    pointOut += 3

click3 = win.getMouse()
click3.draw(win)
x3 = int(click3.getX())
y3 = int(click3.getY())
if checkPosition(x3, y3) == 0:
    pointOut += 5

if pointOut == 9:
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    line1 = Line(p1, p2)
    line1.draw(win)
    line2 = Line(p2, p3)
    line2.draw(win)
    line3 = Line(p1, p3)
    line3.draw(win)
elif pointOut == 8:
    p2 = Point(x2, y2)
    p3 = Point(x3, y3)
    line2 = Line(p2, p3)
    line2.draw(win)
    pA = Point(clipPositionX(x2, y2, x1, y1, checkPosition(x1, y1)),
               clipPositionY(x2, y2, x1, y1, checkPosition(x1, y1)))
    line1 = Line(pA, p2)
    line1.draw(win)
    pB = Point(clipPositionX(x3, y3, x1, y1, checkPosition(x1, y1)),
               clipPositionY(x3, y3, x1, y1, checkPosition(x1, y1)))
    line3 = Line(pB, p3)
    line3.draw(win)
elif pointOut == 6:
    p1 = Point(x1, y1)
    p3 = Point(x3, y3)
    line3 = Line(p1, p3)
    line3.draw(win)
    pA = Point(clipPositionX(x1, y1, x2, y2, checkPosition(x2, y2)),
               clipPositionY(x1, y1, x2, y2, checkPosition(x2, y2)))
    line1 = Line(p1, pA)
    line1.draw(win)
    pB = Point(clipPositionX(x3, y3, x2, y2, checkPosition(x2, y2)),
               clipPositionY(x3, y3, x2, y2, checkPosition(x2, y2)))
    line2 = Line(pB, p3)
    line2.draw(win)
elif pointOut == 4:
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    line1 = Line(p1, p2)
    line1.draw(win)
    pA = Point(clipPositionX(x1, y1, x3, y3, checkPosition(x3, y3)),
               clipPositionY(x1, y1, x3, y3, checkPosition(x3, y3)))
    line3 = Line(p1, pA)
    line3.draw(win)
    pB = Point(clipPositionX(x2, y2, x3, y3, checkPosition(x3, y3)),
               clipPositionY(x2, y2, x3, y3, checkPosition(x3, y3)))
    line2 = Line(p2, pB)
    line2.draw(win)
elif pointOut == 5:
    p3 = Point(x3, y3)
    pA = Point(clipPositionX(x3, y3, x2, y2, checkPosition(x2, y2)),
               clipPositionY(x3, y3, x2, y2, checkPosition(x2, y2)))
    line2 = Line(pA, p3)
    line2.draw(win)
    pB = Point(clipPositionX(x3, y3, x1, y1, checkPosition(x1, y1)),
               clipPositionY(x3, y3, x1, y1, checkPosition(x1, y1)))
    line3 = Line(pB, p3)
    line3.draw(win)
elif pointOut == 3:
    p2 = Point(x2, y2)
    pA = Point(clipPositionX(x2, y2, x1, y1, checkPosition(x1, y1)),
               clipPositionY(x2, y2, x1, y1, checkPosition(x1, y1)))
    line1 = Line(pA, p2)
    line1.draw(win)
    pB = Point(clipPositionX(x2, y2, x3, y3, checkPosition(x3, y3)),
               clipPositionY(x2, y2, x3, y3, checkPosition(x3, y3)))
    line2 = Line(p2, pB)
    line2.draw(win)
elif pointOut == 1:
    p1 = Point(x1, y1)
    pA = Point(clipPositionX(x1, y1, x2, y2, checkPosition(x2, y2)),
               clipPositionY(x1, y1, x2, y2, checkPosition(x2, y2)))
    line1 = Line(p1, pA)
    line1.draw(win)
    pB = Point(clipPositionX(x1, y1, x3, y3, checkPosition(x3, y3)),
               clipPositionY(x1, y1, x3, y3, checkPosition(x3, y3)))
    line3 = Line(p1, pB)
    line3.draw(win)

pointOut = 0
click4 = win.getMouse()
click4.draw(win)
clickx4 = int(click4.getX())
clicky4 = int(click4.getY())
if checkPosition(clickx4, clicky4) == 0:
    pointOut += 1

click5 = win.getMouse()
click5.draw(win)
clickx5 = int(click5.getX())
clicky5 = int(click5.getY())
if checkPosition(clickx5, clicky5) == 0:
    pointOut += 3

if pointOut == 4:
    mirror = Line(click4, click5)
    mirror.draw(win)
elif pointOut == 3:
    pD = Point(
        clipPositionX(clickx5, clicky5, clickx4, clicky4,
                      checkPosition(clickx4, clicky4)),
        clipPositionY(clickx5, clicky5, clickx4, clicky4,
                      checkPosition(clickx4, clicky4)))
    mirror = Line(pD, click5)
    mirror.draw(win)
elif pointOut == 1:
    pD = Point(
        clipPositionX(clickx4, clicky4, clickx5, clicky5,
                      checkPosition(clickx5, clicky5)),
        clipPositionY(clickx4, clicky4, clickx5, clicky5,
                      checkPosition(clickx5, clicky5)))
    mirror = Line(click4, pD)
    mirror.draw(win)

sideA = clicky5 - clicky4
sideB = (clickx5 - clickx4) * -1
sideC = (-sideA * clickx4) - (sideB * clicky4)

mirrorDist = (sideA**2 + sideB**2)
side_A = sideA / (mirrorDist**0.5)
side_B = sideB / (mirrorDist**0.5)
side_C = sideC / (mirrorDist**0.5)


def distPoint(x, y, sideA, sideB, sideC):
    val = sideA * x + sideB * y + sideC
    return Point(x - 2 * sideA * val, y - 2 * sideB * val)


pointOut = 0
p_1 = distPoint(x1, y1, side_A, side_B, side_C)
if checkPosition(p_1.getX(), p_1.getY()) == 0:
    pointOut += 1
p_2 = distPoint(x2, y2, side_A, side_B, side_C)
if checkPosition(p_2.getX(), p_2.getY()) == 0:
    pointOut += 3
p_3 = distPoint(x3, y3, side_A, side_B, side_C)
if checkPosition(p_3.getX(), p_3.getY()) == 0:
    pointOut += 5

x4 = p_1.getX()
x5 = p_2.getX()
x6 = p_3.getX()
y4 = p_1.getY()
y5 = p_2.getY()
y6 = p_3.getY()

if pointOut == 9:
    line_1 = Line(p_1, p_2)
    line_1.draw(win)
    line_2 = Line(p_2, p_3)
    line_2.draw(win)
    line_3 = Line(p_1, p_3)
    line_3.draw(win)
elif pointOut == 8:
    line_2 = Line(p_2, p_3)
    line_2.draw(win)
    pA = Point(clipPositionX(x5, y5, x4, y4, checkPosition(x4, y4)),
               clipPositionY(x5, y5, x4, y4, checkPosition(x4, y4)))
    line_1 = Line(pA, p_2)
    line_1.draw(win)
    pB = Point(clipPositionX(x6, y6, x4, y4, checkPosition(x4, y4)),
               clipPositionY(x6, y6, x4, y4, checkPosition(x4, y4)))
    line_3 = Line(pB, p_3)
    line_3.draw(win)
elif pointOut == 6:
    line_3 = Line(p_1, p_3)
    line_3.draw(win)
    pA = Point(clipPositionX(x4, y4, x5, y5, checkPosition(x5, y5)),
               clipPositionY(x4, y4, x5, y5, checkPosition(x5, y5)))
    line_1 = Line(p_1, pA)
    line_1.draw(win)
    pB = Point(clipPositionX(x6, y6, x5, y5, checkPosition(x5, y5)),
               clipPositionY(x6, y6, x5, y5, checkPosition(x5, y5)))
    line_2 = Line(pB, p_3)
    line_2.draw(win)
elif pointOut == 4:
    line_1 = Line(p_1, p_2)
    line_1.draw(win)
    pA = Point(clipPositionX(x4, y4, x6, y6, checkPosition(x6, y6)),
               clipPositionY(x4, y4, x6, y6, checkPosition(x6, y6)))
    line_3 = Line(p_1, pA)
    line_3.draw(win)
    pB = Point(clipPositionX(x5, y5, x6, y6, checkPosition(x6, y6)),
               clipPositionY(x5, y5, x6, y6, checkPosition(x6, y6)))
    line_2 = Line(p_2, pB)
    line_2.draw(win)
elif pointOut == 5:
    pA = Point(clipPositionX(x6, y6, x5, y5, checkPosition(x5, y5)),
               clipPositionY(x6, y6, x5, y5, checkPosition(x5, y5)))
    line_2 = Line(pA, p_3)
    line_2.draw(win)
    pB = Point(clipPositionX(x6, y6, x4, y4, checkPosition(x4, y4)),
               clipPositionY(x6, y6, x4, y4, checkPosition(x4, y4)))
    line_3 = Line(pB, p_3)
    line_3.draw(win)
elif pointOut == 3:
    pA = Point(clipPositionX(x5, y5, x4, y4, checkPosition(x4, y4)),
               clipPositionY(x5, y5, x4, y4, checkPosition(x4, y4)))
    line_1 = Line(pA, p_2)
    line_1.draw(win)
    pB = Point(clipPositionX(x5, y5, x6, y6, checkPosition(x6, y6)),
               clipPositionY(x5, y5, x6, y6, checkPosition(x6, y6)))
    line_2 = Line(p_2, pB)
    line_2.draw(win)
elif pointOut == 1:
    pA = Point(clipPositionX(x4, y4, x5, y5, checkPosition(x5, y5)),
               clipPositionY(x4, y4, x5, y5, checkPosition(x5, y5)))
    line_1 = Line(p_1, pA)
    line_1.draw(win)
    pB = Point(clipPositionX(x4, y4, x6, y6, checkPosition(x6, y6)),
               clipPositionY(x4, y4, x6, y6, checkPosition(x6, y6)))
    line_3 = Line(p_1, pB)
    line_3.draw(win)

win.getMouse()
win.close()