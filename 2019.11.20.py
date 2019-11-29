while True:
    try:
        n=int(input())
        i=0
        while i<=n:
            m=int(input())
            list.append(m)
            i+=1
        p=-1
        q=int(input())
        i=0
        while i<n:
            if q==list[i]:
                p=i+1
                break
            i+=1
        print(p)
    except:
        break
