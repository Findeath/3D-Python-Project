import pygame
from pygame.locals import *
from pygame.constants import *
import numpy

from OpenGL.GL import *
from OpenGL.GLU import *

import os, random
import split
from math import sin, cos, radians

import pygame, math, numpy, sys
from OpenGL.GL import *
from OpenGL.GLU import *

# IMPORT OBJECT LOADER
from ObjectLoader import *

import pyrr

import ShaderLoader

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

GROUND_LEVEL = 1
InAir = False

##def tree():
##    obj = ObjLoader()
##    obj.load_model("PineTree1.obj")
##
##    texture_offset = len(obj.vertex_index)*12
##
##    shader = ShaderLoader.compile_shader("shaders/video_17_vert.vs", "shaders/video_17_frag.fs")
##
##    VBO = glGenBuffers(1)
##    glBindBuffer(GL_ARRAY_BUFFER, VBO)
##    glBufferData(GL_ARRAY_BUFFER, obj.model.itemsize * len(obj.model), obj.model, GL_STATIC_DRAW)
##    #position
##    glVertexAttribPointer(0,3,GL_FLOAT, GL_FALSE, obj.model.itemsize * 3, ctypes.c_void_p(0))
##    glEnableVertexAttribArray(0)
##
##    glUseProgram(shader)
##   

class Spectator:
    def __init__(self, w=640, h=480, fov=75):
        pygame.init()
        pygame.display.set_mode((640,480), pygame.OPENGL | \
            pygame.DOUBLEBUF)
        glMatrixMode(GL_PROJECTION)
        aspect = w/h
        gluPerspective(fov, aspect, 0.001, 100000.0);
        glMatrixMode(GL_MODELVIEW)

    def simple_lights(self):
        glEnable(GL_LIGHTING)
        glShadeModel(GL_SMOOTH)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.9, 0.45, 0.0, 1.0))
        glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 10.0, 10.0, 10.0))
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
            
    def simple_camera_pose(self):
        """ Pre-position the camera (optional) """
        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(numpy.array([0.741,-0.365,0.563,0,0,0.839,0.544,
            0,-0.671,-0.403,0.622,0,-0.649,1.72,-4.05,1]))
        glTranslatef(0.0, 0.0, -2)

    def draw_simple_cube(self):
        """ Draw a simple object (optional) """
        try:
            glEnableClientState(GL_VERTEX_ARRAY);
            glVertexPointerf( self.points )
            glEnableClientState(GL_NORMAL_ARRAY);
            glNormalPointerf( self.normals )
            glDrawElementsui(GL_TRIANGLES, self.indices)
        except AttributeError:
            # a little hack to initialize points only once
            self.points=numpy.array([2.4,0,0,0,0,2,0,0,0,0,0,2,2.4,0,0,\
                2.4,0,2,0,0,2,0,-1.66,0,0,0,0,0,-1.66,0,2.4,0,0,0,0,0,\
                2.4,0,0,2.4,-1.66,2,2.4,0,2,2.4,-1.66,2,0,0,2,2.4,0,2,0,\
                -1.66,0,0,0,2,0,-1.66,2,2.4,0,0,0,-1.66,0,2.4,-1.66,0,\
                2.4,-1.66,2,2.4,0,0,2.4,-1.66,0,0,0,2,2.4,-1.66,2,0,\
                -1.66,2,2.4,-1.66,2,0,-1.66,0,0,-1.66,2,0,-1.66,0,2.4,
                -1.66,2,2.4,-1.66,0],'f').reshape(-1,3)

            self.normals=numpy.array([0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,\
                1,0,-1,0,0,-1,0,0,-1,0,0,0,0,-1,0,0,-1,0,0,-1,1,0,0,1,\
                0,0,1,0,0,0,0,1,0,0,1,0,0,1,-1,0,0,-1,0,0,-1,0,0,0,0,\
                -1,0,0,-1,0,0,-1,1,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,\
                0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0,0,-1,0 \
                ],'f').reshape(-1,3)

            self.indices=numpy.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,\
                14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,\
                32,33,34,35],'i')

    def loop(self):
        pygame.display.flip()
        pygame.event.pump()
        self.keys = dict((chr(i),int(v)) for i,v in \
            enumerate(pygame.key.get_pressed()) if i<256)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        return True

    def controls_3d(self,mouse_button=1,w_key='w',s_key='s',a_key='a',\
                        d_key='d', space_key=' '):
        """ The actual camera setting cycle """
        mouse_dx,mouse_dy = pygame.mouse.get_rel()
        if pygame.mouse.get_pressed()[mouse_button]:
            look_speed = .2
            buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
            c = (-1 * numpy.mat(buffer[:3,:3]) * \
                numpy.mat(buffer[3,:3]).T).reshape(3,1)
            # c is camera center in absolute coordinates, 
            # we need to move it back to (0,0,0) 
            # before rotating the camera
            ylevel = c[1]
            
            glTranslate(c[0],0,c[2])
            m = buffer.flatten()
            glRotate(mouse_dx * look_speed, m[1],m[5],m[9])
            glRotate(mouse_dy * look_speed, m[0],m[4],m[8])
            
            # compensate roll
            glRotated(-math.atan2(-m[4],m[5]) * \
                57.295779513082320876798154814105 ,m[2],m[6],m[10])
            glTranslate(-c[0], 0,-c[2])
        jump = -15.0 * (self.keys[space_key])

        if abs(jump) and (InAir == False):
            m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
            glTranslate(0, jump*m[2], 0)
            
        # move forward-back or right-left
        # fwd =   .1 if 'w' is pressed;   -0.1 if 's'
        fwd = .1 * (self.keys[w_key]-self.keys[s_key]) 
        strafe = .1 * (self.keys[a_key]-self.keys[d_key])
        if abs(fwd) or abs(strafe):
            m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
            glTranslate(fwd*m[2],0,fwd*m[10])
            glTranslate(strafe*m[0],0,strafe*m[8])


fps = Spectator(w = 640, h = 480, fov = 75)
fps.simple_lights()
fps.simple_camera_pose()



while fps.loop():
    ground()
    Cube()
   # tree()
    #fps.draw_simple_cube()
    fps.controls_3d(0,'w','s','a','d', ' ')
    buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
    c = (-1 * numpy.mat(buffer[:3,:3]) * \
        numpy.mat(buffer[3,:3]).T).reshape(3,1)
    if c[1] > GROUND_LEVEL:
        InAir = True
        glTranslate(0, 0.01, 0)
    if c[1] <= GROUND_LEVEL:
        InAir = False
    
 
    if fps.keys['q']: pygame.quit()
