class Employee:
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email
    def greet(self):
        print("hello",self.fname)

emp1=Employee('asmit','kumar','asmitkumar7750@gmail.com')
emp2=Employee('madhu','kanar','itsmadhuri@gmail.com')
print(emp1.fname)
print(emp2.lname)
emp1.greet()

