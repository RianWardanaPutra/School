xmin, ymin, xmax, ymax = 100, 100, 1000, 800
    
# Bit code (0001, 0010, 0100, 1000 and 0000)
LEFT, RIGHT, BOT, TOP = 1, 2, 4, 8
INSIDE = 0

print(f"Xmin: {xmin}\nYmin: {ymin}\nXmax: {xmax}\nYmax: {ymax}")

x1 = float(input("Enter x: "))
y1 = float(input("Enter y: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Compute code, doing OR operation according
# the position of x,y
def computeCode(x, y):
    code = INSIDE
    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT
    if y < ymin:
        code |= BOT
    elif y > ymax:
        code |= TOP

    return code

# Clipping line process
def cohenSuthClip(x1, y1, x2, y2):

    # Compute region code
    code1 = computeCode(x1, y1)
    code2 = computeCode(x2, y2)
    accept = False

    while True:

        # If both endpoints lie within clip bounds
        if code1 == 0 and code2 == 0:
            accept = True
            break
        
        # If both endpoints are outside clip bounds
        elif (code1 & code2) != 0:
            break

        # Some inside and some outside
        else:

            # Clip process needed
            # At least one point is outside clip
            x = 1.
            y = 1.
            code_out = code1 if code1 != 0 else code2

            # Find intersection point
            # F(y) => y = y1 + slope * (x - x1),
            # F(x) => x = x1 + (1 / slope) * (y - y1)
            if code_out & TOP:

                # point is above xmax
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            elif code_out & BOT:
                 
                # point is below clip
                x = x1 + (x2 - x1) * (ymin - y1) / (x2 - x1)
                y = ymin

            elif code_out & LEFT:

                # point is to the left of the clip
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            elif code_out & RIGHT:

                # point is to the right of the clip
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax
            
            # intersection point x,y is set now
            # replace point outside clipping bounds
            # by recently found intersection point
            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1)
            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2)

    if accept:
        print(f"Line accepted from {x1}, {y1}, {x2}, {y2}")

    else:
        print("Line rejected")

cohenSuthClip(x1, y1, x2, y2)

