# -*-coding:UTF-8 -*-

# 导入基础库

# Util&Log
import locale

import Util

logger = Util.Logger()
logger.info('Start for import library')
# End

import pygame
import requests
import os
import sys
import numpy as np
import cv2

logger.info('End for import library')
# &&&&********-----********&&&& #

# Log
logger.info('Start for init pygame')
# end
pygame.init()
pygame.mixer.init()
# log
logger.info("End for init pygame")
logger.info('System Font > %s' % pygame.font.get_fonts())
logger.info('System Default Font > %s' % pygame.font.get_default_font())
# end

# 基础变量定义
title = ''

workdir = os.getcwd()

resource = Util.Resource(workdir)

# 尝试在线模式
try:
    URL = 'http://perfectfall.cinfinitestudio.xyz'
    rp = requests.get(URL)
    logger.info('Online Mode > %s' % rp.text)
    title = 'Perfect Fall [Online]'
except Exception as exc:
    logger.warn('Offline Mode > %s' % exc)
    title = 'Perfect Fall [Offline]'


class Game:
    STATES = ['NULL', 'LOAD', 'NO_ENTER', 'MENU', 'PLAY', 'END']
    GAME_STATE = ['LEAVE', 'PLAY', 'PAUSE', 'END']
    STATE = STATES[0]
    MENU_STATES = ['NULL', 'SOLO_SELECT', 'MULTI_SELECT', 'CONFIG']
    MENUSTATE = MENU_STATES[0]
    game_size = (1280, 720)

# 修复bug
window = pygame.display.set_mode(Game.game_size, vsync=True)

class Surfaces():
    icon = pygame.image.load(resource.GetResourecePath('image', 'icon', 'png'))
    logoImg = pygame.image.load(resource.GetResourecePath('image', 'logo', 'png')).convert_alpha()

# 基础方法
def renderText(fontPath, textSize, textColor, text, alpha=255):# position,
    global window
    TextFont = pygame.font.Font(fontPath, textSize)
    newText = TextFont.render(text, True, textColor)
    newText.set_alpha(alpha)
    return newText

# 设置

os.environ['SDL_VIDEO_WINDOW_POS'] = '{x},{y}'.format(x=80, y=50)

pygame.display.set_icon(Surfaces.icon)

pygame.display.set_caption(title)

def PaintLogo():
    startImgAlpha = 255
    logoAlpha = 0
    while logoAlpha <= 255:
        Surfaces.logoImg.set_alpha(logoAlpha)
        window.blit(pygame.transform.scale(Surfaces.logoImg, Game.game_size), (0, 0))
        logoAlpha += 5
        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


def handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

PaintLogo()
while True:
    mousePos = pygame.mouse.get_pos()

    handler()
    pygame.display.update()

# Program End For Debug
logger.debug('Log List:' + str(logger.logs))

# #
pygame.quit()
sys.exit()
