num= int(input("Enter the number for fibonacci series: "))

x=0
y=1

for i in range(num):
    sum=x+y
    print(x, end=" ")
    x=y
    y=sum
    
    

 