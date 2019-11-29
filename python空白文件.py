while True:
    try:
        i=int(input())
        while i>0:
            n=int(input())
            x=int(n/3600)
            y=int((n-x*3600)/60)
            z=n-x*3600-y*60
            if(x>0 and x<10):
                print(0,end="")
                print(x,end="")
            if(x==0):
                print('00',end="")
            if(x>=10):
                print(x,end="")
            print(':',end="")
            if(y>0 and y<10):
                print(0,end="")
                print(y,end="")
            if(y==0):
                print('00',end="")
            if(y>=10):
                print(y,end="")
            print(':',end="")
            if(z>0 and z<10):
                print(0,end="")
                print(z)
            if(z==0):
                print('00')
            if(z>=10):
                print(z)
            i-=1
    except:
        break




