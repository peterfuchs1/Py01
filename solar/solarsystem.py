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
        self.w = 800
        self.h = 600
        self.display = (self.w, self.h)
        display.set_mode(self.display, DOUBLEBUF | OPENGL)
        display.set_caption("A simple solarsystem")
        glShadeModel(GL_FLAT)
        glClearColor(0.0, 0.0, 0.0, 0.0 )
        glClearDepth(1.0 )
        glEnable(GL_DEPTH_TEST)

        glMatrixMode( GL_PROJECTION )
        #glLoadIdentity()

        #glShadeModel(GL_SMOOTH)
        gluPerspective(60.0, (self.display[0] / self.display[1]), 0.5, 100)
        # moving back.
        glTranslatef(0.5, 0.5, -8.0)
        # where we might be
        glRotatef(5, 1, 1, 1)

        glMatrixMode(GL_MODELVIEW)

        self.spinMode = GL_TRUE
        self.singleStep = GL_FALSE

        # These three variables control the animation's state and speed.
        self.HourOfDay = 0.0
        self.DayOfYear = 0.0
        self.AnimateIncrement = 24.0  # Time step for animation (hours)
        glutInit()

    def loop(self):
        """ The basic loop for presentation

        """
        while True:
            # events abfragen
            self.input()
            if self.done:
                break
                # Clear the redering window
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            if self.spinMode:
                # Update the animation state
                self.HourOfDay += self.AnimateIncrement
                self.DayOfYear += self.AnimateIncrement / 24.0

                self.HourOfDay -= (self.HourOfDay // 24 * 24)
                self.DayOfYear -= (self.DayOfYear // 365 * 365)

            # Clear the current matrix (Modelview)
            glLoadIdentity()
            #  Back off eight units to be able to view from the origin.
            glTranslatef(0.0, 0.0, -8.0)  # Rotate the plane of the elliptic
            # (rotate the model's plane about the x axis by fifteen degrees)
            #glRotatef(1.0, 0.0, 0.0, 1.0)
            glRotatef(15.0, 1.0, 0.0, 0.0)

            # Draw the sun	-- as a yellow,  wireframe sphere
            glColor3f(1.0, 1.0, 0.0)
            glutWireSphere(1.0, 50, 50)
            # Draw the Earth  # First position it around the sun  #		Use DayOfYear to determine its position
            glRotatef(360.0 * self.DayOfYear / 365.0, 0.0, 1.0, 0.0)
            glTranslatef(4.0, 0.0, 0.0)
            glPushMatrix()  # Save matrix state  # Second,  rotate the earth on its axis.
            # Use HourOfDay to determine its rotation.
            glRotatef(360.0 * self.HourOfDay / 24.0, 0.0, 1.0, 0.0)  # Third,  draw the earth as a wireframe sphere.
            glColor3f(0.2, 0.2, 1.0)
            glutWireSphere(0.4, 40, 40)
            glPopMatrix()  # Restore matrix state
            #  Draw the moon.
            # #	Use DayOfYear to control its rotation around the earth
            glRotatef(360.0 * 12.0 * self.DayOfYear / 365.0, 0.0, 1.0, 0.0)
            glTranslatef(0.7, 0.0, 0.0)
            glColor3f(0.3, 0.7, 0.3)
            glutWireSphere(0.1, 20, 20)  # Flush the pipeline,  and swap the buffers

            glFlush()
            #glutSwapBuffers()

            if self.singleStep:
                self.spinMode = GL_FALSE
            #glutPostRedisplay()  # Request a re-draw for animation purposes
            # pause the program for an amount of time [ms]
            pygame.time.wait(20)
            display.flip()

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
