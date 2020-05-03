#coding=utf8
import pygame
pygame.init()
screen=pygame.display.set_mode((640,640),0,32)
img=pygame.image.load("res/body.png")
imgrect=img.get_rect()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    imgrect=imgrect.move(5,5)
    screen.blit(img,imgrect)
    pygame.display.flip()
#移开和重绘，为什么老是想着替换？