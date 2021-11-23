from pygame.math import Vector2
import core
import pygame
import random
import math
from Soleil import Soleil


class Etoile:
    def __init__(self):

        self.pos_E = Vector2(random.randint(0, 600), random.randint(0, 400))
        self.couleur_E = (255, 255, 255)
        self.rayon_E = 5

        #self.vitesse = Vector2(0, 0)
        # self.g = 1

        #self.distance = (Vector2(300, 200) - self.pos_E) * (Vector2(300, 200) - self.pos_E)
        # self.masse = (30 * self.rayon_E)
        # self.force = self.g * self.masse / self.distance

        # self.vitesse = (self.vitesse + self.force)

        # self.pos_E = self.pos_E + self.vitesse

    def draw(self, screen):
        # self.pos_E = self.force
        pygame.draw.circle(screen, self.couleur_E, self.pos_E, self.rayon_E)
