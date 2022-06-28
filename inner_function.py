g = 'gray'


def colors():
    y = 'yellow'
    g = 'green'

    def print_red():
        r = 'red'
        print(r, y, g)

    def print_blue():
        b = 'blue'
        print(b, y, g)

    print_blue()
    print_red()


colors()
