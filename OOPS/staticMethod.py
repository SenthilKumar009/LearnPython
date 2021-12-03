import datetime
class Employee:
    
    raise_amount = 1.04     

    no_of_emp = 0

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+lname+'@neofinancial.com'

        Employee.no_of_emp +=1

    def fullname(self):
        return self.fname +' '+self.lname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod  # it will work on the class directly instead of through objects
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

        
emp_1 = Employee('Senthil', 'Kumar', 4500000)
emp_2 = Employee('vasantha', 'priya', 2000000)

my_date = datetime.date(2017, 1, 11)

print(Employee.is_workday(my_date))