from pygame.math import Vector2
import core
import pygame
import random
import math


class Soleil:
    def __init__(self):

        self.pos_S = Vector2(300, 200)
        self.couleur_S = (255, 201, 14)
        self.rayon_S = 30

    def draw(self, screen):
        pygame.draw.circle(screen, self.couleur_S, self.pos_S, self.rayon_S)