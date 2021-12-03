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

class Developer(Employee): # create Developer class by extending Employee class
    pass

dev_1 = Employee('Senthil', 'Kumar', 4500000)
dev_2 = Employee('vasantha', 'priya', 2000000)

print(dev_1.fullname())
print(dev_2.email)