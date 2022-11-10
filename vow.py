vowels=["a","e","i","o","u"]
word=input("enter the word:")

list1=[]
for alphabet in word:
    if alphabet in vowels:
        list1.append(alphabet)
        print(list1)
