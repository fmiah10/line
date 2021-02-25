from display import DEFAULT_COLOR, new_screen, plot, save_ppm, save_extension, display
from math import inf

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 > x1:
        tempX = x0
        x0 = x1
        x1 = tempX
        tempY = y0
        y0 = y1
        y1 = tempY
    x = x0
    y = y0
    deltaY = y1-y0
    deltaX = x1-x0
    if deltaX == 0:
        while y <= y1:
            plot(screen, color, x, y)
            y+=1
    else:
        m = deltaY / deltaX
        A = deltaY
        B = -1 * deltaX
        #octants 1 and 5
        if 0 <= m <= 1:
            d = 2*A + B
            while x <= x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+=1
                    d += 2*B
                x+=1
                d += 2*A
        #octants 2 and 6
        elif 1 < m < inf:
            d = A + 2*B
            while y <= y1:
                plot(screen, color, x, y)
                if d < 0:
                    x+=1
                    d += 2*A
                y+=1
                d += 2*B
        #octants 7 and 3
        elif -inf < m <= -1:
            d = A - 2*B
            while y >= y1:
                plot(screen, color, x, y)
                if d > 0:
                    x+=1
                    d += 2*A
                y-=1
                d -= 2*B
        #octants 8 and 4
        elif -1 < m < 0:
            d = 2*A - B
            while x <= x1:
                plot(screen, color, x, y)
                if d < 0:
                    y-=1
                    d -= 2*B
                x+=1
                d += 2*A
