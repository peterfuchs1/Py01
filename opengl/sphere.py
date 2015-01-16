import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame import *
from pygame.locals import *


class Figur:
    """ Erstellt eine Kugel in pygame mittels OpenGL

    :ivar float x: x coordinate
    :ivar float y: y coordinate
    :ivar float z: z coordinate
    :ivar float r: radius of the planet
    :ivar float c: increment or decrement for zooming and positioning
    :ivar bool done: game finished?
    :ivar bool paused: game paused?
    :ivar tuple display: size of the frame (x,y)
    """
    def __init__(self):
        """ Initialisiert pygame

        """
        self.x = 1.0
        self.y = 1.0
        self.z = 1.0
        self.c = 0.1
        self.r = 0.4
        self.done = False
        self.paused = False
        pygame.init()
        self.display = (800, 600)
        display.set_mode(self.display, DOUBLEBUF | OPENGL)
        glShadeModel(GL_SMOOTH)
        gluPerspective(45.0, (self.display[0] / self.display[1]), 0.1, 500)
        # moving back.
        glTranslatef(0.5, -1.5, -6.0)
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
                glDisable(GL_LIGHTING)
                # Unsere Figur wird um 1° um die z-Achse gedreht
                glRotatef(1, 0, 0, 1)
                # glClearColor(0.5, 0.5, 0.5, 1)
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


                # Position camera to look at the world origin.
                # gluLookAt(5, 5, 5, 0, 0, 0, 0, 0, 1)

                # Farbbuffer und Tiefenpuffer entleeren
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                # merke die aktuelle Matrix

                # glLoadIdentity()
                self.draw_sun()
                glPushMatrix()

                Figur.helperSetupLighting()
                Figur.helperPlaceLight()
                glTranslatef(self.x, self.y, self.z)
                self.draw_figur()
                glPopMatrix()


                #self.draw_light()
                display.flip()
            # pause the program for an amount of time [ms]
                pygame.time.wait(10)
        # quit pygame and exit the application
        pygame.quit()

    @staticmethod
    def helperSetupLighting():
        zeros = (0.15, 0.15, 0.15, 0.3)
        ones = (1.0, 1.0, 1.0, 0.3)
        half = (0.5, 0.5, 0.5, 0.5)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
        glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
        glLightfv(GL_LIGHT0, GL_SPECULAR, half)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)

        glEnable(GL_COLOR_MATERIAL)
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)

    @staticmethod
    def helperPlaceLight():
        # last value means point light
        position = (0.0, 0.0, 0.0, 1.0)
        glLightfv(GL_LIGHT0, GL_POSITION, position)

    def draw_sun(self):
        """ Erzeugt eine Kugel im Zentrum (0,0,0)

        """
        # blaugrau
        glColor3f(1, 1, 1)
        # zeichne eine Kugel mit Radius 1
        # im Zentrum
        glutInit()
        glutSolidSphere(0.7, 50, 50)
        # gluSphere(gluNewQuadric(), 1 , 50, 50)


    def draw_figur(self):
        """ Erzeugt eine Kugel im Zentrum (0,0,0)

        """
        # blaugrau
        glColor3f(0, 0.6, 1)
        # zeichne eine Kugel mit Radius 1
        # im Zentrum
        gluSphere(gluNewQuadric(), self.r , 50, 50)

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
