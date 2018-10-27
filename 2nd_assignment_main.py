#########################################################################
# Date: 2018/10/02
# file name: 2nd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 2ND_ASSIGNMENT_CODE
    # Complete the code to perform Second Assignment
    # =======================================================================
    def car_startup(self):
        control = self.car.steering
        control.center_alignment

        variation = self.car.accelerator
        variation.ready()

        blacksensor = self.car.line_detector

        variation.go_forward(30)
        if blacksensor.is_center():
            variation.go_forward(40)
            time.sleep(0.1)
            variation.go_forward(30)
        if blacksensor.is_equal_status([1,0,0,0,0]):
            control.turn_left(35)
            time.sleep(0.1)
            control.center_alignment
        elif blacksensor.is_equal_status([1,1,0,0,0]):
            control.turn_left(30)
            time.sleep(0.1)
            control.center_alignment
        elif blacksensor.is_equal_status([0,1,0,0,0]):
            control.turn_left(10)
            time.sleep(0.1)
            control.center_alignment
        elif blacksensor.is_equal_status([0,1,1,0,0]):
            control.turn_left(5)
            time.sleep(0.1)
            control.center_alignment
        elif blacksensor.is_equal_status([0,0,1,1,0])
            control.turn_right(5)
            time.sleep(0.1)
            control.center_alignment
        elif blacksensor.is_equal_status([0,0,0,1,0]):
            control.turn_right(10)
            time.sleep(0.1)
            control.center_alignment
        elif blacksensor.is_equal_status([0,0,0,1,1]):
            control.turn_right(30)
            time.sleep(0.1)
            control.center_alignment
        elif blacksensor.is_equal_status([0,0,0,0,1]):
            control.turn_right(35)
            time.sleep(0.1)
            control.center_alignment
        # implement the assignment code here
        pass


if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
