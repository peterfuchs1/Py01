import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.display import *
from pygame.event import *
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
        set_mode(self.display, DOUBLEBUF | OPENGL)
        gluPerspective(45.0, (self.display[0] / self.display[1]), 0.1, 50)
        # moving back.
        glTranslatef(0.0, 0.0, -8.0)
        # where we might be
        glRotatef(10, 1, 1, 1)

    def loop(self):
        while True:
            glRotatef(1, 0, 0, 1)
            # Farbbuffer und Tiefenpuffer entleeren
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            event = pygame.event.poll()
            if event.type == QUIT or self.done:
                pygame.quit()
                exit()
            self.input(event)
            # merke die aktuelle Matrix
            glPushMatrix()
            glTranslatef(self.x, self.y, self.z)
            self.draw_figur()
            glPopMatrix()
            flip()
            pygame.time.wait(10)


    def createSphere(self):
        glColor3f(0, 0.6, 1)
        gluSphere(gluNewQuadric(), 1, 50, 50)

    def draw_figur(self):
        self.createSphere()
        # new handling for Lighting
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

    def input(self, me):
        kpb = pygame.key.get_pressed()  # keyboard pressed buttons

        #me = pygame.event.wait()
        if me.type == MOUSEBUTTONDOWN:
            if me.button == 4:
                self.z += self.c
            elif me.button == 5:
                self.z -= self.c

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

    def get_events(self):
        for event in get():
            if event.type == pygame.K_LEFT:
                self.x = -self.c
            elif event.type == pygame.K_RIGHT:
                self.x = self.c
            elif event.type == pygame.KEYUP:
                self.y = self.c
                self.x = self.c
            elif event.type == pygame.KEYDOWN:
                self.y = -self.c
                self.x = -self.c
            elif event.type == pygame.K_END:
                glLoadIdentity()
            elif event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                print(event.button)
                if event.button == 4:
                    # Herauszoomen z += 1
                    self.z = self.c
                elif event.button == 5:
                    # Hineinzoomen z -= 1
                    self.z = -self.c


if __name__ == '__main__':
    s = Figur()
    s.loop()


