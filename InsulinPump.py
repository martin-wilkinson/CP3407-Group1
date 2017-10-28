from

current = 0
previous = 5
HIGH = 7
LOW = 3


def main():
    manual_mode = False
    while manual_mode is False:
        count = 1                                   # This iterates through the data in CSV.
        print("Running startup Checks")
        sensorCheck()
        # startup checks here
        # In while loop I would need a count to say which line to read for the csv.

        getZone()

        pass

def getReading(previous, current):
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

def sensorCheck():

    pass

main()

"""
Have calc call admin to administer insulin and take away from total + add to cumulative.

self-test  program  every  30  seconds.
Check blood sugar every 10mins and deliver insulin if needed

"""