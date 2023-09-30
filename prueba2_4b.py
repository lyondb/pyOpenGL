from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *
import numpy as np

def circle_vertex_shader(radius, cx, cy, cz, num_segments):
    vertices = []
    kernel = [cx, cy, cz]
    for i in range(num_segments):
        theta = 2.0 * np.pi * float(i) / float(num_segments)
        x = radius * np.cos(theta)+kernel[0]
        y = radius * np.sin(theta)+kernel[1]
        z = 0.0+kernel[2]
        vertices.append([x, y, z])
    vertices.append(vertices[0])
    return np.array(vertices, dtype=np.float32)

# render two shapes
class Test(Base):

    def initialize(self):
        print("Initializing program...")
        ### initialize program ###
        vsCode = """ in vec3 position;
                    void main(){ gl_Position = vec4(position.x, position.y, position.z, 1.0); } """
        fsCode = """ out vec4 fragColor;
                    void main() {fragColor = vec4(1.0, 1.0, 0.0, 1.0); } """
        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)
        ### render settings ###
        glLineWidth(1)
        ### set up vertex array object - triangle ###
        self.vaoTri = glGenVertexArrays(1)
        glBindVertexArray(self.vaoTri)
        positionDataTri = [[-0.5, 0.8, 0.0], [-0.2, 0.2, 0.0], [-0.8, 0.2, 0.0]]
        self.vertexCountTri = len(positionDataTri)
        positionAttributeTri = Attribute("vec3",positionDataTri)
        positionAttributeTri.associateVariable( self.programRef, "position" )

        ### set up vertex array object - square ###
        self.vaoSquare = glGenVertexArrays(1)
        glBindVertexArray(self.vaoSquare)
        positionDataSquare = [[0.8, 0.8, 0.0], [0.8, 0.2, 0.0], [0.2, 0.2, 0.0], [0.2, 0.8, 0.0]]
        self.vertexCountSquare = len(positionDataSquare)
        positionAttributeSquare = Attribute("vec3", positionDataSquare)
        positionAttributeSquare.associateVariable(self.programRef, "position")

        self.vaoCircle = glGenVertexArrays(1)
        glBindVertexArray(self.vaoCircle)
        positionDataCircle = circle_vertex_shader(0.3, 0.5, -0.5, 0.0, 40)
        self.vertexCountCircle = len(positionDataCircle)
        positionAttributeCircle = Attribute("vec3", positionDataCircle)
        positionAttributeCircle.associateVariable(self.programRef, "position")


    def update(self):
        # using same program to render both shapes
        glUseProgram( self.programRef )
        # draw the triangle
        glBindVertexArray( self.vaoTri )
        glDrawArrays( GL_LINE_LOOP , 0 , self.vertexCountTri )
        # draw the square
        glBindVertexArray( self.vaoSquare )
        glDrawArrays( GL_LINE_LOOP , 0 , self.vertexCountSquare )
        glBindVertexArray(self.vaoCircle)
        glDrawArrays(GL_LINE_LOOP, 0, self.vertexCountCircle)

# instantiate this class and run the program
Test().run()