from pygame.math import Vector2
import core
import pygame
import random
import math


class Terre:
    def __init__(self):

        self.pos_T = Vector2(150, 100)
        self.couleur_T = (34, 177, 76)
        self.rayon_T = 15

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_T, self.pos_T, self.rayon_T)