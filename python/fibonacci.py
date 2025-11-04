n=int(input("enter number of terms"))
a,b=0,1
count=0
if n<=0:
    print("please enter a positive integer")
elif n==1:
    print("fibonacci sequence upto",n,"term:")
    print(a)
else:
    print("fibonacci sequence:")
    while count<n:
        print(a,end="")
        c=a+b
        a=b
        b=c
        count+=1
