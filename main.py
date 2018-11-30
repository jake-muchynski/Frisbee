import Vector3Class as Vector3
import PlaneClass as Plane
import math
import numpy

import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D

#========Initializing Vectors and Planes==========
initialPosition = Vector3.Vector3()
currentPosition = Vector3.Vector3()
initialVelocity = Vector3.Vector3()
currentVelocity = Vector3.Vector3()
currentAcceleration = Vector3.Vector3()
sumOfForces = Vector3.Vector3()
dragForce = Vector3.Vector3()
liftForce = Vector3.Vector3()
gravityVector = Vector3.Vector3()
gravitationalForce = Vector3.Vector3()
frisbeeNormal = Vector3.Vector3()
groundPlane = Plane.Plane()
frisbeePlane = Plane.Plane()
#=================================================

#============Initializing Other===================
airDensity = 1.23 #UNITS: kg/m^3

timeMax = 3 * 60 #UNITS: seconds
deltaTime = 0.001 #UNITS: seconds
loopCycles = int(timeMax / deltaTime)

radius = 0.135 #UNITS: m
area = numpy.pi * radius ** 2 #UNITS: m^2

mass = 0.175 #UNITS: kg

formLiftCoefficient = 0.33
inducedLiftCoefficient = 1.91
liftCoefficient = 0.0

formDragCoefficient = 0.18
inducedDragCoefficient = 0.69
dragCoefficient = 0.0

idealAngle = (-4 * numpy.pi) / 180 #UNITS: radians

gravityVector.setValues(0, 0, -9.81)
groundPlane.setValues(0, 0, 1, 0)
frisbeePlane.setValues(0, 0, 1, 0)

frisbeeNormal.setValues(0, 0, 1)

tiltAngleY = 0
tiltAngleX = 0

dragMagnitude = 0.0
liftMagnitude = 0.0
angleOfAttack = 0.0

tArr = []
xPosArr = []
yPosArr = []
zPosArr = []
velArr = []

smallestx = 0
smallesty = 0
smallestz = 0
smallestxArr = []
smallestyArr = []
smallestzArr = []

userInput = ['', 0.0, 0.0, 0.0]
#=================================================

print("\nHello TRON Class 2022! Welcome to Frisbee Simulator 2018!\n"
      + "Written by: Andrew Daly, Julia Garbe and Jake Muchynski\n\n"
      + "If you would like to use default values, enter 'd'\n"
      + "If you would like to create a custom simultaion, enter 'c'\n\n"
      + "Here are the default values (vector notation [x, y, z]:\n\n"
      + "Initial Velocity Direction: [0.707, 0.707, 0] (0 degrees above y axis)\n"
      + "Initial Velocity Magnitude: 14 m/s\n"
      + "Initial Position: 1m above the origin\n"
      + "Mass: 0.175 kg\n"
      + "Tilt angle above y-axis: 0 degrees\n"
      + "Tilt angle above x-axis: 0 degrees\n")

while True:
    userInput[0] = input("> ")
    
    if(userInput[0] == "D" or userInput[0] == "d"):
        initialVelocity.setValues(1,1,0)
        initialVelocity = initialVelocity.normalize()
        initialVelocity = initialVelocity.scalarMult(14)
        
        initialPosition.setValues(0,0,1)
        print ("Default choices selected.")
        break

    elif(userInput[0] == "C" or userInput[0] == "c"):
        print ("Custom choices selected.\n")
        userInput[0] = input("Enter Initial Velocity Direction x:\n> ")
        userInput[1] = float(userInput[0])
        userInput[0] = input("\nEnter Initial Velocity Direction y:\n> ")
        userInput[2] = float(userInput[0])
        userInput[0] = input("\nEnter Initial Velocity Direction z:\n> ")
        userInput[3] = float(userInput[0])

        initialVelocity.setValues(userInput[1],userInput[2],userInput[3])
        initialVelocity = initialVelocity.normalize()

        userInput[0] = input("\nEnter Initial Velocity Magnitude (m/s):\n> ")
        userInput[1] = float(userInput[0])
        
        initialVelocity = initialVelocity.scalarMult(userInput[1])

        print("Initial Velocity Vector: ", end = '')
        initialVelocity.info()
        print(" ({0:.2f}".format((groundPlane.projectVector(initialVelocity).anglePlane(initialVelocity, groundPlane.normal())
                         * 180) / numpy.pi) + " degrees above ground Plane)")

        userInput[0] = input("\nEnter Initial Position Height:\n> ")
        userInput[1] = float(userInput[0])

        initialPosition.setValues(0, 0, userInput[1])

        userInput[0] = input("\nEnter Mass:\n> ")
        userInput[1] = float(userInput[0])

        mass = userInput[1]

        userInput[0] = input("\nEnter Tilt Angle Above y-axis (degrees):\n> ")
        userInput[1] = float(userInput[0])

        frisbeeNormal = frisbeeNormal.rotateAroundY((userInput[1] * numpy.pi) / 180)

        userInput[0] = input("\nEnter Tilt Angle Above x-axis (degrees):\n> ")
        userInput[2] = float(userInput[0])

        frisbeeNormal = frisbeeNormal.rotateAroundX((userInput[2] * numpy.pi) / 180)
        frisbeeNormal = frisbeeNormal.normalize()
        frisbeePlane.makeWithTwoVectors(frisbeeNormal, initialPosition)
        
        print("\nCUSTOM SETTINGS:\n")
        print("Initial Velocity Vector: ", end = '')
        initialVelocity.info()
        print(" ({0:.2f}".format((groundPlane.projectVector(initialVelocity).anglePlane(initialVelocity, groundPlane.normal())
                         * 180) / numpy.pi) + " degrees above ground Plane)")
        print("Initial Position Vector: ", end = '')
        initialPosition.info()
        print("\nMass: " + str(mass))
        print("Tilt angle above y-axis: " + str(userInput[1]))
        print("Tile angle aboce x-axis: " + str(userInput[2]))
        
        break

    else:
        print ("Please enter a valid command.\n")
        
