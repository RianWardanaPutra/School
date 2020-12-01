#!/usr/bin/env python

# TUGAS 5 GRAFIKA KOMPUTER AFFINE TREE
# REQUIRED LIBRARY: tkinter, math, PIL
# BY: RIAN WARDANA

# Import library yang dibutuhkan
import tkinter as tk
import math as mt
from PIL import Image, ImageTk

# Menentukan sudut dan arah gambar
alpha = 5
beta = -50
gama = 40

# Batas-batas window dan viewport
xwmin = -3; xwmax = 3
ywmin =  0; ywmax = 7

xvmin = 0; xvmax = 600
yvmin = 0; yvmax = 700

# Variabel bebas yang dibutuhkan
x, y, xi, yi = 0, 0, 0, 0

# Fungsi transformasi window dan viewport
def windowToView(xw, yw):
    xv = xvmin + round((xw - xwmin) / (xwmax - xwmin) * (xvmax - xvmin))
    yv = yvmax - round((yw - ywmin) / (ywmax - ywmin) * (yvmax - yvmin))
    return (xv, yv)

def viewToWindow(xv, yv):
    xw = xwmin + (xv - xwmin) * (xwmax - xwmin) / (xvmax - xvmin)
    yw = ywmin + (yvmax - yv) * (ywmax - ywmin) / (yvmax - yvmin)
    return (xw, yw)


# Pendekatan program dengan OOP
class FractalTree(tk.Tk):
    
    # Constructor
    def __init__(self):
        super().__init__()
        self.title("Tugas 5 Rian Wardana")

        # Variabel pembentuk affine image
        self.a = [0] * 4
        self.b = [0] * 4
        self.c = [0] * 4
        self.d = [0] * 4
        self.e = [0] * 4
        self.f = [0] * 4

        self.a[0] = 0
        self.b[0] = 0
        self.c[0] = 0
        self.d[0] = 0.37
        self.e[0] = 0
        self.f[0] = 0

        self.a[1] =  0.65 * mt.cos(alpha * mt.pi / 180)
        self.b[1] = -0.65 * mt.sin(alpha * mt.pi / 180)
        self.c[1] =  0.65 * mt.sin(alpha * mt.pi / 180)
        self.d[1] =  0.65 * mt.cos(alpha * mt.pi / 180)
        self.e[1] =  0
        self.f[1] =  2.5

        self.a[2] =  0.5 * mt.cos(beta * mt.pi / 180)
        self.b[2] = -0.5 * mt.sin(beta * mt.pi / 180)
        self.c[2] =  0.5 * mt.sin(beta * mt.pi / 180)
        self.d[2] =  0.5 * mt.cos(beta * mt.pi / 180)
        self.e[2] =  0 
        self.f[2] =  1.5 

        self.a[3] =  0.5 * mt.cos(gama * mt.pi / 180)
        self.b[3] = -0.5 * mt.sin(gama * mt.pi / 180)
        self.c[3] =  0.5 * mt.sin(gama * mt.pi / 180)
        self.d[3] =  0.5 * mt.cos(gama * mt.pi / 180)
        self.e[3] =  0
        self.f[3] =  1.7

        # Membentuk bitmap object
        self.bm = Image.new("RGB", ((xvmax-xvmin),(yvmax-yvmin)), color="white")
        self.pixels = self.bm.load()

        # Memanggil fungsi untuk manipulasi pixel dalam bitmap
        self.treeDraw()
        self.pohon.pack()

    def treeDraw(self):

        # Membentuk garis awal
        # Garis ini yang nantinya akan jadi basis
        # untuk membuat tree
        xline = (xvmax-1)/2
        yline = yvmax-1
        for i in range(200):
            self.pixels[xline, yline-i] = (128,128,0)
        
        iteration = 7
        k = 0

        # Rumus untuk membangun self affinity tree
        while k <= iteration:
            for i in range(xvmax-1):
                for j in range(yvmax-1):
                    if self.pixels[i,j] != (255,255,255):
                        x, y = viewToWindow(i,j)
                        xb = self.a[0] * x + self.b[0] * y + self.e[0]
                        yb = self.c[0] * x + self.d[0] * y + self.f[0]
                        xi, yi = windowToView(xb, yb)
                        # print(xi,yi)
                        self.pixels[xi,yi] = (128,128,0)

                        xb = self.a[1] * x + self.b[1] * y + self.e[1]
                        yb = self.c[1] * x + self.d[1] * y + self.f[1]
                        xi, yi = windowToView(xb, yb)
                        self.pixels[xi,yi] = (0,255,0)

                        xb = self.a[2] * x + self.b[2] * y + self.e[2]
                        yb = self.c[2] * x + self.d[2] * y + self.f[2]
                        xi, yi = windowToView(xb, yb)
                        self.pixels[xi,yi] = (0,255,0)

                        xb = self.a[3] * x + self.b[3] * y + self.e[3]
                        yb = self.c[3] * x + self.d[3] * y + self.f[3]
                        xi, yi = windowToView(xb, yb)
                        self.pixels[xi,yi] = (0,255,0)

            k += 1

        # Membentuk gambar dari bitmap, 
        # dan dijadikan objek agar dapat ditampilkan
        self.img = ImageTk.PhotoImage(image=self.bm)
        self.pohon = tk.Label(self, image=self.img)
        # self.bm.show()
        

# Fungsi untuk memanggil objek
# sekaligus menjalankan program
if __name__ == "__main__":
    app = FractalTree()
    app.mainloop()
