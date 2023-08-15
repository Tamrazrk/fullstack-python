magician_names = ["Harry Houdini", "David Blaine", "Criss Angel"]


def show_magicians():
    print("magician names:", magician_names)


def make_great():
    for i in range(len(magician_names)):
        magician_names[i] += " the Great"


make_great()
show_magicians()
