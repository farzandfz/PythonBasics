import time

startTime = time.time()

#for x in range(1,10):
 #   print(x)

sum=1
while sum<100:
     print(sum)
     sum+=1

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
    print('Thank you!')

print("Elapsed time is %s seconds" % (time.time() - startTime))
