mySum = 0
for x in range(1000):
    if x%3==0:
        mySum = mySum + x
    elif x%5==0:
        mySum = mySum + x
print(mySum)
