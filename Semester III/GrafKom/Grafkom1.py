# from tkinter import Tk, ttk, BOTH, Canvas, Frame
from tkinter import *
from tkinter import ttk
import math as mt
import time, asyncio
from contextlib import suppress

root = Tk()
root.title("Grafkom Rian Wardana 600x600")


class Gui:
    def __init__(self):
        tx1 = StringVar()
        ty1 = StringVar()
        tx2 = StringVar()
        ty2 = StringVar()
        tr = StringVar()

        async def drawCircle(x, y, r, deg, canvas):
            startDegree = deg
            while deg < (2 * mt.pi + startDegree):
                deg = deg + 0.1
                canvas.create_arc(x, y, startDegree, deg)
                asyncio.sleep(0.1)

        async def _start(*args):
            x1 = int(tx1.get())
            x2 = int(tx2.get())
            y1 = int(ty1.get())
            y2 = int(ty2.get())
            r = int(tr.get())
            gradien = (x2 - x1) / (y2 - y1)
            k = mt.sqrt((r ** 2) / (1 + gradien ** 2))
            k = k * -1
            centerCircle1x = x1 + k
            centerCircle1y = y1 + k * gradien
            k = k * -1
            centerCircle2x = x2 + k
            centerCircle2y = y2 + k * gradien
            degree = abs(mt.acos(abs(k) / r))
            await drawCircle(centerCircle1x, centerCircle1y, r, -degree)

        async def start_loop():
            loop = asyncio.get_event_loop()
            futures = loop.create_future()
            futures.set_result(root)

        canvas = Canvas(root, background="white", width=600, height=600)
        canvas.grid(column=2, row=0)
        mainframe = Frame(root)
        mainframe.grid(column=0, row=0, sticky=(N, W))
        root.columnconfigure(0, weight=1)
        # root.rowconfigure(0, weight=1)
        startButton = ttk.Button(mainframe, text="Start", command=_start)
        entryx1 = ttk.Entry(mainframe, width=10, textvariable=tx1)
        entryy1 = ttk.Entry(mainframe, width=10, textvariable=ty1)
        entryx2 = ttk.Entry(mainframe, width=10, textvariable=tx2)
        entryy2 = ttk.Entry(mainframe, width=10, textvariable=ty2)
        entryr = ttk.Entry(mainframe, width=10, textvariable=tr)

        entryx1.focus()
        root.bind("<Return>", _start())

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
        startButton.grid(column=1, row=6, sticky=N + W)

        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(start_loop())
        except KeyboardInterrupt:
            for task in asyncio.Task.all_tasks():
                task.cancel()
                with suppress(asyncio.CancelledError):
                    loop.run_until_complete(task)
        finally:
            loop.stop()


gui = Gui()

""" loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(start_loop())
except KeyboardInterrupt:
        for task in asyncio.Task.all_tasks():
            task.cancel()
            with suppress(asyncio.CancelledError):
                loop.run_until_complete(task)
finally:
    loop.stop()
 """  # root.geometry("600x600+200+200")

# mainframe.pack()
root.mainloop()
