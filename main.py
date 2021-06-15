from ev3robot import *
from Gear import Gear

robot = LegoRobot()
gear = Gear(10, 5, 360)
odometry = Odometry(Vector(3))
distanceSensor = UltraSonicSensor(SensorPort.S1)
robot.addPart(gear)

while !robot.isEcapeHit():
    odometry.update(gear.getVelocityRight(),gear.getVelocityLeft())

