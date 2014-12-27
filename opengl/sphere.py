
import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.display import *
from pygame.event import *
from pygame.locals import *

verticies = (
    # start of the triangle
    (-1, -1, 0),
    (1, -1, 0),
    (0, 1, 0),
)

colors = (
    (1, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
)

edges = (
    # start of the triangle
    (0, 1),
    (0, 2),
    (1, 2),
)

surfaces = (
    (0, 1, 2),
)


def draw_figur():
    # first we paint the surfaces
    """
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((1, 1, 1))
            glVertex3fv(verticies[vertex])
    glEnd()
    """
    # secand we paint the lines
    glBegin(GL_TRIANGLES)
    i = 0
    for vertex in verticies:
        glColor3fv(colors[i])
        glVertex3fv(verticies[i])
        i += 1
    glEnd()


def get_events():
    for event in get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            print(event.button)
            if event.button == 4:
                # Herauszoomen z += 1
                glTranslatef(0.0, 0.0, 1.0)
            elif event.button == 5:
                # Hineinzoomen z -= 1
                glTranslatef(0.0, 0.0, -1.0)

if __name__ == '__main__':
    pygame.init()
    display = (800, 600)
    set_mode(display, DOUBLEBUF | OPENGL)

    #
    gluPerspective(45.0, (display[0]/display[1]), 0.1, 50)

    # moving back.
    glTranslatef(0.0, 0.0, -5.0)
    # where we might be
    glRotatef(20, 2, 0, 0)

    while True:
        get_events()
        glRotatef(1, 0, 1, 0)
        glScalef(1.001, 1, 1)
        # Farbbuffer und Tiefenpuffer entleeren
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_figur()
        flip()
        pygame.time.wait(10)
