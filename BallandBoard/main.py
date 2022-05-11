#Copyright (C) 2022 CairBin

import pgzrun
import pygame,sys
import define
import actors
from tkinter import messagebox

#创建游戏对象
ball = actors.Ball()
bar = actors.Bar()

TITLE = define.WINDOW_TITLE
WIDTH, HEIGHT = define.WINDOW_SIZE

#碰撞检测
def actorsAcol():
    if ball.y == bar.init_pos[1] and bar.x <= ball.x and ball.x<=bar.x+bar.width:
        ball.changeDirect()

def judgeGameOver():
    if ball.y+ball.r*2 >= define.WINDOW_SIZE[1]:
        pygame.quit()
        messagebox.showinfo('GameOver','GameOver')
        sys.exit()

#pgzurn绘制函数
def draw():
    screen.fill(define.WINDOW_BACKGROUNT_COLOR)
    ball.show(screen)
    bar.show(screen)

#pgzurn刷新函数
def update():
    ball.action()
    actorsAcol()
    judgeGameOver()

#pgzurn获取鼠标位置
def on_mouse_move(pos):
    bar.x = pos[0]-bar.width//2


pgzrun.go()