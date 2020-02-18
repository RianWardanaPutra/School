# Draws a polyhedron
# Controls: UP - rotate up
#           DOWN - rotate down
#           LEFT - rotate left
#           RIGHT - rotate right

# OpenGL imports for python
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GLUT import *
except:
    print ("Please install PyOpenGL & python-opengl")

class icosa:
    def __init__(self):
        self.rotate_y=0.0
        self.rotate_x=0.0
        self.scale=2.0

    def init(self):
        # Set background to black
        glClearColor(0.0, 0.0, 0.0, 0.0)

        #Enable depth sensing
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        # Set the shade model to flat
        glShadeModel(GL_SMOOTH)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.draw(True)

    def draw(self, mirror):
        # Set the color to cyan
        glColor3f(0.0,1.0,1.0)

        # Reset the matrix
        glLoadIdentity()

        # Set the camera
        gluLookAt(0.0,0.0,5.0,0.0,0.0,0.0,0.0,1.0,0.0)

        if mirror:
            glScalef(-self.scale, self.scale, self.scale)
            glRotatef(-self.rotate_y,0.0,1.0,0.0)
        else:
            glScalef(self.scale, self.scale, self.scale)
            glRotatef(self.rotate_y,0.0,1.0,0.0)

        glRotatef(self.rotate_x,1.0,0.0,0.0)

        # Draw solid polyhedron
        glutSolidIcosahedron()

        # Draw a white wire to highlight
        glColor3f(1.0,1.0,1.0)
        glutWireIcosahedron()
        glFlush()

    def reshape(self, w, h):
        glViewport(0, 0, GLsizei(w), GLsizei(h))
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
        glMatrixMode(GL_MODELVIEW)

    def control(self, key, x, y):
        if key==GLUT_KEY_RIGHT:
            self.rotate_y+=5
        if key==GLUT_KEY_LEFT:
            self.rotate_y-=5
        if key==GLUT_KEY_UP:
            self.rotate_x+=5
        if key==GLUT_KEY_DOWN:
            self.rotate_x-=5
        glutPostRedisplay()

def main():
    # Initialize OpenGL
    glutInit(sys.argv)

    # Set display mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

    # Set size and position of window size
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)

    # Create window with given title
    glutCreateWindow("Polyhedron")

    shape=icosa()
    shape.init()

    glutDisplayFunc(shape.display)
    glutReshapeFunc(shape.reshape)
    glutSpecialFunc(shape.control)
    glutMainLoop()

if __name__=='__main__':
    main()