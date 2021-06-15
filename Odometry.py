import math
import time

from Matrix import Matrix
from Vector import Vector


class Odometry():
    def __init__(self, robotDiameter, startPosition=Vector(3, [0, 0, 0])):
        self.robotDiameter = robotDiameter
        self.currentPosition = startPosition
        self.translationMatrix = Matrix(3, 3)
        self.timeOfPreviousMeasurment = time.thread_time()

    def getAngle(self):
        return self.currentPosition.values[2]

    def getPos(self):
        return Vector(2, self.currentPosition[:2])

    def update(self, velocityRight, velocityLeft):
        timeDelta = time.thread_time() - self.timeOfPreviousMeasurment
        angularVelocity = (velocityRight - velocityLeft) / self.robotDiameter
        rotationRadius = self.robotDiameter / 2 * (velocityRight + velocityLeft) / (velocityRight - velocityLeft)
        self.translationMatrix.set(0, 0, -math.cos(angularVelocity * timeDelta))
        self.translationMatrix.set(0, 1, -math.sin(angularVelocity * timeDelta))
        self.translationMatrix.set(1, 0, math.sin(angularVelocity * timeDelta))
        self.translationMatrix.set(1, 1, math.cos(angularVelocity * timeDelta))
        self.translationMatrix.set(0, 2, 0)
        self.translationMatrix.set(1, 2, 0)
        self.translationMatrix.set(2, 2, 1)
        self.translationMatrix.set(2, 0, 0)
        self.translationMatrix.set(2, 1, 0)

        magicVector = Vector(3)
        magicVector.set(0, angularVelocity * math.sin(self.currentPosition.values[2]))
        magicVector.set(1, -angularVelocity * math.cos(self.currentPosition.values[2]))
        magicVector.set(2, self.currentPosition.values[2])

        otherMagicVector = Vector(3)
        otherMagicVector.set(0, self.currentPosition.values[0] - rotationRadius * math.sin(
            self.currentPosition.values[2]))
        otherMagicVector.set(1, self.currentPosition.values[1] + rotationRadius * math.sin(
            self.currentPosition.values[2]))
        otherMagicVector.set(2, timeDelta * angularVelocity)

        self.currentPosition = self.translationMatrix * magicVector + otherMagicVector
        self.timeOfPreviousMeasurment = time.thread_time()
