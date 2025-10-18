class emp:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
class empchild(emp):
    def __init__(self,name,age,sal,idnum):
        self.name=name
        self.age=age
        self.sal=sal
        self.idnum=idnum
#driver mode
e=emp("lucky",23,3000)
print("emp name =",e.name)
e1=empchild("lucky-B sec",23,3000,22)
print(e1.name)
        