print ("\nTo begin Frisbee Simulator 2018 type 's'")

while True:
    userInput[0] = input("> ")
    
    if(userInput[0] == "S" or userInput[0] == "s"):
        break

    else:
        print ("Please enter a valid command.\n")

#BEEF TIME

currentVelocity = initialVelocity
currentPosition = initialPosition

for i in range(loopCycles):
    frisbeePlane.makeWithTwoVectors(frisbeeNormal, currentPosition)
    
    angleOfAttack = -frisbeePlane.projectVector(currentVelocity).anglePlane(currentVelocity, frisbeeNormal)
    
    dragCoefficient = formDragCoefficient + inducedDragCoefficient*(angleOfAttack - idealAngle)**2
    dragMagnitude = (1/2)*(airDensity)*(currentVelocity.magnitude()**2)*(area)*(dragCoefficient)
    dragForce = currentVelocity.normalize().scalarMult(-dragMagnitude)

    liftCoefficient = formLiftCoefficient + inducedLiftCoefficient*(angleOfAttack)
    liftMagnitude = (1/2)*(airDensity)*(currentVelocity.magnitude()**2)*(area)*(liftCoefficient)
    liftForce = (frisbeeNormal.normalize()).scalarMult(liftMagnitude)

    gravitationalForce = gravityVector.scalarMult(mass)
    
    sumOfForces = gravitationalForce.add(liftForce).add(dragForce)
    currentAcceleration = sumOfForces.scalarMult(1/mass)

    currentVelocity = currentVelocity.add(currentAcceleration.scalarMult(deltaTime))
    currentPosition = currentPosition.add(currentVelocity.scalarMult(deltaTime))

    tArr.append(float(i)/1000)
    xPosArr.append(currentPosition.x)
    yPosArr.append(currentPosition.y)
    zPosArr.append(currentPosition.z)
    velArr.append(currentVelocity.magnitude())

    if(xPosArr[i] < smallestx):
        smallestx = xPosArr[i]

    if(yPosArr[i] < smallesty):
        smallesty = yPosArr[i]

    if(zPosArr[i] < smallestz):
        smallestz = zPosArr[i]

    if (currentPosition.z <=0):
        break
    
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
ax.set_xlabel('X Distance (m)')
ax.set_ylabel('Y Distance (m)')
ax.set_zlabel('Z Distance (m)')

for i in range(len(tArr)):
    smallestxArr.append(smallestx)
    smallestyArr.append(smallesty)
    smallestzArr.append(smallestz)
    
ax.plot(xPosArr, yPosArr, smallestzArr, color = 'gray')
ax.plot(xPosArr, smallestyArr, zPosArr, color = 'gray')
ax.plot(smallestxArr, yPosArr, zPosArr, color = 'gray')
scatterx = [initialPosition.x]
scattery = [initialPosition.y]
scatterz = [initialPosition.z]
ax.scatter(scatterx, scattery, scatterz, label='Initial Position', color = 'blue')
ax.plot(xPosArr, yPosArr, zPosArr, label='Frisbee Path', color='purple')
ax.legend()

x1 = numpy.linspace(0.0, 5.0)
x2 = numpy.linspace(0.0, 2.0)

y1 = numpy.cos(2 * numpy.pi * x1) * numpy.exp(-x1)
y2 = numpy.cos(2 * numpy.pi * x2)

plt.subplot(1, 2, 2)
plt.plot(tArr, velArr)
plt.title('Velocity')
plt.ylabel('Velocity (m/s)')
plt.xlabel('Time(s)')

plt.show()
