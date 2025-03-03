class Person:
    _AVAIL = object()

    def check(self):
        return Person._AVAIL


print(Person().check())
