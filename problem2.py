mySum=0
x = 1
y = 2
if x < 4000000:
    and y < 4000000:
    z = x + y
    if z%2==0:
        mySum = mySum + z
while x < 4000000:
    and y < 4000000:
    x = y
    y = z
    z = x + y
if z%2==0:
    mySum = mySum + z
print(mySum)
