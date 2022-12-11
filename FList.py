FList=[]
SList=[]
Sum1=0
Sum2=0
inp=0
len1=int(input("How many number do you want to add in  first list :"))
for i in range(0,len1):
    inp==int(input("Enter the value for element:"))
    FList.append(inp)
len2=int(input("How many numbers do you want to add in second list :"))
for i in range(0,len2):
    inp=int(input("Enter the value for element :"))
    SList.append(inp)
if(len(FList)==len(SList)):
    print("Two lists are of same length")
else:
    print("Lists have of different length")
    for num in FList:
        Sum1+=num
    for num in SList:
        Sum2+=num
    if Sum1==Sum2:
        print("The sum of values of elements in both list are equal")
    else:
        print("Sum of values of both lists are different")
for num in FList:
    if num in SList:
        print(num,"found in both lists\n")
