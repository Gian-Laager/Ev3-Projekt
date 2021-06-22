from ev3robot import *

robot = LegoRobot()

distanceSensor = UltrasonicSensor(SensorPort.S3)
robot.addPart(distanceSensor)

motor = Motor(MotorPort.C)
robot.addPart(motor)

buttonPos = 75
normalPos= 0
maxDist = 10
minDist = 3
tolerance = 2

motor.resetMotorCount()

#arduino like map function
def map(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

while not robot.isEscapeHit():
    if distanceSensor.getDistance() < maxDist:
        motor.rotateTo(map(distanceSensor.getDistance(), minDist, maxDist, buttonPos, normalPos) - motor.getMotorCount())
robot.exit()
        

