from machine import Pin, PWM


class Motor:
    """Class for managing motors of Pi Pico car"""

    def __init__(self, pins, MAX=62025, MIN=0):
        """Initialize motor pins"""
        # Set max and min PWM duty cycles
        self.MAX = int(MAX)
        self.MIN = int(MIN)
        # Initialize GPIO/PWM pins for motor
        self.a = PWM(Pin(pins[0]), freq=5000, duty_u16=self.MIN)
        self.b = PWM(Pin(pins[1]), freq=5000, duty_u16=self.MIN)

    def stop(self):
        """Stop motor"""
        self.a.duty_u16(self.MIN)
        self.b.duty_u16(self.MIN)

    def forward(self, power=100):
        """Set motor to run at specified power"""
        self.a.duty_u16(self._validate(power))
        self.b.duty_u16(self.MIN)

    def reverse(self, power=100):
        """Set motor to run in reverse at specified power"""
        self.a.duty_u16(self.MIN)
        self.b.duty_u16(self._validate(power))

    def _validate(self, power):
        """Validate input and normalize to an int value in
        the upper half of the range between MIN and MAX duty."""
        if power <= 0:
            return self.MIN
        elif power >= 100:
            return self.MAX
        else:
            return int((self.MAX - self.MIN) * ((power/200) + 0.5)) + self.MIN
