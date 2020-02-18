#!/usr/bin/env python

######################
#  By: Rian Wardana  #
# 18/427592/PA/18552 #
######################
try:
    import pygame
    from pygame.locals import *

    from OpenGL.GL import *
    from OpenGL.GLU import *
    from math import pi, sqrt, sin, cos
except:
    print("Install pyOpenGL, pyGame, pyOpenGL_accelerate");

tetraVertices = (
    (1,1,1),
    (-1,1,-1),
    (-1,-1,1),
    (1,-1,-1)
)

tetraEdges = (
    (0,1),
    (0,2),
    (0,3),
    (1,2),
    (1,3),
    (2,3)
)

octaVertices = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1)
)

octaEdges = (
    (0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5)
)

cubeVertices = (
    (-1,-1,-1),
    (1,-1,-1),
    (1,-1,1),
    (-1,-1,1),
    (-1,1,-1),
    (1,1,-1),
    (1,1,1),
    (-1,1,1)
)

cubeEdges = (
    (0,1),
    (0,3),
    (0,4),
    (1,2),
    (1,5),
    (2,3),
    (2,6),
    (3,7),
    (4,5),
    (4,7),
    (5,6),
    (6,7)
)
phi = (1+sqrt(5))/2
a = 1
b = 1/(phi)
isocaVertices = (
    ( 0,  a,  b), 
    ( 0,  a, -b), 
    ( 0, -a, -b), 
    ( 0, -a,  b), 
    ( b,  0,  a), 
    ( b,  0, -a), 
    (-b,  0, -a), 
    (-b,  0,  a), 
    ( a,  b, 0), 
    ( a, -b, 0), 
    (-a, -b, 0),
    (-a,  b, 0)
    )

isocaEdges = (
    (0, 1),
    (0, 4),
    (0, 7),
    (0, 8),
    (0, 11),
    (2, 3),
    (1, 5),
    (1, 6),
    (1, 8),
    (1, 11),
    (2, 5),
    (2, 6),
    (2, 9),
    (2, 10),
    (3, 4),
    (3, 7),
    (3, 9),
    (3, 10),
    (4, 7),
    (4, 8),
    (4, 9),
    (5, 6),
    (5, 8),
    (5, 9),
    (6, 10),
    (6, 11),
    (7, 10),
    (7, 11),
    (8, 9),
    (10, 11)
)

def Tetra():
    glBegin(GL_LINES)
    for edge in tetraEdges:
        for vertex in edge:
            glVertex3fv(tetraVertices[vertex])
    glEnd()

def Cube():
    glBegin(GL_LINES)
    for edge in cubeEdges:
        for vertex in edge:
            glVertex3fv(cubeVertices[vertex])
    glEnd()

def Octa():
    glBegin(GL_LINES)
    for edge in octaEdges:
        for vertex in edge:
            glVertex3fv(octaVertices[vertex])
    glEnd()

def Isoca():
    glBegin(GL_LINES)
    for edge in isocaEdges:
        for vertex in edge:
            glVertex3fv(isocaVertices[vertex])
    glEnd()



def main():
    print("List of available platonic solid object:\n1. Tetrahedron\n"
        + "2. Octahedron\n3. Hexahedron(cube)\n4. Isocahedron\n")
    choice = input("Input platonic solids number:\n")
    while True:
        try:
            choice = int(choice)
            break
        except:
            choice = input("Input option's number!: ")
    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslate(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 2, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        if choice == 1 or choice == '1':
            Tetra()
        elif choice == 2 or choice == '2':
            Octa()
        elif choice == 3 or choice == '3':
            Cube()
        elif choice == 4 or choice == '4':
            Isoca()
        else:
            print("Option number invalid")
            return
        pygame.display.flip()
        pygame.time.wait(5)

if __name__ == "__main__":
    main()