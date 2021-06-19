from ev3robot import *
from math import *


class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

def addParts(robot, *parts):
    for part in parts:
        robot.addPart(part)

motorTicksPerRotation = 360
class ImprovedGear:
    def __init__(self, wheelRadius, robotDiameter, robot):
        self.wheelCircumference = wheelRadius * 2 * pi
        self.robotDiameter = robotDiameter
        self.rightMotor = Motor(MotorPort.B)
        self.leftMotor = Motor(MotorPort.A)
        addParts(robot, self.rightMotor, self.leftMotor)

    def forward(self, dist):
        self.rightMotor.resetMotorCount()
        self.leftMotor.resetMotorCount()
        self.leftMotor.forward()
        self.rightMotor.forward()
        desiredCount = (dist / self.wheelCircumference) * motorTicksPerRotation
        while self.rightMotor.getMotorCount() < desiredCount:
            pass
        self.rightMotor.stop()
        while self.rightMotor.getMotorCount() < desiredCount:
            pass
        self.leftMotor.stop()

    def forwardNonBlocking(self):
        self.rightMotor.forward()
        self.leftMotor.forward()

    def backward(self, dist):
        self.rightMotor.resetMotorCount()
        self.leftMotor.resetMotorCount()
        self.leftMotor.backward()
        self.rightMotor.backward()
        desiredCount = -(dist / self.wheelCircumference) * motorTicksPerRotation
        while self.rightMotor.getMotorCount() > desiredCount:
            pass
        self.rightMotor.stop()
        while self.leftMotor.getMotorCount() > desiredCount:
            pass
        self.leftMotor.stop()

    def left(self, deg):
        rad = (deg * 2 * pi) / 360.0
        self.rightMotor.resetMotorCount()
        self.leftMotor.resetMotorCount()
        self.leftMotor.backward()
        self.rightMotor.forward()
        desiredCount = ((rad * self.robotDiameter) / float(self.wheelCircumference * 2)) * motorTicksPerRotation / 3.0
        while self.rightMotor.getMotorCount() < desiredCount:
            pass
        self.rightMotor.stop()
        while self.leftMotor.getMotorCount() > -desiredCount:
            pass
        self.leftMotor.stop()

    def right(self, deg):
        rad = deg * 2 * pi / 360.0
        self.rightMotor.resetMotorCount()
        self.leftMotor.resetMotorCount()
        self.leftMotor.forward()
        self.rightMotor.backward()
        desiredCount = (rad * self.robotDiameter / (self.wheelCircumference * 2)) * motorTicksPerRotation / 3.0
        while self.rightMotor.getMotorCount() > -desiredCount:
            pass
        self.rightMotor.stop()
        while self.leftMotor.getMotorCount() < desiredCount:
            pass
        self.leftMotor.stop()


class Colors:
    yellow = "yellow"
    blue = "blue"
    black = "black"
    white = "white"

robot = LegoRobot()
colorSensor = ColorSensor(SensorPort.S2)
distanceSensor = UltrasonicSensor(SensorPort.S1)
gear = ImprovedGear(5.5 / 2.0, 29.8, robot)
addParts(robot, colorSensor, distanceSensor)


def driveAroundObject():
    gear.left(90.0)
    gear.forward(5.0)
    gear.right(90.0)

def getObjectColor(color):
    if color.blue >= 5:
        return Colors.white
    elif color.blue >= 2:
        return Colors.blue
    elif color.red >= 2:
        return Colors.yellow
    return Colors.black


def main():
    counter = 0
    while not robot.isEscapeHit():
        if distanceSensor.getDistance() <= 5:
            if getObjectColor(colorSensor.getColor()) == Colors.yellow:
                gear.forwar(6.0)
                gear.backward(2.0)
                gear.left(90.0)
                gear.forward(2.0)
                gear.left(90.0)
            else:
                if getObjectColor(colorSensor.getColor()) == Colors.black:
                    gear.forward(5.5)
                    counter += 1
                    gear.backward(2.0)
                driveAroundObject()
        gear.forwardNonBlocking()
        

if __name__ == "__main__":
    main()
    robot.exit()
