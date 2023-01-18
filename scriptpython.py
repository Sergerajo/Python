class Emp: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = 30 
      
    def info(self): 
        print("Bonjour, % s. Vous avez % s ans." % (self.name, self.age)) 
  
Emps = [Emp("John", 43), 
    Emp("Hilbert", 16), 
    Emp("Alice", 30)] 
  
for emp in Emps: 
    emp.info()
