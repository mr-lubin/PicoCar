from motor import Motor
from time import sleep


class Car:
    """Class for managing two wheel drive Pi Pico car"""

    def __init__(self, left, right):
        """Initialize left and right motors,
        set power to 100 and direction to forward.
        left and right arguments are tuples
        containing pairs of GPIO pin numbers"""
        self.left = Motor(left)
        self.right = Motor(right)

        self.power = 100
        self.going_forward = True

        self.stop()

    def drive(self, time=0):
        """Drive in current direction at specified power for specified time"""
        if self.going_forward:
            self.left.forward(self.power)
            self.right.forward(self.power)
        else:
            self.left.reverse(self.power)
            self.right.reverse(self.power)
        sleep(time)

    def turn_left(self, time=0):
        """Turn left for specified time"""
        if self.going_forward:
            self.left.forward(self.power * 0.5)
            self.right.forward(self.power * 0.8)
        else:
            self.left.reverse(self.power * 0.5)
            self.right.reverse(self.power * 0.8)
        sleep(time)

    def turn_right(self, time=0):
        """Turn left for specified time"""
        if self.going_forward:
            self.left.forward(self.power * 0.8)
            self.right.forward(self.power * 0.5)
        else:
            self.left.reverse(self.power * 0.8)
            self.right.reverse(self.power * 0.5)
        sleep(time)

    def spin_cw(self, time=0):
        """Rotate clockwise in place"""
        self.left.forward(self.power * 75)
        self.right.reverse(self.power * 75)
        sleep(time)

    def spin_countercw(self, time=0):
        """Rotate counterclockwise in place"""
        self.left.reverse(self.power * 75)
        self.right.forward(self.power * 75)
        sleep(time)

    def stop(self):
        """Stop car and wait one second"""
        self.left.stop()
        self.right.stop()
        sleep(1)

    def forward(self):
        """Set direction to forward"""
        self.going_forward = True

    def reverse(self):
        """Set direction to reverse"""
        self.going_forward = False

    def flip(self):
        """Toggle between forward and reverse"""
        self.going_forward = not self.going_forward

    def sleep(self, time=1):
        """Wait for a specified number of seconds"""
        sleep(time)
