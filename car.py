from motor import Motor
from time import sleep


class Car:
    """Class for managing two wheel drive Pi Pico car"""

    def __init__(self, left, right):
        """Initialize left and right motors, set direction to forward"""
        """left and right are tuples containing pairs of GPIO pin numbers"""
        self.left = Motor(left)
        self.right = Motor(right)

        self.forward = True

        self.stop()

    def drive(self, power=100, time=0):
        """Drive in current direction at specified power for specified time"""
        if self.forward:
            self.left.forward(power)
            self.right.forward(power)
        else:
            self.left.reverse(power)
            self.right.reverse(power)
        sleep(time)

    def turn_left(self, time=0):
        """Turn left for specified time"""
        if self.forward:
            self.left.forward(50)
            self.right.forward(80)
        else:
            self.left.reverse(50)
            self.right.reverse(80)
        sleep(time)

    def stop(self):
        """Stop car and wait one second"""
        self.left.stop()
        self.right.stop()
        sleep(1)

    def flip(self):
        """Toggle between forward and reverse"""
        self.forward = not self.forward

    def sleep(self, time=1):
        """Wait for a specified number of seconds"""
        sleep(time)
