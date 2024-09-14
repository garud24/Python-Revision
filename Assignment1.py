# Python Object-Oriented Programming

# creating a simple Employee Class

class Employee:
    def __init__(self, first, last, pay):
        self.first =  first
        self.last = last
        self.pay = pay
        self.email = self.first + '.' + self.last + "@gmail.com"
    # This method is like a constructor, it will be created when  an object is created    
        

# Now we have a simple employee class 

emp_1 = Employee("Himanshu","Garud",4500) # This is a instance of class Employee
emp_2 = Employee("Shivani", "Gaikwad", 60000) # This is a instance of class Employee

# Each of these instances will be unique
print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_1.first, emp_1.last)) # This is a lot of work, so we will be needing methods


