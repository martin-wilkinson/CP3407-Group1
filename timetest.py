from time import gmtime, strftime

now = strftime("%H:%M:%S", gmtime())
if str(now) == "00:00:00":
    print(now)
