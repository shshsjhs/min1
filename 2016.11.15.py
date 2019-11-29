while True:
    try:
        n=int(input())
        a=input()
        a = a.split(" ")
        sum=0
        i=0
        #for i in range(len(a)):
        #    pass
        #for index,value in enumerate(a):
        #    pass
        while i<n:
            a[i]=int(a[i])
            sum=sum+a[i]
            i+=1
        min=a[0]
        max=a[0]
        for i in a:
            if i<min:
                min=i
        for j in a:
            if j>max:
                max=j
        print(max)
        print(min)
        print(sum)
    except:
        break




