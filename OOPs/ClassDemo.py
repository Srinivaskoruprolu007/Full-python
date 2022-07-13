class Employee(object):
    numEmployee = 0

    def __init__(self, name, rate):
        self.owned = 0
        self.name = name
        self.rate = rate
        Employee.numEmployee += 1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numhour):
        self.owned += numhour * self.rate
        return "%.2f hours worked" % numhour

    def pay(self):
        self.owned = 0
        return "Payed %s" % self.name

    def __repr__(self):
        return "a custom object (%r)" %self.name


# creating an object based on the above class template
emp1 = Employee(name="vasu",rate=17.8)
print(Employee.numEmployee)
print(emp1.name)
emp1.__del__()
emp1.__repr__()