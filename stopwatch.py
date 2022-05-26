import time

def stopwatch_main():
    underStart = "\u0332".join("START")
    underStop = "\u0332".join("STOP")
    
    input("Press enter to " + underStart + " the stopwatch")
    start = time.time()

    input("Press enter to " + underStop + " the stopwatch")
    finish = time.time()

    stopwatch = finish - start

    min = stopwatch // 60
    sec = stopwatch - (min * 60)
    hour = min // 60
    min = min - (hour * 60)
    
    timeArray = [hour, min, sec] 

    print("{0}:{1}:{2}".format(int(timeArray[0]),int(timeArray[1]),int(timeArray[2])))
    input("Press ENTER to return to the menu.")

    return