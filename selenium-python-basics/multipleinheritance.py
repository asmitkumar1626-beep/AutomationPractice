class Move:
    def movefrd(self):
        print(self.name," will move forward")
    def movebwd(self):
        print(self.name," will move backward")
class Jump:
    def jumpfwd(self):
        print(self.name," will jump forward")
    def jumpbwd(self):
        print(self.name," will jump backward")
class Ben(Move,Jump):
    name="ben"
    pass
class Kevin(Move,Jump):
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