from time import gmtime, strftime


from getTestData import *

HIGH = 7
LOW = 3
MAX_DAILY_DOSAGE = 10
MAX_DOSAGE = 3
DOSE = 1


def main():
    count = 1  # This iterates through the data in CSV.
    current = 0
    reservoir = int(reservoirLevel())
    dailyDosage = 0
    manualMode = False
    if manualMode is False:  # Manual/Auto loop switch
        for i in range(19):
            time = strftime("%H:%M:%S", gmtime())
            # print("Running startup Checks")
            statusArray = checks(count)  # startup checks
            # print(statusArray)
            previous = current
            current = getSugarLevels(count)
            # print("current=",current, "previous=", previous)
            rate = getRate(current, previous)
            if canAdminister(rate, current):
                message = "{}: {}".format(time, canAdminister(rate, current)[1])
                print(message)
                if rate >= MAX_DOSAGE:
                    rate = MAX_DOSAGE
                canDose = cumlativeDose(rate, dailyDosage)[0]
                # print(canDose)
                if reservoir >= rate and canDose:
                    dailyDosage = cumlativeDose(rate, dailyDosage)[1]
                    message3 = "{}: Insulin Delivered.".format(time)
                    print(message3)
                elif cumlativeDose(rate, dailyDosage) is False:
                    dailyExceedMessage = "{}: Daily Dosage exceeded.".format(time)  # Error for too much dose in a day.
                    print(dailyExceedMessage)
                elif reservoir < rate:
                    emptyReservoirMessage = "{}: Reservoir out of insulin.".format(time)
                    print(emptyReservoirMessage)

                print(dailyDosage)
            count += 1
        while manualMode is True:
            time = strftime("%H:%M:%S", gmtime())
            # button code here
            # within a 5 second window from first press, count the amount of presses to get the dosage.
            # pass the button count presses to manualAdminister
            manualDosage = manualAdminister(buttonCount, dailyDosage, time)


def manualAdminister(buttonCount, dailyDosage, time):  # This is to handle the manual buttons and administer dosage
    if ((DOSE * buttonCount) + dailyDosage) > MAX_DAILY_DOSAGE or (MAX_DOSAGE + dailyDosage) > MAX_DAILY_DOSAGE:
        manualDailyExceedMessage = "{}: Daily Dosage exceeded.".format(time)
        return manualDailyExceedMessage
    else:
        dailyDosage += (DOSE * buttonCount)
        return dailyDosage


def cumlativeDose(rate, dailyDosage):
    if (dailyDosage + rate) > MAX_DAILY_DOSAGE:
        return False, dailyDosage
    elif (dailyDosage + rate) <= MAX_DAILY_DOSAGE:
        dailyDosage += rate
        return True, dailyDosage


def getSugarLevels(count):
    current = int(getData(count, 6))
    return current


def getRate(current, previous):
    rate = int(round((current - previous), 0))
    return rate


def canAdminister(rate, current):
    if rate > 0:
        if current > HIGH:
            message = 'Blood Sugar levels high'
            return True, message
        elif LOW <= current <= HIGH:
            message = 'Blood Sugar Safe'
            return False, message
        elif current < LOW:
            message = "Your Blood Sugar Levels are low!"
            return True, message

    elif rate < 0:
        if current > HIGH:
            message = 'Blood Sugar levels high'
            return True, message
        elif LOW <= current <= HIGH:
            message = 'Blood Sugar Safe'
            return False, message
        elif current < LOW:
            message = "Your Blood Sugar Levels are low!"
            return True, message

    elif rate == 0:
        if current > HIGH:
            message = 'Blood Sugar levels high'
            return True, message
        elif LOW <= current <= HIGH:
            message = 'Blood Sugar Safe'
            return False, message
        elif current < LOW:
            message = "Your Blood Sugar Levels are low!"
            return True, message


def reservoirLevel():
    level = getData(1, 7)
    return level


def get_status_checks(count):
    sensorStatus = getData(count, 1)
    pumpStatus = getData(count, 2)
    deliveryStatus = getData(count, 3)
    needleStatus = getData(count, 4)
    reservoirStatus = getData(count, 5)
    statusArray = []
    statusArray.extend([sensorStatus, pumpStatus, deliveryStatus, needleStatus, reservoirStatus])
    return statusArray

# def checkReservoir(count):
#     print(getData(count, 7))
#     if getData(count, 7) == 'TRUE':
#         return True
#     else:
#         return False
