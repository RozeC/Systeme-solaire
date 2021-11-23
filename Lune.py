from pygame.math import Vector2
import core
import pygame
import random
import math


class Lune:
    def __init__(self):

        self.pos_L = Vector2(180, 120)
        self.couleur_L = (192, 192, 192)
        self.rayon_L = 10

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_L, self.pos_L, self.rayon_L)