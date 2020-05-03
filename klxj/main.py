#coding=utf8
import sys
import pygame
from pygame.locals import *
from ck import *
from eggs import *
#屏幕图形管理对象
pygame.init()
#设置窗口大小
screen=pygame.display.set_mode((1920,1080),FULLSCREEN,32)
#设置标题
pygame.display.set_caption("彤彤的快乐小鸡")
sound=pygame.mixer.Sound("res/crow.wav")
#分数变量
eggNumber=0
# #入口函数
hen1=hen()
eggsgroup=[]
#初始化游戏，资源加载，界面加载
def init():
   
    #设置分数图像
    eggNumberJpg=pygame.image.load("res/icon_egg.png")
    eggNumberJpgRect=eggNumberJpg.get_rect()
    eggNumberJpgRect=eggNumberJpgRect.move([50,50])
    #添加图像上去
    screen.blit(eggNumberJpg,eggNumberJpgRect)
    #设置分数
    eggNumberFont=pygame.font.SysFont("仿宋",70)
    eggNumberFontText=eggNumberFont.render(str(eggNumber),1,(255,255,255))
    screen.blit(eggNumberFontText,(140,75))
    #画小鸡
    
    screen.blit(hen1.mouth,hen1.mouthRect)
    screen.blit(hen1.foot1,hen1.footRect1)
    screen.blit(hen1.foot2,hen1.footRect2)
    screen.blit(hen1.body,hen1.bodyRect)
    screen.blit(hen1.eye,hen1.eyeRect)
    #更新图形
    

#游戏主循环
def game():
    spend=2
    
    while True:
        
        screen.fill((99,184,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                hen1.move(pygame.mouse.get_pos())
                sound.play() 
                egg1=egg(pygame.mouse.get_pos())
                eggsgroup.append(egg1)
                global eggNumber
                eggNumber+=1
        #移动脚
        
        hen1.footRect1=hen1.footRect1.move(0,spend)
        hen1.footRect2=hen1.footRect2.move(0,-spend)
        if(hen1.footRect1.y>hen1.bodyRect.y+250 or hen1.footRect2.y<hen1.bodyRect.y+210):
            spend=-spend
        if(hen1.footRect1.y<hen1.bodyRect.y+210 or hen1.footRect2.y>hen1.bodyRect.y+250):
            spend=-spend
        
       
        if len(eggsgroup)>0:
            for e in eggsgroup:
                screen.blit(e.egg_img,e.egg_img_rect)
        init()
        pygame.display.flip()
        

        


def main():
    game()
        
if __name__ == "__main__":
    main()