class student:
    def __init__(self,m1,m2,m3):
        self.phy=m1
        self.maths=m2
        self.eng=m3

    def display_phy(self):
        print(self.phy)
obj=student(23,45,40)
obj.display_phy()
obj1=student(50,34,45)
obj1.display_phy()