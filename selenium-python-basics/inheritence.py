class parent :
    def __init__(self):
        print("this is the parent class")
    def money(self):
        print("this is parents money")
class child(parent):
    pass
p=parent()
p.money()
c=child()
c.money()

