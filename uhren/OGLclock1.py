"""
Created on 07.07.2014

@author: uhs374h
"""
from IPython.nbformat import current
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, sys, math, datetime
from pygame.locals import *
#from pygame import *
class MyClock:
    '''
    MyClock is a OpenGL analog clock
    '''
    def __init__(self, analog=True, background=True):
    # Attribute
        self.background = background # Soll der Hintergrund angezeigt werden?
        self.analog = analog # Soll der Sokundenzeiger analog dargestellt werden?
        self.windowMargin = 30
        self.windowWidth = 600
        self.windowHeight = self.windowWidth
        self.windowCenter = self.windowWidth/2, self.windowHeight/2
        self.clockMarginWidth = 20
        self.secondColor = (255, 0, 0)
        self.minuteColor = (100, 200, 0)
        self.hourColor = (100, 200, 0)
        self.clockMarginColor = (130, 130, 0)
        self.clockBackgroundColor = (20, 40, 30)
        self.backgroundColor = (255, 255, 255)
        self.ticksColor=(255,255,0)
        self.radius=self.windowWidth/2.0-self.windowMargin
        self.hourCursorLength = self.radius-140
        self.minuteCursorLength = self.radius-40
        self.secondCursorLength = self.radius-10
        self.quatorTicks=self.radius*0.75
        self.fiveMinuteTicks=self.quatorTicks*1.2
        self.oneMinuteTicks=self.secondCursorLength
        self.virtualSpeed = 1
        self.useVirtualTimer = False
    
    #Initialisierung des Screens
        video_flags = OPENGL|HWSURFACE|DOUBLEBUF
        pygame.init()
        pygame.display.gl_set_attribute(GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(GL_MULTISAMPLESAMPLES, 4)
    
        self.screen = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight)
            , video_flags)
        pygame.display.set_caption("Analog Clock")
        self.resize((self.windowWidth,self.windowHeight))
        self.init()
    #Endlosschleife fuer den Hauptablauf der Uhr
        frames = 0
        ticks = pygame.time.get_ticks()
        while True:
            event = pygame.event.poll()
            if event.type == QUIT or\
                (event.type == KEYDOWN and\
                 event.key == K_ESCAPE):
                break
            self.draw()
            pygame.display.flip()
            frames += 1
        print( "fps: %d" % ((frames*1000)/(pygame.time.get_ticks()-ticks)))
    
    
    '''
        while True:
            self.handleEvents()
            self.screen.fill(self.backgroundColor)
            self.drawBackground()
            self.drawCurrentTime()
            self.drawForeground()
            pygame.display.flip()
            pygame.time.delay(10)
    '''
        
    def resize(self,size):
        width, height=size
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-0.2, 4.2, 4.2, -0.2, -6.0, 0.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def init(self):
        glShadeModel(GL_SMOOTH)
        glClearColor(0.0, 0.0, 0.0, 0.0)
        glClearDepth(1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
        
    def drawRing(self, radius, width, depth):
        outerRadius = radius+width/2
        innerRadius = radius-width/2
        numCircleVertices = 1000
        inner = True
        glColor4f(0.9, 0.4, 0.2, 1.0)
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(numCircleVertices):
            angle = (i / float(numCircleVertices-2)) * 2 * math.pi;
            currentRadius = innerRadius if inner else outerRadius
            """
            if inner:
                currentRadius = innerRadius
            else:
                currentRadius = outerRadius
            """
            x = math.cos(angle) * currentRadius
            y = math.sin(angle) * currentRadius
            inner = not inner
            glVertex3f(x, y, depth)
        glEnd()
    def drawPointer(self, width, length, position, scale):
        angle = float(position)/scale*360.0
        glRotatef(+angle, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(-width/2, 0.0, 0.0)
        glVertex3f(+width/2, 0.0, 0.0)
        glVertex3f(0.0, -length, 0.0)
        glVertex3f(-width/2, 0.0, 0.0)
        glVertex3f(+width/2, 0.0, 0.0)
        if length > 0:
            glVertex3f(0.0, +0.2, 0.0)
        else:
            glVertex3f(0.0, -0.2, 0.0)
        glEnd()
        glRotatef(-angle, 0.0, 0.0, 1.0)
    
    def drawCurrentTime(self, hour, minute, second, micro):
        glColor4f(0.3, 0.7, 0.2, 1.0)
        self.drawPointer(0.20, 1.0, hour+(minute/60.0), 12)
        glColor4f(0.3, 0.9, 0.5, 1.0)
        self.drawPointer(0.15, 1.8, minute+(second/60.0), 60)
        glColor4f(0.8, 0.4, 0.8, 1.0)
        showSecond=(second+micro/1000000.0 if self.analog else second)
        self.drawPointer(0.08, 2.0, showSecond, 60)

    def drawClockFace(self):

        for minute in range(60):
            angle = float(minute)/60*360.0
            glRotatef(+angle, 0.0, 0.0, 1.0)
            # Ganze 5 Minuten werden dicker dargestellt
            # und länger
            big = minute % 5 == 0
            if big:
                glColor4f(0.4, 0.7, 0.9, 1.0)
            else:
                glColor4f(1.0, 1.0, 0.0, 1.0)
            glBegin(GL_QUADS)
            x, y = (0.05, 1.5) if big else (0.01, 1.7)
            glVertex3f(-0.01, y, 0.0)
            glVertex3f(+0.01, y, 0.0)
            glVertex3f(+x, 1.9, 0.0)
            glVertex3f(-x, 1.9, 0.0)
            glEnd()
            glRotate(-angle, 0.0, 0.0, 1.0)

        """
        for hour in range(12):
            angle = float(hour)/12*360.0
            glColor4f(0.4, 0.7, 0.9, 1.0)
            glRotatef(+angle, 0.0, 0.0, 1.0)
            glBegin(GL_QUADS)
            glVertex3f(-0.01, 1.5, 0.0)
            glVertex3f(+0.01, 1.5, 0.0)
            glVertex3f(+0.05, 1.9, 0.0)
            glVertex3f(-0.05, 1.9, 0.0)
            glEnd()
            glRotate(-angle, 0.0, 0.0, 1.0)
        """
    def drawClockBackground(self,hour, minute, second):

        glBegin(GL_POLYGON)
        # center of the fan with last used color
        #glVertex3f(0.0, 0.0, 0.0)
        numCircleVertices = 300
        clockRadius = 2.0

        for i in range(numCircleVertices):
            angle = (i / float(numCircleVertices-1)) * 2 * math.pi
            x = math.cos(angle) * clockRadius
            y = math.sin(angle) * clockRadius
            # red, green, blue in relation to the current time
            glColor4f(second/60.0, minute/60.0, hour/24.0, 1.0)
            #glColor4f(1, 1, 1, 1.0)
            glVertex3f(x, y, 0.0)
        glEnd()


    def clockRotate(self, second, micro, start, stop, rotation):
        x, y, z = rotation
        
        clockRotation = (second - start +
                         micro/1000000.0)/(stop-start)*360.0
        # new handling for Lighting
        glEnable(GL_LIGHTING)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.9, 0.9, 0.9, 1.0])
        glLightfv(GL_LIGHT0, GL_POSITION, [-2, -2, -1.0, 1.0])
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
        glEnable(GL_TEXTURE_GEN_S)
        glEnable(GL_TEXTURE_GEN_T)

        glEnable(GL_NORMALIZE)
        if 90 < clockRotation < 270:
            # invert the normal vector
            glNormal3f(0.0, 0.0, +1.0)
        if clockRotation <= 360:
            glRotate(clockRotation, x, y, z)
    
    def draw(self):
        # Tiefenpuffer und Farbpuffer loeschen
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Systemzeit auslesen
        now = datetime.datetime.now()
        micro = now.microsecond
        hour = now.hour
        minute = now.minute
        second = now.second
        # Identitaetsmatrix laden und Ansicht verschieben
        glLoadIdentity()
        glTranslatef(2.0, 2.0, 3.0)
        
       
        
        glNormal3f(0.0, 0.0, -1.0)
        if 0 <= second <= 10:
            self.clockRotate(second, micro, 0, 10, (1.0, 0.0, 0.0))
        elif 30 <= second <= 40:
            self.clockRotate(second, micro, 30, 40, (0.0, 1.0, 0.0))
        
    # Drehung der Uhr
        if second >= 50:
            self.clockRotate(second, micro, 50.0, 58, (1.0, 1.0, 0.0))
      
        # Zeichnen der Uhr
        if self.background:
            self.drawClockBackground(hour, minute, second)
        self.drawClockFace()
        self.drawCurrentTime(hour, minute, second, micro)
        self.drawRing(2.0, 0.1, -0.1)
        self.drawRing(2.0, 0.1, +0.1)

    def connectRings(self, radius, depth1, depth2):
        numCircleVertices = 1000
        inner = True
        glColor4f(0.9, 0.4, 0.2, 1.0)
        glBegin(GL_TRIANGLE_STRIP)
        for i in range(numCircleVertices):
            angle = (i / float(numCircleVertices-2)) * 2 * math.pi;
            if inner:
                depth = depth1
            else:
                depth = depth2
            x = math.cos(angle) * radius
            y = math.sin(angle) * radius
            inner = not inner
            glVertex3f(x, y, depth)
        glEnd()


if __name__ == '__main__':
    MyClock(analog=False, background=False)