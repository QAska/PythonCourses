def make_album(name, title, length=''):
    album = {'name': name, 'title': title, 'length': length}
    return album


album_1 = make_album('Singer_1', 'Title_1')
album_2 = make_album('Singer_2', 'Title_2')
album_3 = make_album('Singer_3', 'Title_3')
album_4 = make_album('Singer_4', 'Title_4', 13)

print(album_1)
print(album_2)
print(album_3)
print(album_4)
