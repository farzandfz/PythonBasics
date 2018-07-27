

#print('How many cucumbers do you need?')
print('Price per cucumber is 3.25 doubloons')
cucumbers=int(input('How many cucumbers do you need?: '))
#cucumbers=3
price_per_cucumber=3.25
total_cost=cucumbers*price_per_cucumber
message='Total cost of %s cucumber is %s doubloons'
print(message % (cucumbers, total_cost))

