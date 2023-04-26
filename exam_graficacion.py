Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
... def punto_medio(xc, yc, r, partes):
...     x = r
...     y = 0
...     dx = r / partes
...     dy = dx
... 
...     plt.plot(x + xc, y + yc, 'bo')
...     for i in range(partes):
...         y += dy
...         p = 1 - r
...         while x > y:
...             x -= dx
...             if p < 0:
...                 p += 2 * y + 1
...             else:
...                 y += dy
...                 p += 2 * (y - x) + 1
...             plt.plot(x + xc, y + yc, 'bo')
...             plt.plot(-x + xc, y + yc, 'bo')
...             plt.plot(x + xc, -y + yc, 'bo')
...             plt.plot(-x + xc, -y + yc, 'bo')
... 
...     plt.show()
... 
... 
... def DDA(xc, yc, r, partes):
...     theta = 360 / partes
...     for i in range(partes):
...         x1 = r * (2 ** (0.5) / 2) * (1 - abs(theta * i % 180 - 90) / 90)
...         y1 = r * (2 ** (0.5) / 2) * (1 - abs(theta * i % 180 - 90) / 90)
...         x2 = r * (2 * (0.5) / 2) * (1 - abs(theta(i + 1) % 180 - 90) / 90)
...         y2 = r * (2 * (0.5) / 2) * (1 - abs(theta(i + 1) % 180 - 90) / 90)
... 
...         if 90 <= theta * i % 360 <= 270:
...             x1 = -x1
...         if 90 <= theta * (i + 1) % 360 <= 270:
...             x2 = -x2
        if 0 <= theta * i % 360 <= 180:
            y1 = -y1
        if 0 <= theta * (i + 1) % 360 <= 180:
            y2 = -y2

        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        if abs(m) <= 1:
            x = min(x1, x2)
            while x <= max(x1, x2):
                y = m * x + b
                plt.plot(x + xc, y + yc, 'bo')
                x += 1
        else:
            y = min(y1, y2)
            while y <= max(y1, y2):
                x = (y - b) / m
                plt.plot(x + xc, y + yc, 'bo')
                y += 1

    plt.show()

def bresenham(xc, yc, r, partes):
    theta = 360 / partes
    for i in range(partes):
        x = 0
        y = r
        dx = 1
        dy = 2 * r
        d = 1 - r

        while x <= y:
            plt.plot(x + xc, y + yc, 'bo')
            plt.plot(-x + xc, y + yc, 'bo')
            plt.plot(x + xc, -y + yc, 'bo')
            plt.plot(-x + xc, -y + yc, 'bo')
            if d < 0:
                d += dx
                dx += 2
            else:
                d += dx + dy
                dx += 2
                dy += 2
                y -= 1
            x += 1

    plt.show()


xc1, yc1, r1 = 2, 2, 10
xc2, yc2, r2 = 18, 2, 10
xc3, yc3, r3 = 34, 2, 10

partes = 4

punto_medio(xc1, yc1, r1, partes)
DDA(xc2, yc2, r2, partes)
bresenham(xc3, yc3, r3, partes)
[DEBUG ON]
[DEBUG OFF]
[DEBUG ON]
[DEBUG OFF]
