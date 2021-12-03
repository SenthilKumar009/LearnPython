# Class is a blue print to create an object
# Class contains attribute and method
# Objects/ instances which are created from the class can access the method and attributes

class Employee:
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+lname+'@neofinancial.com'

    def fullname(self):
        return self.fname +' '+self.lname

emp_1 = Employee('Senthil', 'Kumar', 4500000)
emp_2 = Employee('vasantha', 'priya', 2000000)

#print(emp_1.fullname())

# When wetry to call the methods  directly from the from class we need to pass the object as an argument

#Employee.fullname() # it will throw an error.
print(emp_1.fullname())
print(Employee.fullname(emp_1)) # it will throw an error.
