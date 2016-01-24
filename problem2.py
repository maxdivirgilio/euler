mySum=2
x = 1
y = 2
while x < 4000000 and y < 4000000:
    z = x + y
    x = y
    y = z
    if z%2==0:
        mySum = mySum + z
print(mySum)
