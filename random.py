import random
import time

def getRandomDate(startDate, endDate):
    print("Printing random date between", startDate, "and", endDate)
    randomgen = random.random()
    print(randomgen)
    dateFormat = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startDate, dateFormat))
    print(starttime)
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    print(endtime)
    randomtime = starttime + randomgen *(endtime - starttime)
    print(randomtime)
    randomdate = time.strftime(dateFormat, time.localtime(randomtime))
    print(time.localtime(randomtime))
    return randomdate
    
print("Random Date =", getRandomDate ("1/1/2020", "12/12/2024"))
    
    
