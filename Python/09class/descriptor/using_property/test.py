class SomeClass:
    def __init__(self, budget, rating):
        # underlying attributes:
        self._budget = None
        self._rating = None

        self.budget = budget
        self.rating = rating

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if value < 0:
            raise ValueError("Negative value got: %s" % value)
        self._budget = value

    # not reusable, duplicate code:
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if value < 0:
            raise ValueError("Negative value got: %s" % value)
        self._rating = value


def run():
    #c = SomeClass(1000, -1)
    c = SomeClass(1000, 5)
    print("budget:", c.budget)

if __name__ == '__main__':
    run()
