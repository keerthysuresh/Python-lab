class Addition:
    a=0
    b=0
    c=0
    def __init__(self,f,s):
        self.a=f
        self.b=s
    def calculate(self):
        self.c=self.a+self.b
        print(self.c)
obj1=Addition(1,2)
obj1.calculate()
obj2=Addition(3,4)
obj2.calculate()