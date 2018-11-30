import math

class Vector3:
    x = 0
    y = 0
    z = 0

    #for setting values
    def setValues(self, x0, y0, z0):
        self.x = x0
        self.y = y0
        self.z = z0

        return True

    #for returning the magnitude of the vector
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    #for returning the normal of the given vector
    def normalize(self):
        x0 = self.x / self.magnitude()
        y0 = self.y / self.magnitude()
        z0 = self.z / self.magnitude()

        vec0 = Vector3()
        vec0.setValues(x0, y0, z0)
        
        return vec0

    #for printing the vector properly
    def info(self):
        print("[{0:.2f}".format(self.x) + ", {0:.2f}".format(self.y) + ", {0:.2f}".format(self.z) + "]", end = '')
        
        return True;

    #for returning the cross product of two vectors
    def cross(self, vec0):
        x0 = self.y * vec0.z - self.z * vec0.y
        y0 = self.z * vec0.x - self.x * vec0.z
        z0 = self.x * vec0.y - self.y * vec0.x

        vec1 = Vector3()
        vec1.setValues(x0, y0, z0)

        return vec1

    #for returning the dot product of two vectors, probably wont be used
    def dot(self, vec0):
        return (self.x * vec0.x + self.y * vec0.y + self.z * vec0.z)

    #for scalar multiplication of a vector
    def scalarMult(self, val0):
        x0 = self.x * val0
        y0 = self.y * val0
        z0 = self.z * val0

        vec0 = Vector3()
        vec0.setValues(x0, y0, z0)

        return vec0

    #for subtraction of two vectors
    def subtract(self, vec0):
        x0 = self.x - vec0.x
        y0 = self.y - vec0.y
        z0 = self.z - vec0.z

        vec1 = Vector3()
        vec1.setValues(x0, y0, z0)

        return vec1
    
    #for addition of two vectors
    def add(self, vec0):
        x0 = self.x + vec0.x
        y0 = self.y + vec0.y
        z0 = self.z + vec0.z

        vec1 = Vector3()
        vec1.setValues(x0, y0, z0)

        return vec1

    #for returning the magnitude of an angle between two vectors
    def angleMagnitude(self, vec0):
        cosTheta = self.dot(vec0) / (self.magnitude() * vec0.magnitude())

        return math.acos(cosTheta)

    #for returning the angle between a vector and a plane
    def anglePlane(self, vec0, norm):
        cosTheta = self.dot(vec0) / (self.magnitude() * vec0.magnitude())

        vec1 = Vector3()
        vec1 = norm.projection(vec0)

        val1 = math.acos(cosTheta)

        if(norm.x != 0):
            if(vec1.x / norm.x <0):
                val1 = - val1

        elif(norm.y != 0):
            if(vec1.y / norm.y <0):
                val1 = - val1

        elif(norm.z != 0):
            if(vec1.z / norm.z <0):
                val1 = - val1
                
        return val1

    #for returning a rotated vector around the y-axis
    def rotateAroundY(self, theta):
        x0 = self.x * math.cos(theta) + self.z * math.sin(theta)
        y0 = self.y
        z0 = -self.x * math.sin(theta) + self.z * math.cos(theta)

        vec0 = Vector3()
        vec0.setValues(x0, y0, z0)

        return vec0

    #for returning a rotated vector around the x-axis
    def rotateAroundX(self, theta):
        x0 = self.x
        y0 = self.y * math.cos(theta) - self.z * math.sin(theta)
        z0 = self.y * math.sin(theta) + self.z * math.cos(theta)

        vec0 = Vector3()
        vec0.setValues(x0, y0, z0)

        return vec0

    #for projecting a vector onto this
    def projection(self, vec0):
        val0 = self.dot(vec0) / (self.magnitude() ** 2)
        vec1 = Vector3()
        vec1 = self.scalarMult(val0)

        return vec1

#End of Vector3 Class

"""
a = Vector3()
a.setValues(10,20,30)
b = Vector3()
b.setValues(2,14,32.3)
print(a.cross(b).normalize().magnitude())
"""
