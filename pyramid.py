r=int(input("enter the number of rows:"))
for i in range(1,r+1):
    for j in range(1,i+1):
        sqr=i*j
        print(i*j,end=" ")
    print(" ")