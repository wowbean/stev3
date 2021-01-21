from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''
from pyPS4Controller.controller import Controller

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.



class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)
        
    def on_triangle_press(self):
        BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_C + BP.PORT_D, 100)
        print("Boop") 

    def on_triangle_release(self):
        BP.set_motor_power(BP.PORT_A + BP.PORT_B + BP.PORT_C + BP.PORT_D, 0)
        print("Beep")

    def on_up_arrow_press(self):
        BP.set_motor_power(BP.PORT_B + BP.PORT_C, 50)
        time.sleep(0.2)
        print("GO FORWARD")
        
    def on_down_arrow_press(self):
        BP.set_motor_power(BP.PORT_B + BP.PORT_C, -50)
        time.sleep(0.2)
        print("GO BACKWARD")

    def on_up_down_arrow_release(self):
        BP.set_motor_power(BP.PORT_B + BP.PORT_C, 0)
        time.sleep(0.2)
        print("STOP")

    def on_left_arrow_press(self):
        BP.set_motor_power(BP.PORT_B, 50)
        BP.set_motor_power(BP.PORT_C, -50)
        time.sleep(0.2)
        print("GO LEFT")
        
    def on_right_arrow_press(self):
        BP.set_motor_power(BP.PORT_B, -50)
        BP.set_motor_power(BP.PORT_C, 50)
        time.sleep(0.2)
        print("GO BACKWARD")

    def on_left_right_arrow_release(self):
        BP.set_motor_power(BP.PORT_B + BP.PORT_C, 0)
        time.sleep(0.2)
        print("STOP")


controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
controller.listen()
  