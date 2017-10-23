current = 6
previous = 5
HIGH = 7
MID = 5
LOW = 3

def main():
    pass

def getRate():
    pass

def sugarLow():


def calculate():
    if getRate() > 0:                         # Checking if Sugar Level (SL) rising
        if current > HIGH:
            print('UNSAFE')
        elif current > MID:
            print('Safe, but high')
        elif current > LOW:
            print('Safe, but low')
        elif current < LOW:
            print('Not good ,eat!')

    elif getRate() < 0:                         # Checking if Sugar Level (SL) falling
        if current > HIGH:
            print('UNSAFE')
        elif current > MID:
            print('Safe, but high')
        elif current > LOW:
            print('Safe, but low')
        elif current < LOW:
            print('Not good ,eat!')

    elif getRate() == 0:
        if current > HIGH:
            print('UNSAFE')
        elif current > MID:
            print('Safe, but high')
        elif current > LOW:
            print('Safe, but low')
        elif current < LOW:
            print('Not good ,eat!')