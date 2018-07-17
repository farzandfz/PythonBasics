import time

startTime = time.time()

for x in range(1,10):
    print(x)


print("Elapsed time is %s seconds" % (time.time() - startTime))
