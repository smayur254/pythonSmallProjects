user_input = int(input("Lines for right angle start pattern: "))

for i in range(0, user_input+1):
    for j in range(0, i):
        print("*", end=" ")
    print()
for i in range(user_input, 0, -1):
    for j in range(0, i+1):
        print("*", end=" ")
    print()