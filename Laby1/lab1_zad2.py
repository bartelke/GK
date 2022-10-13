#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *


def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time, x, y, a, b):
    glClear(GL_COLOR_BUFFER_BIT)

    # first triangle:
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x, y)
    glVertex2f(x+a, y)
    glVertex2f(x, y+b)
    glEnd()

    # second triangle:
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x+a, y)
    glVertex2f(x+a, y+b)
    glVertex2f(x, y+b)
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
    # x = input("Enter x value: ")
    # y = input("Enter y value: ")
    # a = input("Enter length of one side: ")
    # b = input("Enter length of the second side: ")
    # print("Generating figure in (" + x + ", " + y + "), size: " +
    #       b + " x " + a + " x " + b + " x " + a)

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
        render(glfwGetTime(), 0, 0, 50, 20)
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()