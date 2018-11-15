import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import sys

ground_vertices = (
    (-10, -0.1, 20),
    (10, -0.1, 20),
    (10, -0.1, -300),
    (10, -0.1, -300),
    )
class ground(object):
    def ground():
        glBegin(GL_QUADS)
        for vertex in ground_vertices:
            glColor3fv((0, 0.5, 0.5))
            glVertex3fv(vertex)
        glEnd()

class player(object):
    def __init__(self, x, y, z, width, height):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0,-5)

    xMove = 0
    yMove = 0
    zMove = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                #    glTranslatef(1,0,0)
                    xMove = 0.3
                if event.key == pygame.K_RIGHT:
                   # glTranslatef(-1,0,0)
                    xMove = - 0.3
                if event.key == pygame.K_UP:
                   # glTranslatef(0,-1,0)
                    zMove = 0.3
                if event.key == pygame.K_DOWN:
                   # glTranslatef(0,1,0)
                    zMove = -0.3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xMove = 0
                
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                   zMove = 0

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(xMove, yMove, zMove)
             
        ground()
        pygame.display.flip()
        pygame.time.wait(10)

main()
