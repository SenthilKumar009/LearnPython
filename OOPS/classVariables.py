class Employee:
    
    raise_amount = 1.04 # its a class variable and it can be access through class and all the objects.
    # this is common for all the objects

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
        # self.pay = int(self.pay * raise_amount) -> cant access the raise amount variable like this.
        # We must access through class intance. Otherwise it will throw an error.
        self.pay = int(self.pay * self.raise_amount)
        # self.pay = int(self.pay * Employee.raise_amount) -> This also works

emp_1 = Employee('Senthil', 'Kumar', 4500000)
emp_2 = Employee('vasantha', 'priya', 2000000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)


# -----------------------------------------------------------------------------------------------#

print(emp_1.__dict__) # It will display the object variable's details
print(Employee.__dict__) # it will display the class details and the places where variable stored.

# -----------------------------------------------------------------------------------------------#

Employee.raise_amount = 1.05  # It will applicable to all the objects
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)


emp_1.raise_amount = 1.06 # It will change/ applicable only to the object emp_1
emp_2.raise_amount = 1.08 # It will change/ applicable only to the object emp_2
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)

# -----------------------------------------------------------------------------------------------#

print(Employee.no_of_emp)