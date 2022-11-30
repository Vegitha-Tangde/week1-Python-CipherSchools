# Looping Statements

# 1.while
#a = 1
#while a < 10:
 #   print(a)
  #  a += 1

# 2.for -->works in sequences
name = "Cipher"
print(name.__iter__)
for c in name:
    print(c)

print(type(name))
print("***")
for c in name:
    print(c)
    print(type(c))

for i in range(5):
    print(i)

a = range(5)
print(a.__iter__)

# Break,Continue and Pass

print("aaaa" * 4)

for i in range(5):
    print(i)
    if i == 3:
        continue



for i in range(5):
    print(i)
    if i == 3:
        break

for i in range(5):
    print(i)
    i = 100

for i in range(5):
    print(i)
    i = 100
    print(i)

for i in range(5):
    print(i)
    del i

a = 1
print(a)
del a
#print(a)   # 'a'is not defined

if True:
    pass
    print("rest of the code")   # Empty statement

for i in range(5):
    print(i)
else:
    print("something")