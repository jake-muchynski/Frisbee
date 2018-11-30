import math
import Vector3Class as Vector3

class Plane:
    a = 0
    b = 0
    c = 0
    d = 0
    #in the form of ax + by + cz = d

    #for setting values of a plane
    def setValues(self, a0, b0, c0, d0):
        self.a = a0
        self.b = b0
        self.c = c0
        self.d = d0

        return True

    #for making the plane with a normal and position vector
    def makeWithTwoVectors(self, norm, pos):
        self.a = norm.x
        self.b = norm.y
        self.c = norm.z
        self.d = norm.x * pos.x + norm.y * pos.y + norm.z * pos.z

        return True

    #for returning the normal vector of a plane
    def normal(self):
        x0 = self.a
        y0 = self.b
        z0 = self.c
    
        vec0 = Vector3.Vector3()
        vec0.setValues(x0, y0, z0)

        return vec0

    #for projecting a vector onto the plane
    def projectVector(self, vec0):
        normVector = Vector3.Vector3()
        normVector = self.normal()

        val1 = (vec0.dot(normVector)) / (normVector.magnitude()) ** 2
        vec1 = Vector3.Vector3()
        vec1 = vec0.subtract(normVector.scalarMult(val1))

        return vec1

#End of Plane Class
