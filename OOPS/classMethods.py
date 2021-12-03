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
        
emp_1 = Employee('Senthil', 'Kumar', 4500000)
emp_2 = Employee('vasantha', 'priya', 2000000)

Employee.set_raise_amount(1.11)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# user can call class method using instances also

emp_1.set_raise_amount(1.06)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# create a new class using classmethod
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'John-Davidson-80000'
emp_str_3 = 'John-Smith-90000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())
print(new_emp_1.email)