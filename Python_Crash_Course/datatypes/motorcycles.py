motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'                       #replaces 1st element
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')                    #adds to the end of the list
print(motorcycles)

motorcycles = []                                #creates list from scratch
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0,"ducati")                  #inserts element according index
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[1]                              #deletes element by index
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()          #extracts last element and saves element extracted
print(motorcycles)                              #list without element removed
print(popped_motorcycles)                       #element removed

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)                                             #extracts n element
print("The first motorcycle I owned was a " + first_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')                        #deletion by value (first occurrence deleted)
print(motorcycles)
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)                   #deletion by variable
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensice for me.")