from pygame import *
w=900
h=400
win = display.set_mode((w,h))

while True:
    
    for e in event.get():
        if e.type == 12:
            exit()


    win.fill((255,255,255))
    display.update()