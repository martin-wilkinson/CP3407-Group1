from getTestData import *


HIGH = 7
LOW = 3


def main():
    count = 1                                       # This iterates through the data in CSV.
    current = 0
    manual_mode = False
    # while manual_mode is False:                   # Manual/Auto loop switch
    for i in range(19):
        print("Running startup Checks")
        checks(count)                               # startup checks
        previous = current
        current = getLevels(count)
        print("current=",current, "previous=", previous)
        getZone(current, previous)
        count += 1

def getLevels(count):
    current = int(getData(count, 6))
    return current

def getZone(current, previous):
    if (int(round((current - previous), 0))) > 0:
        if current > HIGH:
            print('UNSAFE')
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")

    elif (int(round((current - previous), 0))) < 0:
        if current > HIGH:
            print('UNSAFE')
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")

    elif (int(round((current - previous), 0))) == 0:
        if current > HIGH:
            print('UNSAFE')
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")


def checks(count):
    sensorStatus = getData(count, 1)
    pumpStatus = getData(count, 2)
    deliveryStatus = getData(count, 3)
    needleStatus = getData(count, 4)
    reservoirStatus = getData(count, 5)
    statusArray = []
    statusArray.extend([sensorStatus, pumpStatus, deliveryStatus, needleStatus, reservoirStatus])
    print(statusArray)


main()

"""
Have calc call admin to administer insulin and take away from total + add to cumulative.

self-test  program  every  30  seconds.
Check blood sugar every 10mins and deliver insulin if needed

"""