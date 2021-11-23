from pygame.math import Vector2
import core
import pygame
import random
from Etoile import Etoile
from Soleil import Soleil
from Terre import Terre
from Lune import Lune


def setup():
    print("Setup START---------")

    core.fps = 30
    core.WINDOW_SIZE = [600, 400]

    core.memory("etoile", [])
    core.memory("J", 0)

    core.memory("soleil", [])
    core.memory("s", 1)

    core.memory("terre", [])
    core.memory("t", 1)

    core.memory("lune", [])
    core.memory("l", 1)

    for i in range(50):
        core.memory("etoile").append(Etoile())

    core.memory("soleil").append(Soleil())
    core.memory("terre").append(Terre())
    core.memory("lune").append(Lune())

  #  J.append(Etoile())

    print("Setup END-----------")


def run():
    core.cleanScreen()

    for c in core.memory("etoile"):
        c.draw(core.screen)

    for s in core.memory("soleil"):
        s.draw(core.screen)

    for t in core.memory("terre"):
        t.draw(core.screen)

    for l in core.memory("lune"):
        l.draw(core.screen)




core.main(setup, run)