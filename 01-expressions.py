# Constants:- fixed values which dont change
print(123)
print("Hello")


# Reserved keywords can't be used as variables or for other thing, like if, else, break, lambda, for. etc

# Variables:- a named place in memory used to store data
# we can change the content of variables

x = 7
print(x)
name = "Ali"
x = 20      # Assignment
print(x)

# operators in Python

z = 30  # assignment
a = z + x   # addition
b= z - x    # subtraaction
c = z* x    # multiplication
d =z / 2    # division
e = x % 2   # modulus/Remainder
f = x ** 2  # power

ans = x + c -z / a * d  # operator precedence. use brackets for evaluation.
                        # parenthesis > power > multiplication > addition ( left to right)
print(type(z))  # check type of data


# Type conversions

x = 12
x_f = float(x)
print(x_f)

print(int(x_f))

str = '120'
print(type(str))
str_i = str + '1'
print(str_i)
print(type(str_i))
print(int(str_i))

# taking input 

name = input("enter name ") # returns a string
print("welcome " + name)

# comments:- used for documentation
# single line comment
'''
multiline comment.
'''