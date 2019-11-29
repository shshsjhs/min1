a=1000
sum=0
j=0
while a>0:
    sum=0
    i=2
    while i<a:
        if a%i==0:
            sum=sum+i
        i+=1
    if sum==0:
        j+=1
    a-=1
print(j)  