import time
from BrickPi import *
BrickPiSetup()
BrickPi.MotorEnable[PORT_A] = 1
BrickPi.MotorEnable[PORT_D] = 1
BrickPi.MotorEnable[PORT_B] = 1
BrickPiSetupSensors()



def forward():
     BrickPi.MotorSpeed[PORT_A] = 200
     BrickPi.MotorSpeed[PORT_D] = 200
     BrickPiUpdateValues()
     time.sleep(2)
     print("forward")

def backward():
    BrickPi.MotorSpeed[PORT_A] = -200
    BrickPi.MotorSpeed[PORT_D] = -200
    BrickPiUpdateValues()
    time.sleep(2)
    print("backward")

def turn_left()
    BrickPi.MotorSpeed[PORT_A] = -100
    BrickPi.MotorSpeed[PORT_D] = 100
    BrickPiUpdateValues()
    time.sleep(0.5)
    print("left")

def shoot():
    BrickPi.MotorSpeed[PORT_B] = 5
    BrickPiUpdateValues()
    time.sleep(0.5)
    print("shoot")

def wait:
    time.sleep(5)
    print("wait")

x = 0

left()
while x <= 3:
    forwards()
    shoot()
    backward()
    wait()
    x += 1
    
    
    











    
