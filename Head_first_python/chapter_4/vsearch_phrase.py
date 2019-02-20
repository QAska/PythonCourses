def search4letters(phrase, letters):
    """Возвращает буквы, найденные в указанном слове."""
    return vowels.intersection(set(phrase))

def test_search4letters_1():
    assert search4vowels('samara') == {'a'}

def test_search4letters_2():
    assert search4vowels('') == set()