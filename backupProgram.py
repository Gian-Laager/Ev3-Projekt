from ev3robot import *

robot = LegoRobot()
lightSensor = LightSensor(SensorPort.S2)
distanceSensor = UltrasonicSensor(SensorPort.S1)
gear = Gear()
robot.addPart(lightSensor)
robot.addPart(distanceSensor)
robot.addPart(gear)
black = 100
yellow = (100, 200)
counter = 0
rotation90Deg = 2500


def driveAroundObject():
    gear.left(rotation90Deg)
    gear.forward(2000)
    gear.right(rotation90Deg)


while !robot.isEscapeHit():
    if distanceSensor.getDistance() <= 5:
        if lightSensor.getValue() > yellow[0] and lightSensor.getValue() < yellow[1]:
            gear.backward(2000)
            gear.left(rotation90Deg)
            gear.forward(2000)
            gear.left(rotation90Deg)
        else:
            if lightSensor.getValue < black:
                gear.forward(2000)
                counter += 1
                gear.backward(2000)
            driveAroundObject()
    gear.forward()
