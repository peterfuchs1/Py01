'''
Created on 07.07.2014

@author: uhs374h
'''
import sys, math, datetime
import pygame

class MyClock:

    def __init__(self, analog=True):
    # Attribute
        self.analog=analog # Soll der Sokundenzeiger analog dargestellt werden?
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
        pygame.init()
 
        self.screen = pygame.display.set_mode(
            (self.windowWidth, self.windowHeight)
            , pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption("Analog Clock")
    #Endlosschleife fuer den Hauptablauf der Uhr
        while True:
            self.handleEvents()
            self.screen.fill(self.backgroundColor)
            self.drawBackground()
            self.drawCurrentTime()
            self.drawForeground()
            pygame.display.flip()
            pygame.time.delay(10)

    def getCursorPositionDegrees(self, position, scale):
# 12 Uhr entspricht -90 Grad
        cursorOffset = -90
        degrees = 360 / scale * position + cursorOffset
        return degrees

    def gradToBogenmass(self, degrees):
# python bietet auch die Funktion math.radians(degrees),
# welche die Umrechnung genauso ausfuehrt, aber so wird
# der Sachverhalt deutlicher
        return degrees/180.0*math.pi


    def getCirclePoint(self, position, scale, cursorLength):
        degrees = self.getCursorPositionDegrees(position, scale)
        bogenmass = self.gradToBogenmass(degrees)
        xPos = round(math.cos(bogenmass)*cursorLength+self.windowCenter[0])
        yPos = round(math.sin(bogenmass)*cursorLength+self.windowCenter[1])
        return (xPos, yPos)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                sys.exit(0)

    def drawBackground(self):
        self.screen.fill(self.backgroundColor)
        pygame.draw.ellipse(self.screen, self.clockMarginColor, (self.windowMargin,\
                self.windowMargin, self.windowWidth-2*self.windowMargin,\
                self.windowWidth-2*self.windowMargin))
        pygame.draw.ellipse(self.screen, self.clockBackgroundColor,\
                        (self.windowMargin+self.clockMarginWidth/2,\
                         self.windowMargin+self.clockMarginWidth/2,\
                         self.windowWidth-(self.windowMargin+self.clockMarginWidth/2)*2,\
                         self.windowWidth-(self.windowMargin+self.clockMarginWidth/2)*2))
        # paint the quator and the 5minute-ticks
        for i in range (0,60,1):
            start=self.getCirclePoint(i, 60, self.radius)
            length=self.oneMinuteTicks
            if i%15==0:
                length=self.quatorTicks
            elif i%5==0:
                length=self.fiveMinuteTicks
                
            self.drawCursor(self.ticksColor, 5, length,i, 60,start)


        
    def drawForeground(self):
        pygame.draw.ellipse(self.screen, self.clockMarginColor,\
                        (self.windowWidth/2.0-9, self.windowHeight/2.0-9, 18, 18))

    def drawCursor(self,color, width, length, position, scale, start=0):
        start =(start if start!=0 else self.windowCenter)
        end = self.getCirclePoint(position, scale, length)
        pygame.draw.line(self.screen, color, start, end, width)

    def drawCurrentTime(self):
        if self.useVirtualTimer:
            global hour, minute, second, micro
            self.timeGoesOn()
        else:
            now = datetime.datetime.now()
            micro = now.microsecond
            hour = now.hour
            minute = now.minute
            second = now.second
        # Stundenzeiger    
        self.drawCursor(self.hourColor, 15,
                   self.hourCursorLength,
                   hour+minute/60.0, 12)
        # Minutenzeiger
        self.drawCursor(self.minuteColor, 8,
                   self.minuteCursorLength,
                   minute+second/60.0, 60)
        showSecond=(second+micro/1000000.0 if self.analog else second)
        # Sekundenzeiger analog versus Sekundenzeiger digital
        self.drawCursor(self.secondColor, 3,
                   self.secondCursorLength,
                   showSecond, 60)
        

    hour = 0
    minute = 0
    second = 0
    micro = 0
    def timeGoesOn(self):
        global hour, minute, second, micro
        micro += self.virtualSpeed
        if micro >= 2: # halve seconds - not micro seconds
            second += 1
            micro %= 2
        if second > 60:
            minute += 1
            second %= 60
        if minute > 60:
            hour += 1
            minute %= 60
        if hour > 12:
            hour %= 12    


if __name__ == '__main__':
    MyClock(analog=False)