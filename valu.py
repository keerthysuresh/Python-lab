sen=input("enter the word:")
counts=dict()
words=sen.split()
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
        print(counts)
