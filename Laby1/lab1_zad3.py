#!/usr/bin/env python3
import sys
import random

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time, x, y, a, b, d, color1, color2, color3, color4):
    glClear(GL_COLOR_BUFFER_BIT)

    # first triangle:
    glBegin(GL_TRIANGLES)
    glColor3f(color1[0], color1[1], color1[2])
    glVertex2f(x, y)
    glColor3f(color2[0], color2[1], color2[2])
    glVertex2f(d*(x+a), y)
    glColor3f(color4[0], color4[1], color4[2])
    glVertex2f(x, d*(y+b))
    glEnd()

    # second triangle:
    glBegin(GL_TRIANGLES)
    glColor3f(color2[0], color2[1], color2[2])
    glVertex2f(d*(x+a), y)
    glColor3f(color3[0], color3[1], color3[2])
    glVertex2f(d*(x+a), d*(y+b))
    glColor3f(color4[0], color4[1], color4[2])
    glVertex2f(x, d*(y+b))
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
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    color1 = [random.uniform(0.0, 1.0), random.uniform(
        0.0, 1.0), random.uniform(0.0, 1.0)]
    color2 = [random.uniform(0.0, 1.0), random.uniform(
        0.0, 1.0), random.uniform(0.0, 1.0)]
    color3 = [random.uniform(0.0, 1.0), random.uniform(
        0.0, 1.0), random.uniform(0.0, 1.0)]
    color4 = [random.uniform(0.0, 1.0), random.uniform(
        0.0, 1.0), random.uniform(0.0, 1.0)]

    print(color1)

    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    a = int(input("Enter length of one side: "))
    b = int(input("Enter length of the second side: "))
    d = int(input("Enter deformation variable: "))
    print("Generating figure...")

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
        render(glfwGetTime(), x, y, a, b, d, color1, color2, color3, color4)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()
