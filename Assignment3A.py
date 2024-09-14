## This is the inheritance tutorial

'''Here we will be looking at the inheritance 
how to inherit the parent class 
how to do method overriding
'''

class dog():
    def __init__(self, name, age):
        self.name = name
        self.age =  age 
        
    def speak(self):
        print("Hi my name is {} and my age is {}".format(self.name, self.age))
    
    def action(self):
        print("Bark!!")

class cat(dog):
    def __init__(self,name, age, color):
        super().__init__(name, age)
        self.color = color
    
tim = cat("tim", 55, "blue")
tim.speak()                        