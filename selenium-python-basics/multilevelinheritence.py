class Move:
    def movefrd(self):
        print(self.name," will move forward")
    def movebwd(self):
        print(self.name," will move backward")
class Jump(Move):
    def jumpfwd(self):
        print(self.name," will jump forward")
    def jumpbwd(self):
        print(self.name," will jump backward")
class Ben(Jump):
    name="ben"
    pass
class Kevin(Jump):
    name="kevin"
    pass
p=Ben()
p.movefrd()
p.jumpbwd()
p.jumpfwd()
p.movebwd()
p=Kevin()
p.movefrd()
p.jumpbwd()
p.jumpfwd()
p.movebwd()
# if a has some properties it will be inherited by b and after 2 years b gives a child c so C will inherit the properties of b and because b had the properties of a so c will inherit the properties of b as well as a