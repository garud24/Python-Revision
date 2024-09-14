## Creating our own class dog
'''
This demonstarte how do we crate our own class and how to access attributes,
How does __init__() works and what is the role of self
What is the advantage of Class and Methods
'''

class Dog():
    
    def __init__(self, name, age, kind):
        self.name = name
        self.age = age
        self.kind = kind
        
    def display(self):
        print("The name of the dog is :{} It's age is: {} It's kind is: {}".format(self.name, self.age, self.kind))
        
    def change_name(self, new_name):
        self.name = new_name
        print("The New Name of the dog is :", self.name)   
        

tommy = Dog("tommy", 5, "street")
mony = Dog("mony", 55, "Lab")

'''The display function is working'''
tommy.display()
mony.display()

'''The change_name'''
tommy.change_name("spike")

print(tommy.name)
            