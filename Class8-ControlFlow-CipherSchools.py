n = 5
for i in range(n):
    for j in range(n):
        print(i, end = " ")
    print()
    print("\n")

for i in range(n):
    for j in range(n):
        print(i, end = " ")

for i in range(n):
    for j in range(n):
        print(i, end = " ")
        print()
    
for i in range(n):
    for j in range(n):
        print(j, end = " ")
    print()

for i in range(n):
    for j in range(n):
        print(n-i, end = " ")
                # &
        print(n-j, end = " ")
                # &
        print(n-j-1, end = " ")
                # &
        print(j+1, end = " ")
                # &
        print(i+1, end = " ")
    print()

# max(1, 2, 3, 4, 5, 7,....)
n = 4
for i in range(n):
    for j in range(n):
        print(max(i+1, j+1, n-j), end = " ")
    print()

n = 8
for i in range(n):
    for j in range(n):
        i,j
        print((i, j), end = " ")
    print()
  
for i in range(n):
    for j in range(n):
        print(max(i, j), end = " ")
    print()

for i in range(n):
    for j in range(n):
        print(max(n-j-1, n-i-1), end = " ")
    print()

for i in range(n):
    for j in range(n):
       # print(max(max(i+1, j+1), max(n-j, n-i), end = " "))
    print()

sum([1, 2, 3, 4, 5, 6, 7, 8, 9,])