#################################
### Dependency : Python 3 (3.6.x and up) ####
####### Required Library : Tkinter ########
##### Created by Rian Wardana 18552 #####
#################################

## ! Important => Jalankan dengan command " python <nama_file_ini.py> "
## ! Important => Atau " python3 <nama_file_ini.py> " jika terjadi error syntaxfrom tkinter import *

from tkinter import *
from tkinter import ttk
import math as m

# Deklarasi jendela utama
root = Tk()
root.title("Grafkom Rian Wardana 800x600")

# Deklarasi variabel yang digunakan
ax = StringVar()
ay = StringVar()
bx = StringVar()
by = StringVar()
cx = StringVar()
cy = StringVar()

L1x = IntVar()
L1y = IntVar()
L2x = IntVar()
L2y = IntVar()

Ax = 0
Ay = 0
Bx = 0
By = 0
Cx = 0
Cy = 0

triangle = []
INSIDE = 0
LEFT = 1
RIGHT = 2
TOP = 8
BOT = 4

# Deklarasi ukuran window untuk clip
xmin, xmax, ymin, ymax = 100, 700, 100, 500


# Mengecek apakah garis ada di luar atau di dalam region clip
def compute(x, y):
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


# Menghitung garis yang akan digambar dalam region clip
def cohenSutherlandClip(x1, y1, x2, y2):

    # Menghitung masing-masing endpoints
    code1 = compute(x1, y1)
    code2 = compute(x2, y2)
    accept = False

    while True:

        # Jika kedua ujung titik = 0, garis diterima
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # Jika keduanya tidak masuk, maka garis tidak diterima
        elif (code1 & code2) != 0:
            break

        # hitungan dilakukan jika salah satu titik diluar dan sisanya di dalam
        else:
            x = 1.0
            y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax
            elif code_out & BOT:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute(x2, y2)

    if accept:
        canvas.create_line(x1, y1, x2, y2)


# Menghitung titik jarak X pada segitiga dan garis refleksi
def __distance_x(x, y, A, B, C):
    distance = A * x + B * y + C
    return (x - 2 * A * distance)


# Menghitung titik jarak Y pada segitiga dan garis refleksi
def __distance_y(x, y, A, B, C):
    distance = A * x + B * y + C
    return (y - 2 * B * distance)


# Menggambar segitiga dari 3 point yang diberikan
def draw(Ax, Ay, Bx, By, Cx, Cy):
    triangle.append([Ax, Ay, Bx, By, Cx, Cy])
    canvas.create_polygon([Ax, Ay, Bx, By, Cx, Cy],
                          outline="blue",
                          fill="cyan",
                          width=3)


""" def drawSimple(i):
    triangle.append(i)
    canvas.create_polygon(i, outline="blue", fill="cyan", width=3) """


# Fungsi untuk handler mouse klik tahan
def __reflection_start(event):
    global L1x, L1y
    L1x = event.x
    L1y = event.y


# Fungsi untuk menghitung refleksi dan menggambarnya dari mouse hingga jadi segitiga
def __draw_reflection(event):
    global L1x, L1y, L2x, L2y
    global Ax, Ay, Bx, By, Cx, Cy
    L2x, L2y = event.x, event.y
    canvas.create_line(L1x, L1y, L2x, L2y)

    A = L2y - L1y
    B = -(L2x - L1x)
    C = -A * L1x - B * L1y
    M = m.sqrt(A * A + B * B)
    Aa = A / M
    Ba = B / M
    Ca = C / M

    Dx = __distance_x(Ax, Ay, Aa, Ba, Ca)
    Ex = __distance_x(Bx, By, Aa, Ba, Ca)
    Fx = __distance_x(Cx, Cy, Aa, Ba, Ca)

    Dy = __distance_y(Ax, Ay, Aa, Ba, Ca)
    Ey = __distance_y(Bx, By, Aa, Ba, Ca)
    Fy = __distance_y(Cx, Cy, Aa, Ba, Ca)

    draw(Dx, Dy, Ex, Ey, Fx, Fy)


