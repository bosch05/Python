class Employee:

    def __init__(self, first, last, title, pay):
        self.first = first
        self.last = last
        self.title = title
        self.pay = pay

    def fullname(self):
        return self.first + " " + self.last

    def payraise(self, raiseamount):
        self.pay = int(self.pay * (1 + raiseamount))


emp_1 = Employee("Cyril", "Bosch", "Fund Manager", 100000)
emp_2 = Employee("Christina", "Bosch", "Accountant", 100000)

print(emp_1.fullname())
print(emp_1.pay)
emp_1.payraise(0.05)
print(emp_1.pay)
