class Employee:
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    
    def email(self):
        return '{}.{}@neofinancial.com'.format(self.fname, self.lname)

    @property # to access a method like attribute, it means no need to call like method -> emp.fullname(), simply emp.fullname is enough.
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    @fullname.setter
    def fullname(self, name):
        fname, lname = name.split(' ')
        self.fname = fname
        self.lname = lname
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.fname = None
        self.lname = None

emp_1 = Employee('Senthil', 'Kumar', 4500000)
emp_2 = Employee('vasantha', 'priya', 2000000)

print(emp_1.fullname)
print(emp_1.email())

emp_1.lname = 'Kanagaraj'
print(emp_1.fullname)
print(emp_1.email())

# When we change the method as property, we cant change the value of the property directly.
# we have to use setter for re-assigning values

print('After Setting Setter method')
emp_1.fullname = 'Kabil Raj'
print(emp_1.fullname)

print('After Setting deleter method')
del emp_1.fullname
print(emp_1.fullname)