len=int(input("How many numbers do you want to store?"))
inpvalueList=[]
for num in range(0,len):
    inpvalue=int(input("Enter value :"))
    if inpvalue>100:
        inpvalueList.append("Over")
    else:
        inpvalueList.append(inpvalue)
print(inpvalueList)
