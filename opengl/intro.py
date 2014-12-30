import pygame

__author__ = 'uhs374h'
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.display import *
from pygame.event import *
from pygame.locals import *

verticies = (
    # start of the cube
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    # start of the octahedron
    (0, 0, -1),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, -1, 0),

)

edges = (
    # start of the cube
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
    # start of the octahedron
    (8, 9),
    (8, 10),
    (9, 11),
    (10, 11),
    (8, 12),
    (9, 12),
    (10, 12),
    (11, 12),
    (8, 13),
    (9, 13),
    (10, 13),
    (11, 13),
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
    # new handling for Lighting
    glEnable(GL_LIGHTING)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.9, 0.9, 0.9, 1.0])
    glLightfv(GL_LIGHT0, GL_POSITION, [-2, -2, 3.0, 1.0])
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

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


def main():
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
        # Farbbuffer und Tiefenpuffer entleeren
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        flip()
        pygame.time.wait(10)



if __name__ == '__main__':
    main()
