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
    raise_amount = 1.10
    
    def __init__(self, fname, lname, pay, prog_lang):
        super().__init__(fname, lname, pay)
        #Employee.__init__(self, fname, lname, pay)

        # We can use either super init method or class init method to pass the attribute values to the parent class. 
        # However using super is a most meaningfull and understandabe way.
        
        self.lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees= None):
        super().__init__(fname, lname, pay)
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
            print('-->', emp.fullname())


dev_1 = Developer('Senthil', 'Kumar', 50000, 'Python')
dev_2 = Developer('Vasantha', 'Priya', 60000, 'Staff Nurse')

mgr_1 = Manager('Sue', 'Smith', 60000, [dev_1])

print(mgr_1.email)
#mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

#print(dev_1.email)
#print(dev_2.email)

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)
#print(dev_1.lang)

#print(dev_2.pay)
#dev_2.apply_raise()
#print(dev_2.pay)
#print(dev_2.lang)

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

