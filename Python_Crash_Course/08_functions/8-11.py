magicians = ['amayak akopyan', 'david copperfield', 'harry houdini']


def make_great(magicians):
    new_magicians = []
    for magician in magicians:
        new_magicians.append('Great ' + magician)
    return new_magicians


def show_magicians(new_magicians):
    for magician in new_magicians:
        print(magician.title())


new_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(new_magicians)
