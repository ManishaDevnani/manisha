num=int(input("Enter no:"))
temp=num
sum=0
while (num>0):
    rem=num%10
    sum=sum+(rem**3)
    num=num//10
if sum==temp:
    print("Amstrong")
else:
    print("Not Amstrong")
