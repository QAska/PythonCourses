def search4vowels(word):
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))


def test_search4letters_1():
    assert search4letters('samara') == {'a'}


def test_search4letters_2():
    assert search4letters('hitch-hiker', 'aeiou') == {'e', 'i'}


def test_search4letters_3():
    assert search4letters('', '') == set()


def test_search4vowels_1():
    assert search4vowels('samara') == True


def test_search4vowels_2():
    assert search4vowels('') == False
