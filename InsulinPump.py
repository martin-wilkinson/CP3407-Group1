from getTestData import *
from time import gmtime, strftime

HIGH = 7
LOW = 3
MAX_DOSAGE = 10

def main():
    count = 1                                       # This iterates through the data in CSV.
    current = 0
    reservoirCapacity = 10
    manualMode = False
    # while manualMode is False:                    # Manual/Auto loop switch
    for i in range(19):
        # print("Running startup Checks")
        checks(count)                               # startup checks
        if checkReservoir(count):
            newReservoir = True
        else:
            newReservoir = False
        previous = current
        current = getLevels(count)
        print("current=",current, "previous=", previous)
        rate = getRate(current, previous)
        if administer(rate, current):
            if cumlativeDose():
                reservoirLevel(rate, newReservoir)
            else:
                pass # Error for too much dose in a day.
        count += 1

def cumlativeDose(rate):
    now = strftime("%H:%M:%S", gmtime())
    if str(now) == "00:00:00":
        dailyDosage = 0
    elif (dailyDosage + rate) > MAX_DOSAGE:
        print("Maximum Daily Insulin will be exceeded")
        return False
    elif (dailyDosage + rate) <= MAX_DOSAGE:
        dailyDosage += rate
        return dailyDosage


def getLevels(count):
    current = int(getData(count, 6))
    return current


def getRate(current, previous):
    rate = int(round((current - previous), 0))
    return rate


def administer(rate, current):
    if rate > 0:
        if current > HIGH:
            print('Blood Sugar levels high, ', rate, 'delivered.')
            return True
        elif LOW <= current <= HIGH:
            print('Safe')
            return False
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")
            return True

    elif rate < 0:
        if current > HIGH:
            print('Blood Sugar levels high, ', rate, 'delivered.')
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")

    elif rate == 0:
        if current > HIGH:
            print('Blood Sugar levels high, ', rate, 'delivered.')
        elif LOW <= current <= HIGH:
            print('Safe')
        elif current < LOW:
            print("Your Blood Sugar Levels are low!")


def reservoirLevel(rate, newReservoir):
    print(rate, newReservoir)
    if newReservoir:
        level = 10
    else:
        level -= rate

    if level <= 0:
        print("Reservoir is Empty!")
    else:
        return level


def checks(count):
    sensorStatus = getData(count, 1)
    pumpStatus = getData(count, 2)
    deliveryStatus = getData(count, 3)
    needleStatus = getData(count, 4)
    reservoirStatus = getData(count, 5)
    statusArray = []
    statusArray.extend([sensorStatus, pumpStatus, deliveryStatus, needleStatus, reservoirStatus])
    return statusArray

def checkReservoir(count):
    print(getData(count, 7))
    if getData(count, 7) == 'TRUE':
        return True
    else:
        return False

main()

"""
Have calc call admin to administer insulin and take away from total + add to cumulative.

self-test  program  every  30  seconds.
Check blood sugar every 10mins and deliver insulin if needed

"""