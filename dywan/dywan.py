#!/usr/bin/env python3
import sys
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

val = random.random()

def startup():
    update_viewport(None, 400, 400)
    glClearColor(0.3, 0.3, 0.3, 1.0)

def shutdown():
    pass

def render(time):
    glClear(GL_COLOR_BUFFER_BIT)
    random.seed(val)
    q = random.random()     
    w = random.random()
    e = random.random()
    glColor3f(q, w, e)

    dywanik(0,0,100,80,5)

    glFlush()

def dywanik(poz_x, poz_y, a, b, stopien):
    # idea jest taka, ze dzielimy prostakat na 9 pol (3x3)
    # i w 8 z tych pol rekurencyjnie robimy to samo (z wylaczeniem srodka ktory chcemy wyciac)

    if stopien != 0:
        # dopoki nie osiagniemy warunku bazowego (stopien=0) dzielimy prostokat:
        stopien = stopien-1  
        nowe_a = a/3
        nowe_b = b/3

        # w kazdym polu 3x3 z wyjatkiem srodka wykonujemy rekurencje:
        for i in range(3):
            for j in range(3):
                if i!=1 or j!=1: # srodkowe pole ma indeks [i=1,j=1] wiec je pomijamy
                    nowy_y = poz_y - nowe_b + j * nowe_b
                    nowy_x = poz_x - nowe_a + i * nowe_a
                    dywanik(nowy_x, nowy_y, nowe_a, nowe_b, stopien)
    else:
        # warunek bazowy i rysowanie: 
        glColor3f(0.0,0.5,0.5)
        glBegin(GL_QUADS)
        glVertex2f(poz_x, poz_y)
        glVertex2f(poz_x+a, poz_y)
        glVertex2f(poz_x+a, poz_y+b)
        glVertex2f(poz_x, poz_y+b)
        glEnd()      


def update_viewport(window, width, height):
    if height == 0:
        height = 1
    if width == 0:
        width = 1
    aspectRatio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspectRatio, 100.0 / aspectRatio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspectRatio, 100.0 * aspectRatio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
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
        render(glfwGetTime())
        glfwSwapBuffers(window)
        #glfwSwapInterval(40)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main() 