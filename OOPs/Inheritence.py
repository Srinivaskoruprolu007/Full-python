from OOPs.ClassDemo import Employee


class SpecialEmployee(Employee):
    def hours(self, numhour):
        self.owned += numhour * self.rate
        return "%.2f hours worked" % numhour

    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate)  # calls the base classes
        self.bonus = bonus

    def __repr__(self):
        return 'a custom object (%r)' % self.name


specialEmployee = SpecialEmployee(name="hero", rate=23.5, bonus=3000)
specialEmployee.hours(44)