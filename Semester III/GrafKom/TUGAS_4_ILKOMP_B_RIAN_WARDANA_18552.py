from tkinter import *
from tkinter import ttk
import math as m

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self):
        return self.x, self.y

    def setPoint(self, x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    

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

A = Point(0, 0)
B = Point(0,0)
C = Point(0,0)

triangle_counts=0
triangle=[]
poly=[]

# Menghitung titik jarak X pada segitiga dan garis refleksi
def __distance(xy, A, B, C):
    distance = A * xy.getX() + B * xy.getY() + C
    return Point((xy.getX()-2*A*distance), (xy.getY()-2*B*distance))

# Menggambar segitiga dari 3 point yang diberikan
def draw(A, B, C):
    global triangle, triangle_counts
    triangle.append([A.getPoint(), B.getPoint(), C.getPoint()])
    canvas.create_polygon([A.getPoint(), B.getPoint(), C.getPoint()], outline="blue", fill="cyan", width=3)
    triangle_counts+=1

# Fungsi untuk handler mouse klik tahan
def __reflection_start(event):
    global L1x, L1y
    L1x = event.x
    L1y = event.y

# Fungsi untuk menghitung refleksi dan menggambarnya dari mouse hingga jadi segitiga
def __draw_reflection(event):
    global L1x, L1y, L2x, L2y
    global A, B, C
    L2x, L2y = event.x, event.y
    canvas.create_line(L1x, L1y, L2x, L2y)
    
    a = L2y - L1y
    b = -(L2x - L1x)
    c = -a * L1x - b * L1y
    M = m.sqrt(a*a + b*b)
    Aa = a/M
    Ba = b/M
    Ca = c/M

    D = __distance(A, Aa, Ba, Ca)
    E = __distance(B, Aa, Ba, Ca)
    F = __distance(C, Aa, Ba, Ca)

    draw(D, E, F)
    
# Membuat batas clipping
def draw_rect():
    global poly
    canvas.create_polygon(100,100,700,100,700,500,100,500, fill='white', outline='black', dash=(5,
        2))
    poly.append([100,100,700,100,700,500,100,500])

# Membersihkan layar canvas
def clear():
    global triangle, triangle_counts, poly
    poly=[]
    triangle=[]
    triangle_counts=0
    canvas.delete(ALL)

# Mengambil input dari tempat di GUI
def __start():
    global A, B, C
    clear()
    draw_rect()
    A = Point(int(ax.get()), int(ay.get()))
    B = Point(int(bx.get()), int(by.get()))
    C = Point(int(cx.get()), int(cy.get()))
    draw(A, B, C)

def clip():
    global triangle, triangle_counts, poly
    for i in poly:
        for x1,y1,x2,y2 in zip(i[::2], i[1::2], i[2::2], i[3::2]):
            print(x1,y1,x2,y2)
#    for i in triangle:

def __log():
    global triangle, triangle_counts, poly
    for i in triangle:
        print(i)
    print(triangle_counts)
    for i in poly:
        print(i)

# Deklarasi komponen GUI dan mouse event reader
mainframe = Frame(root, width=1000, height=600)
mainframe.grid(column=0, row=0, sticky=N+W)
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

enterax.grid(column=1, row=1, sticky=N+W)
enteray.grid(column=1, row=2, sticky=N+W)
enterbx.grid(column=1, row=3, sticky=N+W)
enterby.grid(column=1, row=4, sticky=N+W)
entercx.grid(column=1, row=5, sticky=N+W)
entercy.grid(column=1, row=6, sticky=N+W)

ttk.Label(mainframe, text="Input Point Ax: ").grid(column=0, row=1, sticky=N+W)
ttk.Label(mainframe, text="Input Point Ay: ").grid(column=0, row=2, sticky=N+W)
ttk.Label(mainframe, text="Input Point Bx: ").grid(column=0, row=3, sticky=N+W)
ttk.Label(mainframe, text="Input Point By: ").grid(column=0, row=4, sticky=N+W)
ttk.Label(mainframe, text="Input Point Cx: ").grid(column=0, row=5, sticky=N+W)
ttk.Label(mainframe, text="Input Point Cy: ").grid(column=0, row=6, sticky=N+W)
# root.bind("<Return>", __start())
button = ttk.Button(mainframe, text="Go!", command=__start).grid(column=0, row=7, sticky=N+W)
clear_button = ttk.Button(mainframe, text="Clear!", command=clear).grid(column=1, row=7)
clip_button = ttk.Button(mainframe, text="Clip!", command=clip).grid(column=1, row=8)
log_button = ttk.Button(mainframe, text="log", command=__log).grid(column=0, row=8)
root.pack_slaves()
draw_rect()



root.mainloop()
