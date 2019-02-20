bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())      #capital letter
print(bicycles[1])
print(bicycles[-1])             #last element
print(bicycles[-3])

message = "My first bicycle was a " + bicycles[0].title() + "."     #concatenation with lists
print(message)