n=int(input("enter:"))
flag=0
for i in range(1,n):
    if(i*(i+1)==n):
        print("pronic")
        flag=1
        break
if(flag==0):
        print("not pronic")
