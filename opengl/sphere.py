import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame import *
from pygame.locals import *

from math import *


class Figur:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.c = 0.1
        self.done = False
        pygame.init()
        self.display = (800, 600)
        display.set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45.0, (self.display[0] / self.display[1]), 0.1, 50)
        # moving back.
        glTranslatef(0.5, 0.5, -8.0)
        # where we might be
        glRotatef(10, 1, 1, 1)

    def loop(self):
        while True:
            glRotatef(1, 0, 0, 1)
            # Farbbuffer und Tiefenpuffer entleeren
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            # events abfragen
            self.input()
            # merke die aktuelle Matrix
            glPushMatrix()
            glTranslatef(self.x, self.y, self.z)
            self.draw_figur()
            glPopMatrix()
            self.draw_light()
            display.flip()
            pygame.time.wait(10)

    def draw_figur(self):
        # blaugrau
        glColor3f(0, 0.6, 1)
        # zeichne eine Kugel mit Radius 1
        # im Zentrum
        gluSphere(gluNewQuadric(), 1, 50, 50)

    def draw_light(self):
        # handling for Lighting
        glEnable(GL_LIGHTING)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 0.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.9, 0.9, 0.9, 0.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [0.5, 0.5, 0.5, 0.0])
        glLightfv(GL_LIGHT0, GL_POSITION, [-2, -2, -20, 1.0])
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)

    def input(self):
        ev = pygame.event.poll()
        if ev.type == QUIT or self.done:
            pygame.quit()
            exit()

        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 4:
                self.z += self.c
            elif ev.button == 5:
                self.z -= self.c
        kpb = pygame.key.get_pressed()  # keyboard pressed buttons

        if kpb[K_ESCAPE]:
            self.done = True

        if kpb[K_UP]:
            self.y += self.c
        if kpb[K_DOWN]:
            self.y -= self.c

        if kpb[K_RIGHT]:
            self.x += self.c
        if kpb[K_LEFT]:
            self.x -= self.c

if __name__ == '__main__':
    s = Figur()
    s.loop()