# Mengambil input dari tempat di GUI
def __start():
    global Ax, Ay, Bx, By, Cx, Cy
    clear()
    Ax = int(ax.get())
    Ay = int(ay.get())
    Bx = int(bx.get())
    By = int(by.get())
    Cx = int(cx.get())
    Cy = int(cy.get())
    draw(Ax, Ay, Bx, By, Cx, Cy)


# Membersihkan layar canvas
def clear():
    triangle.clear()
    canvas.delete(ALL)
    draw_rect()


# Membuat batas clipping
def draw_rect():
    canvas.create_polygon(100,100,700,100,700,500,100,500,  \
        fill='white', outline='black', dash=(5,2))

# Program untuk memulai clipping
def __clip():
    canvas.delete(ALL)
    draw_rect()
    cohenSutherlandClip(L1x, L1y, L2x, L2y)
    for i in triangle:
        cohenSutherlandClip(i[0], i[1], i[2], i[3])
        cohenSutherlandClip(i[0], i[1], i[4], i[5])
        cohenSutherlandClip(i[2], i[3], i[4], i[5])


# Deklarasi komponen GUI dan mouse event reader
mainframe = Frame(root, width=1000, height=600)
mainframe.grid(column=0, row=0, sticky=N + W)
canvas = Canvas(root, background="white", width=800, height=600)
canvas.grid(column=2, row=0)
root.columnconfigure(0, weight=1)
canvas.bind("<ButtonPress-1>", __reflection_start)
canvas.bind("<ButtonRelease-1>", __draw_reflection)

enterax = ttk.Entry(mainframe, width=10, textvariable=ax)
enteray = ttk.Entry(mainframe, width=10, textvariable=ay)
enterbx = ttk.Entry(mainframe, width=10, textvariable=bx)
enterby = ttk.Entry(mainframe, width=10, textvariable=by)
entercx = ttk.Entry(mainframe, width=10, textvariable=cx)
entercy = ttk.Entry(mainframe, width=10, textvariable=cy)
enterax.focus()

enterax.grid(column=1, row=1 + 2, sticky=N + W)
enteray.grid(column=1, row=2 + 2, sticky=N + W)
enterbx.grid(column=1, row=3 + 2, sticky=N + W)
enterby.grid(column=1, row=4 + 2, sticky=N + W)
entercx.grid(column=1, row=5 + 2, sticky=N + W)
entercy.grid(column=1, row=6 + 2, sticky=N + W)

ttk.Label(mainframe,
          text="Input points of triangle into the labels").grid(row=0)
ttk.Label(mainframe, text="Click and drag to draw mirror line").grid(row=1)
ttk.Label(mainframe, text="Input Point Ax: ").grid(column=0,
                                                   row=1 + 2,
                                                   sticky=N + W)
ttk.Label(mainframe, text="Input Point Ay: ").grid(column=0,
                                                   row=2 + 2,
                                                   sticky=N + W)
ttk.Label(mainframe, text="Input Point Bx: ").grid(column=0,
                                                   row=3 + 2,
                                                   sticky=N + W)
ttk.Label(mainframe, text="Input Point By: ").grid(column=0,
                                                   row=4 + 2,
                                                   sticky=N + W)
ttk.Label(mainframe, text="Input Point Cx: ").grid(column=0,
                                                   row=5 + 2,
                                                   sticky=N + W)
ttk.Label(mainframe, text="Input Point Cy: ").grid(column=0,
                                                   row=6 + 2,
                                                   sticky=N + W)
# root.bind("<Return>", __start())
button = ttk.Button(mainframe, text="Go!", command=__start).grid(column=0,
                                                                 row=9,
                                                                 sticky=N + W)
clear_button = ttk.Button(mainframe, text="Clear!",
                          command=clear).grid(column=1, row=9)
clipButton = ttk.Button(mainframe, text="Clip!",
                        command=__clip).grid(column=0, row=10, sticky=N + W)
root.pack_slaves()
draw_rect()

root.mainloop()
