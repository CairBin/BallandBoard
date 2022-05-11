#Copyright (C) 2022 CairBin
import pgzrun
import pygame.rect
import define
import random


class Ball:
    def __init__(self):
        #球的初始位置
        self.init_pos = (define.WINDOW_SIZE[0]//2,define.WINDOW_SIZE[1]//2)
        #球的位置
        self.x,self.y = self.init_pos
        #球的半径
        self.r = 20
        #球的颜色
        self.color = 'blue'
        #球的速度
        self.speed_x = random.sample([4,-4,-4],1)[0]
        self.speed_y = 4

    #绘制
    def show(self,surface):
        surface.draw.filled_circle((self.x,self.y),self.r,self.color)

    #动画
    def action(self):
        #移动
        self.y = self.y + self.speed_y
        self.x = self.x+self.speed_x
        #当球触碰边界
        if self.y >= define.WINDOW_SIZE[1]-self.r or self.y <= self.r:
            self.speed_y = -self.speed_y
        if self.x >= define.WINDOW_SIZE[0]-self.r or self.x<=self.r:
            self.speed_x = -self.speed_x

    #碰撞改变方向
    def changeDirect(self):
        lst_x = [1,-1,-self.speed_x,self.speed_x,5,-5,-self.speed_x,self.speed_x,5,-5]
        ra_num = random.randint(0,len(lst_x)-1)
        self.speed_x = lst_x[ra_num]

        lst_y = [-3,-4,-5,-3,-4]
        ra_num = random.randint(0, len(lst_y) - 1)
        self.speed_y = lst_y[ra_num]




class Bar:
    def __init__(self):
        #宽度和高度
        self.width = define.WINDOW_SIZE[0]/6
        self.height = define.WINDOW_SIZE[1]/30
        #初始位置
        self.init_pos =  (define.WINDOW_SIZE[0]//2,define.WINDOW_SIZE[1]*0.7)
        self.x = self.init_pos[0]
        #颜色
        self.color = 'red'


    #绘制
    def show(self,surface):
        if self.x >= define.WINDOW_SIZE[0]-self.width:
            self.x = define.WINDOW_SIZE[0]-self.width
        if self.x<=0:
            self.x = 0
        box = pygame.rect.Rect((self.x,self.init_pos[1]),(self.width,self.height))
        surface.draw.filled_rect(box,self.color)





