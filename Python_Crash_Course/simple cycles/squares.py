squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)          #the new value 'square' joins the list of squares
    print(squares)

squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)

squares = [value**2 for value in range(1,11)]
print("\n" + str(squares))