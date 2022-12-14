def fib(n):
    first=0
    second=1
    if n==1:
        print(first)
    else:
        for i in range (n):
            print(first)
            third=first+second
            first=second
            second=third
n=int(input("enter a number"))
fib(n)