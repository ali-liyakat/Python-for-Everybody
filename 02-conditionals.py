# comparison operators
'''
>, >=, <, <=, ==, !=,,, hey evaluate and return True or False

'''
# If statement

x = 5
if x < 10:
    print("Smaller")
if x > 10:
    print("Bigger")
print("Finish")

# Nested if statement

y = 10
if y > 5:
    print("Greater than 5")
    if y < 20:
        print("less than 10")
print("Done")

# if else statement   Two-way decision

x = 10
if x > 5:
    print("Greater than 5")
else:
    print("less than 5")

# elif ladder   Multiway decision
x = 5
if x < 2:
    print("Small")
elif x < 10:
    print("Medium")
else:
    print("Large")

    # we can have No Else also


# try except sructure

astr = 'hello'
try:
    istr = int(astr)
except:
    istr = -1
print("first ", istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print(astr)