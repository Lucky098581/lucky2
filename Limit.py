low=int(input("enter lower limit:"))
high=int(input("enter higher limit:"))
for i in range(low,high):
    count=0
    for j in range(1,i+1):
        if(i%j==0):
            count+=1
            if(count==2):
                print(i)
