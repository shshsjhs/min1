while True :
    try:
        b=int(input())
        a=input()
        a=a.split(" ")
        for index, value in enumerate(a):
            a[index] = int(value)
        print(a)
        j=0
        while j<len(a):
            if a[j]==b:
                print(j)
            j+=1
    except :
        break

