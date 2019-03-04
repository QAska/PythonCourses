glossary = {
    'number': 'data type to store numeric values',
    'string': 'contiguous batch of characters',
    'list': 'collection which is ordered and changeable',
    'tuple': 'collection which is ordered and unchangeable',
    'set': 'collection which is unordered and unindexed',
    'dictionary': 'collection which is unordered, changeable and indexed',
    'class': 'user-defined prototype for an object that defines a set of attributes',
    'inheritance': 'transfer of the characteristics of a class to other classes that are derived from it',
    'method': 'special kind of function that is defined in a class definition',
    'object': "unique instance of a data structure that's defined by its class",
}

for key, value in glossary.items():
    print(key.title(), 'is a', value + '.')
