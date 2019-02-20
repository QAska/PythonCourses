cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()                                         #constant alphabetizing
print(cars)
cars.sort(reverse=True)                             #constant reverse alphabetizing
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()                                      #constant sorting in reverse order (not in alphabetical order)
print("\nHere is the sorted list in reverse order:")
print(cars)
cars.reverse()                                      #constant sorting in reverse order (not in alphabetical order)
print("Here is the original list again after reverse:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the new original list:")
print(cars)
print("Here is the alphabetically sorted list:")
print(sorted(cars))                                         #temporary alphabetical sorting
print("Tere is the sorted list in reverse alphabetical order:")
print(sorted(cars, reverse=True))                           #temporary sorting in reverse alphabetical order

print(len(cars))            #list length