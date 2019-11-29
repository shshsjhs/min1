n=100
while n<1000:
    a=n/100
    b=(n-a*100)/10
    c=n-a*100-b*10
    if a**2+b**2+c**2==n:
        print(n)
    n=n+1