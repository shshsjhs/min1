def pppp(o,j):
    p=0
    while p<len(j):
        if int(j[p])==int(o):
            return p
        p+=1
while True :
    try:
        target=int(input())
        nums=list(input())
        for i in nums:
            if i==' ':
                nums.remove(' ')
        print(nums)
        c=0        
        for x in nums:
            for y in nums:
                if int(x)+int(y)==target and int(x)!=int(y) and pppp(x,nums)+pppp(y,nums)!=c:
                    print(pppp(x,nums),end=" ")
                    print("",end=" ")
                    print(pppp(y,nums))
                    c=pppp(x,nums)+pppp(y,nums)
    except :
        break
