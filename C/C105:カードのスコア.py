n = int(input())
Sum = 0

myList = [int(i) for i in input().split()]

for i in range(len(myList)):
    if myList[i] + 1 not in myList:
        Sum += myList[i]

print(Sum)
