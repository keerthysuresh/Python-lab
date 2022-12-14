lower=int(input("enter lower limit"))
upper=int(input("enter upper limit"))
a=[]
a=[x for x in range(lower,upper+1)if(int(x**0.5))**2==x]
print(a)