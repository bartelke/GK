#!/usr/bin/env python3
from cmath import cos, pi, sin
import math
import sys
import numpy
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 1920, 1080)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 1.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()


def setColors(tab):
    end = len(tab)
    for i in range(0, end):
        for j in range(0, end):
            # red 0
            tab[i][j][0] = random.random()
            # green 1
            tab[i][j][1] = random.random()
            # blue 2
            tab[i][j][2] = random.random()
    return tab


def render(tab, colours, time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 60 / 3.1415)
    axes()

    # Generowanie jaja:
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(len(tab)-1):
        for j in range(len(tab[i])):
            glColor3f(colours[i][j][0], colours[i][j][1], colours[i][j][2])
            glVertex3f(tab[i][j][0], tab[i][j][1], tab[i][j][2])

            glColor3f(colours[i+1][j][0], colours[i+1]
                      [j][1], colours[i+1][j][2])
            glVertex3f(tab[i+1][j][0], tab[i+1][j][1], tab[i+1][j][2])
    glEnd()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 7.5, -7.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 7.5, -7.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    n = 35

    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(1920, 1080, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    colours = setColors(numpy.zeros((n, n, 3)))

    tab = numpy.zeros((n, n, 3))

    for i in range(0, n):
        for j in range(0, n):
            u = i/(n-1)
            v = j/(n-1)
            # wsp X:
            tab[i][j][0] = ((-90*pow(u, 5))+(225*pow(u, 4)) -
                            (270*pow(u, 3))+(180*pow(u, 2))-(45*u)) * math.cos(pi*v)
            # wsp Y:
            tab[i][j][1] = (160*pow(u, 4))-(320*pow(u, 3))+(160*pow(u, 2))-5
            # wsp Z:
            tab[i][j][2] = ((-90*pow(u, 5))+(225*pow(u, 4)) -
                            (270*pow(u, 3))+(180*pow(u, 2))-(45*u))*math.sin(pi*v)

    startup()
    while not glfwWindowShouldClose(window):
        render(tab, colours, glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
