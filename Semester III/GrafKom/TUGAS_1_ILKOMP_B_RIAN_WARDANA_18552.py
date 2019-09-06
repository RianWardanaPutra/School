##########################################
## Dependency : Python 3 (3.6.x and up) ##
####### Required Library : Tkinter #######
###### Created by Rian Wardana 18552 #####
##########################################

from tkinter import *
from tkinter import ttk
import math as mt
import asyncio

# Induk window kita
root = Tk()
root.title("Grafkom Rian Wardana 800x800")

# Variable buat input
tx1 = StringVar()
ty1 = StringVar()
tx2 = StringVar()
ty2 = StringVar()
tr = StringVar()

# Menggambar lingkaran dengan penuh cinta
# Dengan menggunakan algoritma DDA
# Diberikan 4 cara untuk tiap kemungkinan kasus
# Arah gerakan
async def gambarLingkaran1(centerx, centery, r, deg):
    k = 0
    while k < (2*mt.pi*r):
        x = centerx+round(r*mt.cos(deg))
        y = centery+round(r*mt.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg+1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

async def gambarLingkaran2(centerx, centery, r, deg):
    k = 0
    while k < (2*mt.pi*r):
        x = centerx+round(r*mt.cos(deg))
        y = centery+round(r*mt.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg-1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

async def gambarLingkaran3(centerx, centery, r, deg):
    k = 0
    while k < (2*mt.pi*r):
        x = centerx+round(r*mt.cos(deg))
        y = centery+round(r*mt.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg-1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

async def gambarLingkaran4(centerx, centery, r, deg):
    k = 0
    while k < (2*mt.pi*r):
        x = centerx+round(r*mt.cos(deg))
        y = centery+round(r*mt.sin(deg))
        canvas.create_line(x,y,x+1,y)
        deg = deg+1/r
        root.update_idletasks()
        k = k + 1
        await asyncio.sleep(0.01)
    return

# Menggambar garis dengan penuh kasih sayang
# Juga menggunakan algoritma DDA
async def gambarGaris(x1, y1, dx, dy):
    x = x1
    y = y1
    k = 0
    if(abs(dx) > abs(dy)):
        steps = int(round(abs(dx)))
    else:
        steps = int(round(abs(dy)))
    
    xrun = dx/steps
    yrun = dy/steps
    canvas.create_line(x, y, x+1, y)
    while k < steps:
        x = x + xrun
        y = y + yrun
        k = k + 1
        canvas.create_line(x, y, x+1, y)
        root.update_idletasks()
        await asyncio.sleep(0.01)


# Tempat semua pergambaran dimulai, menentukan variable untuk dipanggil
# ke fungsi penggambar
async def mulai_gambar(*args):
    x1 = float(tx1.get())
    y1 = float(ty1.get())
    x2 = float(tx2.get())
    y2 = float(ty2.get())
    r = float(tr.get())

    gradient = (x2-x1)/(y2-y1)*-1
    k = mt.sqrt((r**2)/(1+gradient**2))
    k = k * -1
    dx = x2 - x1
    dy = y2 - y1
    circleCenter1x = x1 + k
    circleCenter1y = y1 + k * gradient
    k = k * -1
    circleCenter2x = x2 + k
    circleCenter2y = y2 + k * gradient
    degree = abs(mt.acos(abs(k)/r)) * -1
    canvas.delete("all")                    # <-- Membersihkan canvas setiap penghitungan baru
    
    
    # Pemanggilan fungsi tergantung kejadian 
    # agar gambar yang dihasilkan sesuai
    if x1<x2 and y1<y2:
        degree = abs(mt.acos(abs(k)/r)) * -1
        await gambarLingkaran1(circleCenter1x, circleCenter1y, r, degree)
        await gambarGaris(x1, y1, dx, dy)
        await gambarLingkaran2(circleCenter2x, circleCenter2y, r, degree + mt.pi)
    elif x1>x2 and y1>y2:
        degree = abs(mt.acos(abs(k)/r)) * -1
        await gambarLingkaran3(circleCenter1x, circleCenter1y, r, degree)
        await gambarGaris(x1, y1, dx, dy)
        await gambarLingkaran4(circleCenter2x, circleCenter2y, r, degree + mt.pi)
    elif x1<x2 and y1>y2:
        degree = abs(mt.acos(abs(k)/r)) * 1
        await gambarLingkaran3(circleCenter1x, circleCenter1y, r, degree)
        await gambarGaris(x1, y1, dx, dy)
        await gambarLingkaran4(circleCenter2x, circleCenter2y, r, degree + mt.pi)
    elif x1>x2 and y1<y2:
        degree = abs(mt.acos(abs(k)/r)) * 1
        await gambarLingkaran1(circleCenter1x, circleCenter1y, r, degree)
        await gambarGaris(x1, y1, dx, dy)
        await gambarLingkaran2(circleCenter2x, circleCenter2y, r, degree + mt.pi)


# Fungsi yang bisa dimasukkan ke tombol, tempat semua bermula
def do_task():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(mulai_gambar())
    finally:
        #loop.close()
        pass
        
# Tempat kita menggambar bentuk-bentuk yang indah (lingkaran dan garis)
canvas = Canvas(root, background="white", width=800, height=800)
canvas.grid(column=2, row=0)
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W))
root.columnconfigure(0, weight=1)
# root.rowconfigure(050, weight=1)


# Attributes yang dipasang di GUI, biar mudah inputnya.
# Kalau pakai ini kan kita jadi tidak ngetik di console :D
entryx1 = ttk.Entry(mainframe, width=10, textvariable=tx1)
entryy1 = ttk.Entry(mainframe, width=10, textvariable=ty1)
entryx2 = ttk.Entry(mainframe, width=10, textvariable=tx2)
entryy2 = ttk.Entry(mainframe, width=10, textvariable=ty2)
entryr = ttk.Entry(mainframe, width=10, textvariable=tr)
entryx1.focus()
entryx1.grid(column=1, row=1, sticky=N + W)
entryy1.grid(column=1, row=2, sticky=N + W)
entryx2.grid(column=1, row=3, sticky=N + W)
entryy2.grid(column=1, row=4, sticky=N + W)
entryr.grid(column=1, row=5, sticky=N + W)
ttk.Label(mainframe, text="Input X1:").grid(column=0, row=1, sticky=(N, W))
ttk.Label(mainframe, text="Input Y1:").grid(column=0, row=2, sticky=(N, W))
ttk.Label(mainframe, text="Input X2:").grid(column=0, row=3, sticky=N + W)
ttk.Label(mainframe, text="Input Y2:").grid(column=0, row=4, sticky=N + W)
ttk.Label(mainframe, text="Input R:").grid(column=0, row=5, sticky=N + W)

# Tombol sakti (untuk memulai gambar) :))
startButton = ttk.Button(mainframe, text="Start", command=do_task)
startButton.grid(column=1, row=6, sticky=N + W)

# Fungsi untuk menampilkan GUI kitaa
root.mainloop()