i=2 
a=0 
b=1 
sum=1
while i<41:
    c=a+b
    a=b
    b=c
    sum=sum+c
    i+=1
print(sum)