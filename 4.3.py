def pppp(o,j):
    p=0
    while p<len(j):
        if j[p]==int(o):
            return p
        p+=1
while True :
    try:
        target=int(input())
        nums=input()
        nums=nums.split(" ")
        for index, value in enumerate(nums):
            nums[index] = int(value)
        c=0        
        for x in nums:
            for y in nums:
                if x+y==target and x!=y and pppp(x,nums)+pppp(y,nums)!=c:
                    print(pppp(x,nums),end=" ")
                    print(pppp(y,nums))
                    c=pppp(x,nums)+pppp(y,nums)
    except :
        break
