from tkinter.messagebox import showinfo
from pygame.locals import *
import tkinter as tk
from random import *
import pygame
base = tk.Tk()
base.geometry('0x0')
base.resizable(False,False)
def gen_pipe(h):
    surf = pygame.Surface((64,h))
    surf.fill((61,145,64))
    rint = randint(100,h - 100)
    pygame.draw.rect(surf,(51,161,201),Rect((0,rint),(64,rint + 64)))
    return surf
def check(surf,r1):
    r1 = ((int(r1[0][0]),int(r1[0][1])),(int(r1[1][0]),int(r1[1][1])))
    for i in range(r1[0][0],r1[1][0]):
        for j in range(r1[0][1],r1[1][1]):
            if(surf.get_at((i,j)) != (51,161,201)):
                return True
    return False
def main():
    WIDTH,HEIGHT = 640,480
    scr = pygame.display.set_mode((WIDTH,HEIGHT))
    bird = pygame.image.load('bird.png')
    bird_y = WIDTH / 2
    pipe = gen_pipe(HEIGHT)
    pipe_x = int(WIDTH)
    score = 0
    while(1):
        if(pipe_x <= -pipe.get_width()):
            pipe = gen_pipe(HEIGHT)
            pipe_x = int(WIDTH)
            score += 1
        pipe_x -= 1
        bird_y += (1 / 3)
        pygame.display.update()
        scr.fill((51,161,201))
        scr.blit(pipe,(pipe_x,0))
        if (bird_y < 0 or bird_y > HEIGHT or check(scr, ((100, bird_y), (133, bird_y + 32)))):
            return score
        scr.blit(bird, (100, bird_y))
        for ev in pygame.event.get():
            if(ev.type == QUIT):
                exit()
            elif(ev.type == KEYDOWN and ev.key == K_SPACE):
                bird_y -= 70
if(__name__ == '__main__'):
    while(1):
        s = main()
        showinfo('GAMEOVER!','GAMEOVER!score:%s'%s)
