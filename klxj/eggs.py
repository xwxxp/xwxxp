#coding=utf8
import pygame
class egg():
    def __init__(self,postion):
        self.egg_img=pygame.image.load("res/color_egg3.png")
        self.egg_img_rect=self.egg_img.get_rect()
        self.egg_img_rect.x,self.egg_img_rect.y,=postion
        