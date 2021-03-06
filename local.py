# --- Imports --- #

import pygame, os, sys
pygame.init()

# --- Variables --- #

BLACK = (0,)*3
DARKBROWN = (74,49,34) #Dark Dirt
BROWN = (136,89,63)
LIGHTBROWN = (185,122,86) #Menus and dirt
GOLD = (255,202,24)
YELLOW = (245,225,0)
GREEN = (14,209,69) #Grass
DARKGREEN = (14,56,14) #Dark Grass
LIGHTBLUE = (0,168,243)
BLUE = (0,119,190) #Ocean Blue
DARKBLUE = (0,48,76) #Dark Ocean
DARK = (35,)*3
DARKRED = (55,35,35)
RED = (255,0,0)
WHITE = (255,)*3

DISPLAYW = 1280
DISPLAYH = 720
LANDHEIGHT = 580

MOVEMENT = 8
RUN_MOVEMENT = MOVEMENT*2

COMICSANS = pygame.font.SysFont("comicsansms", 20)
OPENDYSLEXIC = pygame.font.Font(f"{sys.path[0]}/Fonts/OpenDyslexic.otf", 20)
FONT = COMICSANS #This is not constant, changes in __init__.py for dyslexic use

DAYNIGHT = pygame.event.custom_type()
DAYCYCLETIME = 60000
DAYNIGHTEVENT = pygame.event.Event(DAYNIGHT)

ATTACK = pygame.event.custom_type()
ATTACKTIME = 10000
ATTACKEVENT = pygame.event.Event(ATTACK)

IMAGE_PATH = f"{sys.path[0]}/Images"
SAVE_PATH = f"{sys.path[0]}/Saves/{os.getlogin()}.sgf"
ERROR_PATH = f"{sys.path[0]}/Error.log"

SHIFTS = (pygame.KMOD_LSHIFT, pygame.KMOD_RSHIFT)
