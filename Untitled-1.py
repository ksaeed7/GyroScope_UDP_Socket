
from pygame.locals import K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE
from operator import itemgetter
import numpy as np
from time import sleep
import Point3D

class Simulation:
    
    """ init """
    def __init__(self, win_width = 640, win_height = 480):
        
        pygame.init()
 
        #set screen to certain width and height
        self.screen = pygame.display.set_mode((win_width, win_height))
        self.origColor = [255,0,0]
        #set caption
        pygame.display.set_caption("3D Cube Rotation using Gyroscope")
 
        #system clock time
        self.clock = pygame.time.Clock()
 
        #create box vertices
        self.vertices = [
            Point3D(-1,1,-1),
            Point3D(1,1,-1),
            Point3D(1,-1,-1),
            Point3D(-1,-1,-1),
            Point3D(-1,1,1),
            Point3D(1,1,1),
            Point3D(1,-1,1),
            Point3D(-1,-1,1)
        ]
        
        #Faces correspond to 4 Point3Ds
        self.faces  = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]

        # Define colors for each face
        self.colors = [(255,0,255),(255,0,0),(0,255,0),(0,0,255),(0,255,255),(255,255,0)]
        #Updated values based on gyroscope
        self.angleX, self.angleY, self.angleZ = 0, 0, 0
        
    """ Rotates the cube in the given direction """
    def rotate(self, direction):
        
        # It will hold transformed vertices.
        tVertices = []
        
        for vertex in self.vertices:
            # Rotate the point around X axis, then around Y axis, and finally around Z axis.
            rotation = vertex.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
            # Transform the point from 3D to 2D
            projection = rotation.project(self.screen.get_width(), self.screen.get_height(), 256, 4)
            # Put the point in the list of transformed vertices
            tVertices.append(projection)

        # Calculate the average Z values of each face.
        avgZ = []
        
        for i, f in enumerate(self.faces):
            z = (tVertices[f[0]].z + tVertices[f[1]].z + tVertices[f[2]].z + tVertices[f[3]].z) / 4.0
            avgZ.append([i,z])
            i = i + 1

        #Sort the "z" values in reverse and display the foremost faces last
        for face in sorted(avgZ,key=itemgetter(1),reverse=True):
            fIndex = face[0]
            f = self.faces[fIndex]
            pointList = [(tVertices[f[0]].x, tVertices[f[0]].y), (tVertices[f[1]].x, tVertices[f[1]].y),
                         (tVertices[f[1]].x, tVertices[f[1]].y), (tVertices[f[2]].x, tVertices[f[2]].y),
                         (tVertices[f[2]].x, tVertices[f[2]].y), (tVertices[f[3]].x, tVertices[f[3]].y),
                         (tVertices[f[3]].x, tVertices[f[3]].y), (tVertices[f[0]].x, tVertices[f[0]].y)]
            pygame.draw.polygon(self.screen,self.colors[fIndex],pointList)
 
 
        #updates display surface to screen
        pygame.display.flip()
 
 
    
    def colorFade(self, origColor1, fadeInColor):
        #check background color status
        if (self.origColor[0] != fadeInColor[0]):
            if (self.origColor[0] < fadeInColor[0]):
                self.origColor[0]+= 1
            else:
                self.origColor[0]-= 1
        
        if (self.origColor[1] != fadeInColor[1]):
            if (self.origColor[1] < fadeInColor[1]):
                self.origColor[1]+= 1
            else:
                self.origColor[1]-= 1
                
        if (self.origColor[2] != fadeInColor[2]):
            if (self.origColor[2] < fadeInColor[2]):
                self.origColor[2]+= 1
            else:
                self.origColor[2]-= 1
            
        #origColor = [0,0,0]
        #update background color
        self.screen.fill(self.origColor)
 
    
    def update(self, sensor_data):
        # Adjust these values based on your sensor's scaling factors
        self.angleX += sensor_data["xG"]
        self.angleY += sensor_data["yG"]
        self.angleZ += sensor_data["zG"]
        self.rotate()         

if __name__ == "__main__":
    Simulation().run()