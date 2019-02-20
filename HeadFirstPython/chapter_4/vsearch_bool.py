def search4vowels(word:str) -> set:
    """Возвращает гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))

def test_search4vowels_1():
    assert search4vowels('samara') == {'a'}

def test_search4vowels_2():
    assert search4vowels('') == set()