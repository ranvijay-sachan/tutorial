import datetime


class Employee(object):
    no_of_employee = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@example.com"

        Employee.no_of_employee += 1

    def __repr__(self):
        return "Employee('{}, {}, {}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        return self.pay * self.raise_amt

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())

emp_1 = Employee.from_string('sonam-sachan-70000')
emp_2 = Employee.from_string('sonam-sachan-10000')

print emp_1 + emp_2
# print(emp_1.fullname(), emp_1.email, emp_1.pay)
# print Employee.is_workday(datetime.date(2017, 8, 7))

# dev1 = Developer("Ranvijay", "Sachan", 570000, 'python')
# dev2 = Developer("Neha", "Sachan", 500000, 'java')
#
#
# mgr1 = Manager("xyz", "singh", 570000, [dev1])
# print mgr1.email
# mgr1.add_emp(dev2)
# print mgr1.print_emps()
# print isinstance(mgr1, Manager)
# print issubclass(Developer, Manager)
# print(repr(mgr1))



