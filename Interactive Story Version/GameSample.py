import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import os, random
import split
from math import sin, cos


ground_vertices = (
    (-10, -0.1, 20),
    (10, -0.1, 20),
    (10, -0.1, -300),
    (10, -0.1, -300),
    )

def ground():
    glBegin(GL_QUADS)
    for vertex in ground_vertices:
        glColor3fv((0, 0.5, 0.5))
        glVertex3fv(vertex)
    glEnd()

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
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

def Cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


yrot = 0.0
xpos = 0.0
zpos = 0.0

lookupdown = 0.0
walkbias = 0.0
walkbiasangle = 0.0

LightAmbient  = [ 0.5, 0.5, 0.5, 1.0]
LightDiffuse  = [ 1.0, 1.0, 1.0, 1.0]
LightPosition = [ 0.0, 0.0, 2.0, 1.0]

piover180 = 0.0174532925
        
#def init():
  #  global lookupdown, walkbias, walkbiasangle

    #glShadeModel(GL_SMOOTH)
    #glClearColor(0.0, 0.0, 0.0, 0.0)
    #glClearDepth(1.0)
    #glEnable(GL_DEPTH_TEST)
    #glDepthFunc(GL_LEQUAL)
    #glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    #glLightfv( GL_LIGHT1, GL_AMBIENT, LightAmbient )
    #glLightfv( GL_LIGHT1, GL_DIFFUSE, LightDiffuse )
    #glLightfv( GL_LIGHT1, GL_POSITION, LightPosition )
    #glEnable( GL_LIGHT1 )
    #lookupdown    = 0.0
    #walkbias      = 0.0
    #walkbiasangle = 0.0
    #glColor4f( 1.0, 1.0, 1.0, 0.5)    


def main():

    global xpos, zpos, yrot, filter
    global piover180, walkbiasangle, walkbias

    
    pygame.init()
    display = (800, 600)
    #init()
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
                    yrot = -0.5
                if event.key == pygame.K_RIGHT:
                   # glTranslatef(-1,0,0)
                    yrot = 0.5
                if event.key == pygame.K_UP:
                   # glTranslatef(0,-1,0)
                    xpos = -sin(yrot * piover180)*0.5
                    zpos = -cos(yrot * piover180)*0.5

                    if (walkbiasangle >= 359.0):
                        walkbiasangle = 0.0
                    else:
                        walkbiasangle += 10.0
                    walkbias = sin(walkbiasangle * piover180)/20.0
                    
                if event.key == pygame.K_DOWN:
                   # glTranslatef(0,1,0)
                    xpos = sin(yrot * piover180)*0.5
                    zpos = cos(yrot * piover180)*0.5
                    if (walkbiasangle <= 1.0):
                        walkbiasangle = 359.0
                    else:
                        walkbiasangle -= 10.0
                    walkbias = sin (walkbiasangle * piover180)/20.0

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    yrot = 0
                
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                   xpos = 0
                   zpos = 0

        xtrans = -xpos
        ztrans = -zpos
        ytrans = -walkbias-0.25
        sceneroty = 360.0 - yrot
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #glLoadIdentity()
        glRotatef(lookupdown, 1.0, 0.0, 0.0)
        glRotatef(sceneroty, 0.0, 1.0, 0.0)
        glTranslatef(xtrans, 0, ztrans)
             
        ground()
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
