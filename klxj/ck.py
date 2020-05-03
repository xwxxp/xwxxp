import pygame
#coding=utf8
class hen():
    def __init__(self):
        self.body=pygame.image.load("res/body.png").convert_alpha()
        self.mouth=pygame.image.load("res/mouth.png").convert_alpha()
        self.mouth_open=pygame.image.load("res/mouth_open.png").convert_alpha()
        self.foot1=pygame.image.load("res/foot.png").convert_alpha()
        self.foot2=pygame.image.load("res/foot.png").convert_alpha()
        self.feet_jump=pygame.image.load("res/feet_jump.png").convert_alpha()
        self.eye=pygame.image.load("res/eye.png").convert_alpha()
        self.eye_close=pygame.image.load("res/eye_close.png").convert_alpha()

        self.bodyRect=self.body.get_rect()
        self.mouthRect=self.mouth.get_rect()
        self.mouth_open_Rect=self.mouth_open.get_rect()
        self.footRect1=self.foot1.get_rect()
        self.footRect2=self.foot2.get_rect()
        self.feet_jump_Rect=self.feet_jump.get_rect()
        self.eyeRect=self.eye.get_rect()
        self.eye_close_Rect=self.eye_close.get_rect()

        self.bodyRect.x,self.bodyRect.y=600,300
        self.mouthRect.x,self.mouthRect.y=self.bodyRect.x-10,self.bodyRect.y+60
        self.mouth_open_Rect.x,self.mouth_open_Rect.y=self.bodyRect.x+50,self.bodyRect.y+50
        self.footRect1.x,self.footRect1.y=self.bodyRect.x+80,self.bodyRect.y+230
        self.footRect2.x,self.footRect2.y=self.bodyRect.x+150,self.bodyRect.y+230
        self.feet_jump_Rect.x,self.feet_jump_Rect.y=self.bodyRect.x+50,self.bodyRect.y+50
        self.eyeRect.x,self.eyeRect.y=self.bodyRect.x+90,self.bodyRect.y+90
        self.eye_close_Rect.x,self.eye_close_Rect.y=self.bodyRect.x+50,self.bodyRect.y+50

    def move(self,postion):
        #self.foot1=self.feet_jump
        #self.foot2=pygame.transform.flip(self.feet_jump,True,False)
        self.bodyRect.x,self.bodyRect.y=postion
        self.mouthRect.x,self.mouthRect.y=self.bodyRect.x-10,self.bodyRect.y+60
        self.mouth_open_Rect.x,self.mouth_open_Rect.y=self.bodyRect.x+50,self.bodyRect.y+50
        self.footRect1.x,self.footRect1.y=self.bodyRect.x+80,self.bodyRect.y+230
        self.footRect2.x,self.footRect2.y=self.bodyRect.x+150,self.bodyRect.y+230
        self.feet_jump_Rect.x,self.feet_jump_Rect.y=self.bodyRect.x+50,self.bodyRect.y+50
        self.eyeRect.x,self.eyeRect.y=self.bodyRect.x+90,self.bodyRect.y+90
        self.eye_close_Rect.x,self.eye_close_Rect.y=self.bodyRect.x+50,self.bodyRect.y+50
