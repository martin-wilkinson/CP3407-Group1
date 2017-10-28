from database import *


current = 0
previous = 5
HIGH = 7
LOW = 3

def main():
    print("Running startup Checks")
    # startup checks here
    getZone()
    pass

def getReading(prewious, current):
    # This will assign current to previous and then get a reading from DB to assign current
    previous = current
    current = pull_from_blood_sugar_table()

def getRate():
    rate = int(round((current - previous), 0))
    return rate

def getZone():
    if getRate() > 0:
        if current > HIGH:
            print('UNSAFE', getRate())
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")

    elif getRate() < 0:
        if current > HIGH:
            print('UNSAFE')
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")

    elif getRate() == 0:
        if current > HIGH:
            print('UNSAFE')
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")

main()

"""
Have calc call admin to administer insulin and take away from total + add to cumulative.
"""