def make_album(name, title, number=''):
    album = {'name': name, 'title': title, 'number': number}
    return album


while True:
    name = input('Enter singer: ')
    if name == 'q':
        break
    title = input('Enter name of album: ')
    if title == 'q':
        break
    number = input('Enter number of songs: ')
    if number == 'q':
        break

    album = make_album(name, title, number)
    print(album, '\n')

