class Rate:
    interest=2
    def __init__(self,name,loan):
        self.name=name
        self.loan=loan
    def Interest(self):
        print("interest amnt comes to : ",self.loan * self.interest)
class student(Rate):
    interest = 1.2
    pass
guy1=student("asmit",2000)
guy1.Interest()

