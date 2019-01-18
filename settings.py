#Settings Management Package
import pygame
from pygame.locals import *

#WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
WINDOW_WIDTH, WINDOW_HEIGHT = 1080, 640
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Balloon Shooter Game")
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
TOP_WINDOW_MARGIN = 10

#Few Set of Colors
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

import math
import random
from arrows import *
from balloon import *
from player import *
from events import *