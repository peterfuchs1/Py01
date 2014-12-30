import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame import *
from pygame.locals import *


class Figur:
    """ Erstellt eine Kugel in pygame mittels OpenGL

    :ivar float x: x coordinate
    :ivar float y: y coordinate
    :ivar float z: z coordinate
    :ivar float c: increment or decrement for zooming and positioning
    :ivar bool done: game finished?
    :ivar bool paused: game paused?
    :ivar tuple display: size of the frame (x,y)
    """
    def __init__(self):
        """ Initialisiert pygame

        """
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.c = 0.1
        self.done = False
        self.paused = False
        pygame.init()
        self.display = (800, 600)
        display.set_mode(self.display, DOUBLEBUF | OPENGL)
        glShadeModel(GL_SMOOTH)
        gluPerspective(45.0, (self.display[0] / self.display[1]), 0.1, 50)
        # moving back.
        glTranslatef(0.5, 0.5, -8.0)
        # where we might be
        glRotatef(10, 1, 1, 1)

    def loop(self):
        """ The basic loop for presentation

        """
        while True:
            # events abfragen
            self.input()
            if self.done:
                break
            if not self.paused:
                # Unsere Figur wird um 1° um die z-Achse gedreht
                glRotatef(1, 0, 0, 1)
                # Farbbuffer und Tiefenpuffer entleeren
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                # merke die aktuelle Matrix
                glPushMatrix()
                glTranslatef(self.x, self.y, self.z)
                self.draw_figur()
                glPopMatrix()
                self.draw_light()
                display.flip()
            # pause the program for an amount of time
            pygame.time.wait(10)
        # quit pygame and exit the application
        pygame.quit()

    @staticmethod
    def draw_figur():
        """ Erzeugt eine Kugel im Zentrum (0,0,0)

        """
        # blaugrau
        glColor3f(0, 0.6, 1)
        # zeichne eine Kugel mit Radius 1
        # im Zentrum
        gluSphere(gluNewQuadric(), 1, 50, 50)

    @staticmethod
    def draw_light():
        """ Erstellt eine Lichtquelle Light0

        """
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
        """ Reagiert auf Events von Keyboard und Maus

        """
        ev = pygame.event.poll()
        if ev.type == QUIT:
            self.done = True
            return

        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 4:
                self.z += self.c
            elif ev.button == 5:
                self.z -= self.c
            elif ev.button == 1:
                self.paused = not self.paused

        kpb = pygame.key.get_pressed()  # keyboard pressed buttons

        if kpb[K_ESCAPE]:
            self.done = True
        elif kpb[K_SPACE]:
            self.paused = not self.paused
        elif kpb[K_UP]:
            self.y += self.c
        elif kpb[K_DOWN]:
            self.y -= self.c
        elif kpb[K_RIGHT]:
            self.x += self.c
        elif kpb[K_LEFT]:
            self.x -= self.c
        elif kpb[K_KP_PLUS]:  # vergrößern um 0.1%
            glScalef(1.001, 1.001, 1.001)
        elif kpb[K_KP_MINUS]:  # verkleinern auf 99,9%
            glScalef(0.999, 0.999, 0.999)

if __name__ == '__main__':
    s = Figur()
    s.loop()
