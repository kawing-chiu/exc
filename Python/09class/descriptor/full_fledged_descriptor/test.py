from weakref import WeakKeyDictionary


class NonNegative:
    def __init__(self):
        # use WeakKeyDictionary to do bookkeeping
        self._data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        # instance may be None if the attribute is accessed from the class

        # owener is just the class of instance:
        print(owner is type(instance))

        return self._data[instance]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Negative value got: %s" % value)
        self._data[instance] = value

    def __delete__(self, instance):
        raise AttributeError("Deletion of attribute is not supported!")

class Movie:
    # all instances of the Movie class use the same descriptor instance!!!
    budget = NonNegative()
    rating = NonNegative()

    def __init__(self, budget, rating):
        # no need to use a 'underlying' attribute any more
        self.budget = budget
        self.rating = rating



def run():
    #m = Movie(1000, -1)
    m = Movie(1000, 5)
    print("budget:", m.budget)
    del m.rating

if __name__ == '__main__':
    run()
