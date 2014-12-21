import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.display import *
from pygame.event import *
from pygame.locals import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

surfaces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6),
)


def draw_cube():
    # first we paint the surfaces
    glBegin(GL_QUADS)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((1, 1, 1))
            glVertex3fv(verticies[vertex])
    glEnd()
    # secand we paint the lines
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1, 0, 0))
            glVertex3fv(verticies[vertex])
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
                glTranslatef(0.0, 0.0, 1.0)
            elif event.button == 5:
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
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        flip()
        pygame.time.wait(10)
