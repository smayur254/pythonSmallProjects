# n = int(input())
# print()
# for i in range (0, n):
#     for j in range(0, n-i-1):
#         print(end=" ")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()

# n= int(input())
# for i in range(0, n):
#     for j in range(0, n-i-1):
#         print(end="")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print()



# var = [0] *40

# def fib(n):
#     if n<=1:
#         return n
#     if var[n] == 0:
#         var[n] = fib(n-1) + fib(n-2)
#     return var[n]
# n =int(input())
# print(fib(n))

# n = int(input())
# n1,n2=0, 1
# count =0
# sum = 0
# result = []
# if n<=0:
#     print("pos num")
# elif n==1:
#     print("sequence upto", n,":")
#     print(n1)
# else:
#     print("fib sequence:")
#     while count<n:
#         print(n1)
#         result.append(n1)
#         nth = n1+n2
#         n1=n2
#         n2=nth
#         count+=1
        
# print(result)
# for i in result:
#     sum = sum + i
#     print("i",sum)
# print("sum",sum)


n = int(input())

n1, n2 = 0, 1
count = 0

if n == 1:
    print(n1)
else:
    print("result")
    while count<n:
        print(n1)
        nth =n1+ n2
        n1 = n2
        n2 = nth  
        count+=1

