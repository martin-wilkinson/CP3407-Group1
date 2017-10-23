class Pump:
    current = 0
    previous = 5

    HIGH = 7
    MID = 5
    LOW = 3

    def main(self):
        pass

    def getRate(self):
        # I want this to get current reading from the server
        pass

    def sugarLow(self):
        pass

    def calculate(self):
        if self.getRate() > 0:                         # Checking if Sugar Level (SL) rising
            if self.current > self.HIGH:
                print('UNSAFE')
            elif self.current > self.MID:
                print('Safe, but high')
            elif self.current > self.LOW:
                print('Safe, but low')
            elif self.current < self.LOW:
                print('Not good ,eat!')

        elif self.getRate() < 0:                         # Checking if Sugar Level (SL) falling
            if self.current > self.HIGH:
                print('UNSAFE')
            elif self.current > self.MID:
                print('Safe, but high')
            elif self.current > self.LOW:
                print('Safe, but low')
            elif self.current < self.LOW:
                print('Not good ,eat!')

        elif self.getRate() == 0:
            if self.current > self.HIGH:
                print('UNSAFE')
            elif self.current > self.MID:
                print('Safe, but high')
            elif self.current > self.LOW:
                print('Safe, but low')
            elif self.current < self.LOW:
                print('Not good ,eat!')

"""
Have calc call admin to administer insulin and take away from total + add to cumulative.
"""