from graphics import *

async def gambarGaris(x1, y1, x2, y2):
    if x2 < x1:
        if y1 < y2:
            currentposX = x1
            currentposY = y1
            gradient = (y2 - y1) / (x2 - x1)
            while currentposX != x2:
                canvas.create_line(currentposX, currentposY, currentposX-1, currentposY)
                currentposX = currentposX - 1
                currentposY = currentposY - gradient
                root.update_idletasks()
                await asyncio.sleep(0.01)
            return
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    currentposX = x1
    currentposY = y1
    gradient = (y2 - y1) / (x2 - x1)
    while currentposX != x2:
        canvas.create_line(currentposX, currentposY, currentposX+1, currentposY)
        currentposX = currentposX + 1
        currentposY = currentposY + gradient
        root.update_idletasks()
        await asyncio.sleep(0.01)
    return