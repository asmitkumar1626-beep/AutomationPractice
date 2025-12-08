class Employee:
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.weight=weight
    def print_age(self):
        print("your age is ",self.age)
    def print_name(self):
        print("your name is ",self.name)
    def print_weight(self):
        print("your weight is ",self.weight)

emp1=Employee("asmit","22","50")
emp1.print_name()
emp1.print_weight()
emp1.print_age()