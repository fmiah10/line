from display import new_screen, plot, display, save_ppm, save_ppm_ascii, save_extension
from draw import draw_line

s = new_screen()
brickLines = [248, 248, 255]
brick = [155, 28, 49]

for i in range(500):
    for j in range(500):
        plot(s, brick, i,j)

for i in range(500):
    if (i % 40 == 0):
        draw_line(0, i, 499, i, s, brickLines)
        draw_line(0, i+1, 499, i+1, s, brickLines)
    if (i % 40 == 0 and i % 80 != 0):
        for j in range(500):
            if (j % 80 == 0):
                draw_line(j, i, j, i+40, s, brickLines)
                draw_line(j+1, i, j+1, i+40, s, brickLines)
    elif (i % 40 == 0 and i % 80 == 0):
        for j in range(500):
            if (j % 40 == 0 and j % 80 != 0):
                draw_line(j, i, j, i+40, s, brickLines)
                draw_line(j+1, i, j+1, i+40, s, brickLines)

display(s)
save_ppm(s, 'binary.ppm')
save_ppm_ascii(s, 'ascii.ppm')
save_extension(s, 'img.png')
