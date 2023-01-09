class A:
    def method_A(self):
        print("parent class A")
class B(A):
    def method_B(self):
        print("child class B")
obj=A()
obj.method_A()
obj=B()
obj.method_B()

