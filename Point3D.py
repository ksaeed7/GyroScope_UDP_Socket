import sys, math, random


#Integrated class for 3D 
class Point3D:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x, self.y, self.z = float(x), float(y), float(z)
 
    """ Rotates the point around the X axis by the given angle in degrees. """
    def rotateX(self, angle):
        
        #determines radians
        rad = angle * math.pi / 180
        
        #cos of radians
        cosa = math.cos(rad)
        
        #sin of radians
        sina = math.sin(rad)
        
        #determine new y value
        y = self.y * cosa - self.z * sina
        
        #determine new z value
        z = self.y * sina + self.z * cosa
        
        #return Point3D (rotating around X axis, therefore no change in X value)
        return Point3D(self.x, y, z)
 
    """ Rotates the point around the Y axis by the given angle in degrees. """
    def rotateY(self, angle):
        
        #detemines radians
        rad = angle * math.pi / 180
        
        #cos of radians
        cosa = math.cos(rad)
        
        #sin of radians
        sina = math.sin(rad)
        
        #calculate new z value
        z = self.z * cosa - self.x * sina
        
        #calculate new x value
        x = self.z * sina + self.x * cosa
        
        #return Point3D (rotating around Y axis, therefore no change in Y value)
        return Point3D(x, self.y, z)
 
    """ Rotates the point around the Z axis by the given angle in degrees. """
    def rotateZ(self, angle):
        
        #determines radians
        rad = angle * math.pi / 180
        
        #cos of radians
        cosa = math.cos(rad)
        
        #sin of radians
        sina = math.sin(rad)
        
        #calculate new x value
        x = self.x * cosa - self.y * sina
        
        #calculate new y value
        y = self.x * sina + self.y * cosa
        
        #return Point3D (rotating around Z axis, therefore no change in Z value)
        return Point3D(x, y, self.z)
 
    """ Transforms this 3D point to 2D using a perspective projection. """
    def project(self, win_width, win_height, fov, viewer_distance):
        
        #factor using field of vision
        factor = fov / (viewer_distance + self.z)
        
        #x value
        x = self.x * factor + win_width / 2
        
        #y value
        y = -self.y * factor + win_height / 2
        
        #return Point3D (2D point, z=1)
        return Point3D(x, y, self.z)