# Magic Methods are a special methods which help to change the behaviour of the existing methods and adding additionals features as well
# These special methods are always surrounded by double underscore (__)

class Employee:
    
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname+lname+'@neofinancial.com'

    def fullname(self):
        return self.fname +' '+self.lname

    def __repr__(self):
        return "Employee ('{}', '{}', '{}')".format(self.fname, self.lname, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Senthil', 'Kumar', 4500000)
emp_2 = Employee('vasantha', 'priya', 2000000)

#print(emp_1) # By default __str__ will get trigger with the default option of returning the class address.
print(emp_1)
print(repr(emp_1)) # When we modify the __repr__ method it will disply the details we specify in the __repr__ method 

# When we call str(emp1) without modifying the __str__ method it ll work like __repr__ mothod. 
#Based on the changed made in __str__ method , it will work after that.
# print(emp_1) works like __str__ once its implemented
print(str(emp_1))

print(emp_1.__str__())
print(emp_2.__repr__())


print(1+2) # it will call int dunder add method int.__add__(1,2) in the background and add it.
print('a'+'b') # it will call str dunder concat method str.__add__('a','b') in the background and concatinate it.

print(emp_1 + emp_2) # it will call the __add__(self, other) method and return the sum of pay

print(len(emp_1))