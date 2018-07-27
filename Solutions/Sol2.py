import math
import time

startTime = time.time()


mealCost = float(input('Enter mealCost:' ))
tip = int(input('Enter tip:' ))
tax = int(input('Enter tax:' ))

totalC = 0


def totalCost():
    tipC = (mealCost * tip) / 100
    taxC = (mealCost * tax) / 100
    totalC = mealCost + tipC + taxC
    roundCost = int(totalC)
    print('The total meal cost is', roundCost, 'dollars.')

    return totalC

totalCost()
print("Elapsed time is %s seconds" % (time.time() - startTime))