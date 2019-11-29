import math
n=int(input())
i=1
j=1
while i<=n:
    if math.sqrt(i)==int(math.sqrt(i)):
        if j==1:
            print(i,end=" ")
            j+=1
        else:
            print( i,end=" ")
    i+=1

