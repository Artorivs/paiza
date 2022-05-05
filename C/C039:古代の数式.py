from re import findall

myInput = [i for i in input().split('+')]
Sum = 0

for i in range(len(myInput)):
    Sum += len(findall("<", myInput[i])) * 10 + len(findall("/", myInput[i]))

print(Sum)

num,total =input().split('+'),0
for i in num:
    total += 10*(i.count('<'))+i.count('/')
print(total)
