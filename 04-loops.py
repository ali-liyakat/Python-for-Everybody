# Loops and Iteration

# While Loop    indefinite loop

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Done")

# Loop Breaking keywords
# 1=> break

n = 10
while n > 0:
    print(n)
    n = n-1
    if n == 5:
        break
print("Done")

# 2=> continue

x = 5
while x > 0:
    x -= 1 
    if x == 3:  
        continue
    print(x) 
print("Loop finished!")


# For Loop      definite loop

for i in [1,2,3,4,5,6]:
    print(i)
print("Finished")

# find the largest number
largest = -1
for item in [12, 3, 50, 74, 10, 6]:
    if item > largest:
        largest = item
print("The largest is ",largest)
print("Done")

# find the smallest

small = None
for val in [12, 3 ,56, 89, 90]:
    if small is None:
        small = val
    elif val < small:
        small = val
print("Smallest is ", small)