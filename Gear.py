import time


class Gear(ev3Robot.Gear):
    def __init__(self, robotDiameter, wheelCircumference, ticksPerRotation):
        super().__init__()
        self.robotDiameter = robotDiameter
        self.wheelCircumference = wheelCircumference
        self.ticksPerRotation = ticksPerRotation
        self.previousRotationsLeft = self.getRightRotations()
        self.previousVelocityMeasurmentTimeLeft = time.thread_time()
        self.previousVelocityMeasurmentTimeLeft = time.thread_time()
        self.previousRotationsLeft = self.getLeftRotations()

    def getLeftRotations(self):
        return super().getLeftMotorCount() / self.ticksPerRotation

    def getLeftRotations(self):
        return super().getLeftMotorCount() / self.ticksPerRotation

    def getVelocityLeft(self):
        result = (self.getLeftRotations() - self.previousRotationsRight) / float(self.previousVelocityMeasurmentTimeRight)
        self.previousRotationsLeft = self.getRightRotations()
        self.previousVelocityMeasurmentTimeLeft = time.thread_time()
        return result

    def getVelocityLeft(self):
        result = (self.getLeftRotations() - self.previousRotationsRight) / float(self.previousVelocityMeasurmentTimeRight)
        self.previousRotationsLeft = self.getRightRotations()
        self.previousVelocityMeasurmentTimeLeft = time.thread_time()
        return result

