def f(x):
    if x>1:
        x==f(x-1)+f(x-2)
        return x
    if x==1:
        return 1
    else :
        return 1
print(f(40))

