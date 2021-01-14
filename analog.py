from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''
from pyPS4Controller.controller import Controller
​
from math import log
import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers
​
BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.
​
​LOG_VAL = 0.442
​LOG_VAL_2 = 0.3

class MyController(Controller):
​
    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
    def update(self): # somehow convert a number from -32000 - 32000
        k1 = self.x ** LOG_VAL_2
        if self.x >= 0:
            k2 = k1
            k1 = 0
        else:
            k2 = 0
        BP.set_motor_power(BP.PORT_B, (self.y **​ LOG_VAL) - k1)
        BP.set_motor_power(BP.PORT_C, (self.y **​ LOG_VAL) - k2)
        
    def on_L3_up(self, value):
        self.y = value
        self.update()
​
    def on_L3_down(self, value):
        self.y = value
        self.update()

    def on_L3_down(self, value):
        self.x = value
        self.update()
​
    def on_L3_up(self, value):
        self.x = value
        self.update()
        
    def on_L3_x_at_rest(self):
        self.x = 0
    
    def on_L3_y_at_rest(self):
        self.y = 0

​​
controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
