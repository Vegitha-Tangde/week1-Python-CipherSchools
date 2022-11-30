'''Control flow statements'''

# Conditional statements

#if (true) {


# 1 indent = 2 spaces, 4 spaces, tab, 8 spaces

# if
a = True
if a:
    print("The value is true")
print("end")

# else
a = False
if a:
    print("This value is true")
else:
    print("This value is false")

# elif
a = 5
if a == 3:
    print("The value is 3")
elif a == 5:
    print("This value is 5")
else:
    print("This value is not 3 or 5")
