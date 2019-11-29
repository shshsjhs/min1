import math
a=1
while a>0:
    if math.sqrt(a+100)==int(math.sqrt(a+100)) and math.sqrt(a+168)==int(math.sqrt(a+168)):
        break 
    else: a=a+1
print(a)
