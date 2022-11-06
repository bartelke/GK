#!/usr/bin/env python3
import sys
import math

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *
import random


def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def shutdown():
    pass


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


def render(time, tab, sqrtN, colorTab):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    spin(time * 180 / 3.1415)

    glColor3f(1.0, 0.9, 0.0)
    glBegin(GL_TRIANGLES)
    # for i in range(sqrtN*sqrtN):
    #     glVertex3f(tab[i][0], tab[i][1], tab[i][2])
    iterator = 0
    for i in range(sqrtN):
        u = i
        for j in range(sqrtN):
            v = j % sqrtN

            if (iterator < sqrtN*sqrtN):
                glColor3f(colorTab[iterator][0][0], colorTab[iterator]
                          [0][1], colorTab[iterator][0][2])
                iterator += 1
                glVertex3f(tab[i*sqrtN+j][0], tab[i*sqrtN+j]
                           [1], tab[i*sqrtN+j][2])

                glColor3f(colorTab[iterator][1][0], colorTab[iterator]
                          [1][1], colorTab[0][1][2])
                iterator += 1
                glVertex3f(tab[i*sqrtN+j+1][0], tab[i*sqrtN+j+1]
                           [1], tab[i*sqrtN+j+1][2])

                glColor3f(colorTab[iterator][2][0], colorTab[iterator]
                          [2][1], colorTab[iterator][2][2])
                iterator += 1
                glVertex3f(tab[(i+1)*sqrtN+j][0], tab[(i+1)*sqrtN+j]
                           [1], tab[(i+1)*sqrtN+j][2])
            else:
                iterator = 0
    glEnd()
    axes()

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
    N = 900
    sqrtN = int(math.sqrt(N))
    # tab = [[0] * 3 for i in range(N) for j in range(N)]
    tab = []

    # obliczanie X, Y, Z:
    for i in range(sqrtN+1):
        u = i/sqrtN
        for j in range(sqrtN):
            v = j/sqrtN
            #print("(", u, " ", v, ")")
            x = (-90*pow(u, 5) + 225*pow(u, 4) - 270*pow(u, 3) +
                 180*pow(u, 2) - 45*u)*math.cos(math.pi*v)
            y = (160*pow(u, 4) - 320*pow(u, 3) + 160*pow(u, 2) - 5)
            z = (-90*pow(u, 5) + 225*pow(u, 4) - 270*pow(u, 3) +
                 180*pow(u, 2) - 45*u)*math.sin(math.pi*v)

            point = []
            point.append(x)
            point.append(y)
            point.append(z)
            tab.append(point)

    # kolory:
    colorTab = []

    for i in range(sqrtN*(sqrtN+1)):
        triangleColors = []

        color1 = [random.uniform(0.0, 1.0), random.uniform(
            0.0, 1.0), random.uniform(0.0, 1.0)]
        color2 = [random.uniform(0.0, 1.0), random.uniform(
            0.0, 1.0), random.uniform(0.0, 1.0)]
        color3 = [random.uniform(0.0, 1.0), random.uniform(
            0.0, 1.0), random.uniform(0.0, 1.0)]

        triangleColors.append(color1)
        triangleColors.append(color2)
        triangleColors.append(color3)
        colorTab.append(triangleColors)

    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime(), tab, sqrtN, colorTab)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
