def make_sandwich(*toppings):
    print('\nSandwich with:')
    for topping in toppings:
        print('- ' + topping)


make_sandwich('whole-grain bread', 'hummus', 'tomato', 'cucumber')
make_sandwich('bread', 'hummus', 'tomato', 'cucumber')
make_sandwich('bread')
